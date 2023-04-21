import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility, number, tags
from gradescope_utils.autograder_utils.files import check_submitted_files
import subprocess

class TestFiles(unittest.TestCase):
    @weight(0)
    def test_submitted_files(self):
        """Check submitted files"""
        missing_files = check_submitted_files(['reverse.py'])
        for path in missing_files:
            print('Missing {0}'.format(path))
        self.assertEqual(len(missing_files), 0, 'Missing some required files!')
        print('All required files submitted!')

class TestIntegration(unittest.TestCase):
    def setUp(self):
        pass

    @weight(0)
    def test_1_1(self):
        calc = subprocess.Popen('python3 -u reverse.py'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8')
        student_output = calc.communicate("NY12345006789\n", 1)

        calc_sample = subprocess.Popen('python3 -u live_activity_3.py'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8')
        solution_output = calc_sample.communicate("NY12345006789\n", 1)
        self.assertEqual(student_output[0].split(':')[-1].strip(), solution_output[0].split(':')[-1].strip())

    @weight(0)
    def test_1_2(self):
        calc = subprocess.Popen('python3 -u reverse.py'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8')
        student_output = calc.communicate("CA12321\n", 1)

        calc_sample = subprocess.Popen('python3 -u live_activity_3.py'.split(),
                                       stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                       encoding='utf8')
        solution_output = calc_sample.communicate("CA12321\n", 1)

        self.assertEqual(student_output[0].split(':')[-1].strip(), solution_output[0].split(':')[-1].strip())

