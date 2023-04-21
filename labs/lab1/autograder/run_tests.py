import unittest

from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner
from test_generator import get_data, build_test_class


if __name__ == '__main__':
    suite = unittest.TestSuite()

    data_files = get_data()
    for filename in data_files:
        cls = build_test_class(filename, relative_weight=len(data_files))
        suite.addTest(unittest.makeSuite(cls))

    with open('/autograder/results/results.json', 'w') as f:
        JSONTestRunner(visibility='visible', stream=f).run(suite)
