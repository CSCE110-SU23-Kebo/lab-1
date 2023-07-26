import unittest
from unittest.mock import patch

import csv
import difflib
import functools
import glob
import importlib
import io
import os
import random
import re
import signal
import shutil
import subprocess
import sys
import traceback

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
        'notes',            # hidden notes on test cases
        ]
BASE_DIR = 'test_data'


def run_program(filename, inp=None):
    calc = subprocess.Popen(f'python3 -u {filename}'.split(),
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            encoding='utf8')
    return calc.communicate(inp, 1)


def compute_diff(s1, s2):
    # unittest uses difflib.ndiff which has issues for strings with '\n'
    # in the middle i.e. "a\naab\n"
    # workaround: split string by '\n' for difflib.ndiff
    out = None
    if s1 != s2:
        trunc_s1, trunc_s2 = unittest.util._common_shorten_repr(s1, s2)
        diff = difflib.ndiff(s1.splitlines(True), s2.splitlines(True))
        diff_output = ''.join(diff)
        out = f"\"{trunc_s1}\" != \"{trunc_s2}\"\n\n{diff_output}"
    return out


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
        fn = None
        if len(attrs['cases']) == 0:
            fn = cls.generate_test(attrs['basename'], assert_output=attrs['assert_output'])
            if attrs['assert_output']:
                fn.__doc__ = f"Check for matching output"
            else:
                fn.__doc__ = f"Please manually check the output"
            attrs[cls.test_name(0)] = fn
        else:
            for case in attrs['cases']:
                fn = cls.generate_test_input(
                        attrs['basename'], case['input'], case['visibility'], run_test=case['run_test'],
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
    def generate_test(cls, basename, assert_output=True):
        @number(basename)
        @weight(1)
        def test_output(self):
            inp = None
            if self.gen_input:
                inp = self.gen_input()

            output, err = run_program(f"{self.basename}.py", inp)
            output_sample, err_sample = run_program(f"{self.basename}_sample.py", inp)

            if err:
                print(f"{err}")
                if "EOFError" in err:
                    print((f"{self.basename}.py likely expected more inputs "
                            "than it was given. Please debug this test case "
                            "manually.\n"))

            if self.run_test:
                print(output)
                self.run_test()

            if assert_output:
                msg = compute_diff(output, output_sample)
                self.assertEqual(output, output_sample, msg=msg)
            else:
                print(output)

        return test_output

    @classmethod
    def generate_test_input(cls, basename, inp, vis, run_test=None, print_input=False, assert_output=True, test_weight=0):
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

            if run_test:
                if not run_test(self):
                    return

            raw_output, err = run_program(f"{self.basename}.py", inp)
            raw_output_sample, err_sample = run_program(f"{self.basename}_sample.py", inp)

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

            if DEBUG:
                print(f"Outputs (raw, filtered): {(repr(raw_output), repr(output))}")
                print(output_sample)

            if err:
                print(f"{err}")
                if "EOFError" in err:
                    print((f"{self.basename}.py likely expected more inputs "
                            "than it was given. Please debug this test case "
                            "manually.\n"))

            if assert_output:
                msg = compute_diff(output, output_sample)
                self.assertEqual(output, output_sample, msg=msg)
            else:
                print(output)

        return test_output

    @classmethod
    def test_name(cls, id):
        return f'test_{id}'


def gen_test_cases(filename, gen_input=None, run_test=None):
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
            if gen_input:
                inp = gen_input(None, **inp_dict)

            if i not in cases:
                cases[i] = {
                    'id': i,
                    'input': inp, 
                    'visibility': row['visibility'],
                    'test_case': row['test_case'],
                    'output_test_case': output_test_case,
                    'description': row['description'],
                    'weight': float(row['weight']) if row['weight'].isnumeric() else 1,
                    'kwargs': inp_dict,
                    'run_test': None,
                }
            else:
                if output_test_case:
                    cases[i]['output_test_case'] = output_test_case
                prior_inp = cases[i]['input'][:-1]  # drop \n added to prior_inp
                cases[i]['input'] = '\n'.join([prior_inp, inp])
                prior_test_case = cases[i]['test_case']
                cases[i]['test_case'] = ' '.join([prior_test_case, row['test_case']])

    if run_test:
        for case in cases.values():
            kwargs = case['kwargs'].copy()
            case['run_test'] = functools.partial(run_test, inp=case['input'], **kwargs)

    if DEBUG:
        print(f"Test cases: {cases}")

    return cases.values()

def build_test_class(filename):
    basename, _ = os.path.splitext(os.path.basename(filename))

    assert_output = True
    if basename[-1] == '@':
        basename = basename[:-1]
        assert_output = False

    # wrap filter_{basename} function with self argument
    filt = getattr(sys.modules[__name__], f'filter_{basename}', None)
    gen = getattr(sys.modules[__name__], f'gen_{basename}', None)
    test = getattr(sys.modules[__name__], f'test_{basename}', None)

    filter_output = None
    gen_input = None
    run_test = None
    if filt:
        def filter_output(self, *args, **kwargs):
            filt = getattr(sys.modules[__name__], f'filter_{basename}', None)
            return filt(*args, **kwargs)

    if gen:
        def gen_input(self, *args, **kwargs):
            filt = getattr(sys.modules[__name__], f'gen_{basename}', None)
            return filt(*args, **kwargs)

    if test:
        def run_test(self, *args, **kwargs):
            test = getattr(sys.modules[__name__], f'test_{basename}', None)
            return test(self, *args, **kwargs)

    cases = gen_test_cases(filename, gen_input, run_test)

    cls = TestMetaclass(
            f'Test{"".join([s.capitalize() for s in basename.split("_")])}',
            (unittest.TestCase,),
            {
                'basename': basename,
                'cases': cases,
                'run_test': run_test,
                'gen_input': gen_input,
                'filter_output': filter_output,
                'assert_output': assert_output,
            }
        )
    return cls

def get_programs():
    return sorted(glob.glob('*_sample.py'))

def get_data():
    return sorted(glob.glob(os.path.join(BASE_DIR, '*.csv')))

def strip_basename(basename):
    return basename.strip('@')

### Custom output filters for each question
# for {basename}.csv, functions have signature:
# filter_{basename}(out) - returns a filtered version of out
# gen_{basename}(*args, **kwargs) - returns an input string for the program
#   if this is defined, then inputs in {basename}.csv are supplied to gen_{basename} if any.
# test_{basename}(testCase, **kwargs) - returns true to assert output checking; otherwise, false
#   for manual function testing where inputs will be passed as kwargs

def handle_anchor_idx(body, anchor):
    try:
        anchor_idx = body.index(anchor)
    except:
        raise ValueError(f'Unable to find "{anchor}" in output.')
    return anchor_idx + len(anchor)

def handle_filtering(out, skip, replace):
    out_arr = out.splitlines(True)
    filtered_out = []
    for line in out_arr:
        skip_line = any([line.startswith(token) for token in skip])
        if skip_line or (line == '\n' and filtered_out[-1] == '\n'):
            continue

        # replace substrings in line with newlines if previous filtered line
        # is not a newline
        for replace_regex in replace:
            replacement = '\n'
            if len(filtered_out) > 0 and filtered_out[-1] == replacement:
                replacement = ''
            line = re.sub(replace_regex, replacement, line)

        if len(line) > 0:
            filtered_out.append(line)
    return ''.join(filtered_out)

def handle_random_call(program, sample, *args, seed=0, **kwargs):
    random.seed(seed)
    result, expected = None, None
    try:
        result = program(*args, **kwargs)
    except Exception as e:
        print(f"Your function {program.__name__} produced an error.")
        print(traceback.format_exc())
        raise
    random.seed(seed)
    try:
        expected = sample(*args, **kwargs)
    except Exception as e:
        print("Our sample function produced an error. Please notify a TA.")
        print(traceback.format_exc())
        raise
    return result, expected


def test_sentences(testCase, **kwargs):
    testCase.assertFalse(testCase.missing_files, f'Missing {testCase.missing_files}')

    inp = kwargs.get('inp')
    raw_output, err = run_program(f"{testCase.basename}.py", inp)
    with open('sentences.txt', 'r') as f:
        result = f.read()

    raw_output_sample, err_sample = run_program(f"{testCase.basename}_sample.py", inp)
    with open('sentences.txt', 'r') as f:
        expect = f.read()

    testCase.assertEqual(result, expect, msg=compute_diff(result, expect))

###
