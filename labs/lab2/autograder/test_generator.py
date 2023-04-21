import unittest
import csv
import difflib
import glob
import os
import re
import string
import subprocess
import sys

from gradescope_utils.autograder_utils.decorators import weight, visibility, number, tags
from gradescope_utils.autograder_utils.files import check_submitted_files


DEBUG = False
OMITTED_COLUMNS = ['test_case', 'description', 'visibility']
BASE_DIR = 'test_data'


class TestMetaclass(type):
    """
    Metaclass for unittest.TestCase to dynamically generate test cases.
    """

    def __new__(cls, name, bases, attrs):
        """
        name : string
            name of the class
        bases : obj
            base classes
        attrs: dict
            has the following keys
            - cases: array of dictionaries each with keys 'id', 'input', 'visibility'
            - basename: name of the problem (i.e. q1)
            - filter_output: function for filtering the output for the problem
        """
        attrs['setUp'] = cls.generate_setUp()
        for case in attrs['cases']:
            fn = cls.generate_test(
                    case['input'], case['visibility'], test_weight=case['weight'])
            fn.__doc__ = f"{attrs['basename']}.py: {case['test_case']} ({case['description']})"

            attrs[cls.test_name(case['id'])] = fn
            klass = super(TestMetaclass, cls).__new__(cls, name, bases, attrs)

        # reserved unittest attributes
        klass.setUpClass = cls.generate_setUpClass()

        # class attributes
        klass.filename = f"{attrs['basename']}.py"
        klass.missing_files = False
        return klass

    @classmethod
    def generate_setUpClass(cls):
        @classmethod
        def setUpClass(cls):
            """Check submitted files"""
            missing_files = check_submitted_files([f'{cls.basename}.py'], '.')
            if len(missing_files) > 0:
                cls.missing_files = missing_files
        return setUpClass

    @classmethod
    def generate_setUp(cls):
        def setUp(self):
            self.longMessage = False
            self.maxDiff = None
            self.assertFalse(self.missing_files, f'Missing {self.missing_files}')
        return setUp

    @classmethod
    def generate_test(cls, inp, vis, test_weight=0):
        """ Set up test case """

        @weight(test_weight)
        @visibility(vis)
        def test_output(self):
            calc = subprocess.Popen(f'python3 -u {self.basename}.py'.split(),
                                    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    encoding='utf8')
            raw_output, err = calc.communicate(inp, 1)

            calc_sample = subprocess.Popen(f'python3 -u {self.basename}_sample.py'.split(),
                                    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    encoding='utf8')
            raw_output_sample, err_sample = calc_sample.communicate(inp, 1)

            # filter output if filter_output is defined; otherwise, use raw output
            output = raw_output
            output_sample = raw_output_sample
            if self.filter_output:
                output = self.filter_output(output)
                output_sample = self.filter_output(output_sample)

            if DEBUG:
                print(f"Outputs (raw, filtered): {(repr(raw_output), repr(output))}")

            if err:
                print(f"{err}")

            # unittest uses difflib.ndiff which has issues for strings with '\n'
            # in the middle i.e. "a\naab\n"
            # workaround: split string by '\n' for difflib.ndiff
            msg = None
            if output != output_sample:
                trunc_output, trunc_output_sample = unittest.util._common_shorten_repr(
                        output, output_sample)

                diff = difflib.ndiff(output.splitlines(), output_sample.splitlines())
                diff_output = '\n'.join(diff)

                msg = f"\"{trunc_output}\" != \"{trunc_output_sample}\"\n\n{diff_output}"

            self.assertEqual(output, output_sample, msg=msg)

        return test_output

    @classmethod
    def test_name(cls, id):
        return f'test_{id}'

def gen_test_cases(filename, max_score=0):
    """
    Create a dictionary of test cases.

    filename : str
        filename of csv
    max_score : int
        max score for the question
    """
    cases = []
    with open(filename) as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            # skip omitted columns
            inp_arr = [row[name] for name in filter(
                lambda name: name not in OMITTED_COLUMNS, reader.fieldnames)]

            # skip if row is entirely empty
            if not any(row.values()):
                continue

            # construct test case
            inp = '\n'.join(inp_arr) + '\n'
            cases.append({
                'id': i,
                'input': inp, 
                'visibility': row['visibility'],
                'test_case': row['test_case'],
                'description': row['description'],
            })

        # set weight for each test case
        w = max_score/len(cases)
        cases = [dict(case, weight=w) for case in cases]

        if DEBUG:
            print(f"Test cases: {cases}")

    return cases

def build_test_class(filename, max_score=0, relative_weight=1):
    basename, _ = os.path.splitext(os.path.basename(filename))
    cases = gen_test_cases(filename, max_score=max_score/relative_weight)

    # wrap filter_{basename} function with self argument
    def filter_output(self, *args, **kwargs):
        filt = getattr(sys.modules[__name__], f'filter_{basename}', None)
        return filt(*args, **kwargs)

    cls = TestMetaclass(
            f'Test{"".join([s.capitalize() for s in basename.split("_")])}',
            (unittest.TestCase,),
            {
                'basename': basename,
                'cases': cases,
                'filter_output': filter_output,
            }
        )
    return cls

def get_data():
    return sorted(glob.glob(os.path.join(BASE_DIR, '*.csv')))

### Custom output filters for each question
# for {basename}.csv, functions have signature filter_{basename}(out)

STRIP_CHARS = f'{string.whitespace}'

def filter_register(out):
    return ''.join(out.strip(STRIP_CHARS).splitlines(True)[-9:])

def filter_password(out):
    return out.strip(STRIP_CHARS).splitlines()[-1]

def filter_rates(out):
    out = ': '.join(out.strip(STRIP_CHARS).split(': ')[-4:])
    return out

###
