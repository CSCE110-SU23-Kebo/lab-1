import unittest
import os

from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner
from test_generator import get_data, build_test_class


def reweight_score(results, score):
    max_score = 0
    for test in results['tests']:
        max_score += test['max_score']
    results['score'] = round(results['score'] * score / max_score)


if __name__ == '__main__':
    suite = unittest.TestSuite()

    data_files = get_data()
    for filename in data_files:
        cls = build_test_class(filename)
        suite.addTest(unittest.makeSuite(cls))

    try:
        with open('score', 'r') as f:
            score = float(f.read())
    except:
        score = 0

    def proc_results(results):
        reweight_score(results, score)

    results_path = '/autograder/results/results.json'
    if not os.getcwd().startswith('/autograder'):
        results_path = 'results.json'

    with open(results_path, 'w') as f:
        JSONTestRunner(
                stream=f,
                visibility='visible',
                post_processor=proc_results,
            ).run(suite)
