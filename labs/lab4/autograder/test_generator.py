import unittest
import csv
import difflib
import glob
import os
import subprocess
import sys

from gradescope_utils.autograder_utils.decorators import weight, visibility, number, tags
from gradescope_utils.autograder_utils.files import check_submitted_files


DEBUG = False
RESERVED_COLS = [
        'repl_id',          # for combining inputs in read-eval loops
        'weight',           # test case weight for question/problem
        'test_case',        # string representation of the test case
        'output_test_case', # include test case in output
        'description',      # description of the test
        'visibility',       # test visibility (see gradescope docs)
        ]
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
                    attrs['basename'], case['input'], case['visibility'],
                    print_input=case['output_test_case'], test_weight=case['weight'])

            # sets the test header on gradescope
            fn.__doc__ = f"{case['test_case']} ({case['description']})"

            attrs[cls.test_name(case['id'])] = fn
            klass = super(TestMetaclass, cls).__new__(cls, name, bases, attrs)

        # reserved unittest class attributes
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
    def generate_test(cls, basename, inp, vis, print_input=False, test_weight=0):
        """ Set up test case """

        @number(basename)
        @weight(test_weight)
        @visibility(vis)
        def test_output(self):
            if print_input:
                for i, line in enumerate(inp.split('\n')):
                    if len(line) == 0:
                        continue
                    print(f"Input {i+1}: {line}")
                print()

            calc = subprocess.Popen(f'python3 -u {self.basename}.py'.split(),
                                    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    encoding='utf8')
            raw_output, err = calc.communicate(inp, 1)

            calc_sample = subprocess.Popen(f'python3 -u {self.basename}_sample.py'.split(),
                                    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    encoding='utf8')
            raw_output_sample, err_sample = calc_sample.communicate(inp, 1)

            if DEBUG:
                print(f"Outputs (raw, filtered): {(repr(raw_output), repr(output))}")

            if err:
                print(f"{err}")
                if "EOFError" in err:
                    print((f"{self.basename}.py likely expected more inputs "
                            "than it was given. Please debug this test case "
                            "manually.\n"))

            # filter output if filter_output is defined; otherwise, use raw output
            output = raw_output
            output_sample = raw_output_sample
            if self.filter_output:
                try:
                    output = self.filter_output(output)
                except ValueError as e:
                    print((f"{e} Computing diff with unfiltered output. "
                            "Resolve any errors or debug your program "
                            "then review your output format.\n"))
                else:
                    output_sample = self.filter_output(output_sample)

            # unittest uses difflib.ndiff which has issues for strings with '\n'
            # in the middle i.e. "a\naab\n"
            # workaround: split string by '\n' for difflib.ndiff
            msg = None
            if output != output_sample:
                trunc_output, trunc_output_sample = unittest.util._common_shorten_repr(
                        output, output_sample)

                diff = difflib.ndiff(output.splitlines(True), output_sample.splitlines(True))
                diff_output = ''.join(diff)

                msg = f"\"{trunc_output}\" != \"{trunc_output_sample}\"\n\n{diff_output}"

            self.assertEqual(output, output_sample, msg=msg)

        return test_output

    @classmethod
    def test_name(cls, id):
        return f'test_{id}'

def gen_test_cases(filename):
    """
    Create a dictionary of test cases.

    filename : str
        filename of csv
    """
    cases = {}
    with open(filename) as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            # skip omitted columns
            inp_dict = {}
            inp_arr = []
            for name in filter(
                    lambda name: name not in RESERVED_COLS, reader.fieldnames):
                if row[name]:
                    inp_arr.append(row[name])
                inp_dict[name] = row[name]

            # skip if row is entirely empty
            if not any(row.values()):
                continue

            if row.get('repl_id'):
                i = hash(row['repl_id'])

            output_test_case = False
            if row['output_test_case']:
                output_test_case = True

            # construct test case
            inp = '\n'.join(inp_arr) + '\n'
            if i not in cases:
                cases[i] = {
                    'id': i,
                    'input': inp, 
                    'visibility': row['visibility'],
                    'test_case': row['test_case'],
                    'output_test_case': output_test_case,
                    'description': row['description'],
                    'weight': float(row['weight']) if row['weight'].isnumeric() else 1,
                }
            else:
                if output_test_case:
                    cases[i]['output_test_case'] = output_test_case
                prior_inp = cases[i]['input'][:-1]  # drop \n added to prior_inp
                cases[i]['input'] = '\n'.join([prior_inp, inp])
                prior_test_case = cases[i]['test_case']
                cases[i]['test_case'] = ' '.join([prior_test_case, row['test_case']])

        if DEBUG:
            print(f"Test cases: {cases}")

    return cases.values()

def build_test_class(filename):
    basename, _ = os.path.splitext(os.path.basename(filename))
    cases = gen_test_cases(filename)

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

def handle_anchor_idx(body, anchor):
    try:
        anchor_idx = body.index(anchor)
    except:
        raise ValueError(f'Unable to find "{anchor}" in output.')
    return anchor_idx

def filter_barcode(out):
    anchor_idx = handle_anchor_idx(out, "Matrix A:")
    return out[anchor_idx:]

###
