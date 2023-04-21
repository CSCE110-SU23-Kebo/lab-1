import unittest
import glob
import os

from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner
from test_generator import get_data, strip_basename, build_test_class


def reweight_score(results, problem_scores):
    raw_scores = {}
    raw_max_scores = {}
    for problem in problem_scores.keys():
        raw_scores[problem] = 0
        raw_max_scores[problem] = 0

    for test in results['tests']:
        raw_scores[test['number']] += test['score']
        raw_max_scores[test['number']] += test['max_score']

    scores = 0
    for problem, score in problem_scores.items():
        scores += raw_scores[problem] * problem_scores[problem] / raw_max_scores[problem]

    results['score'] = round(scores)


def rename_tests(results):
    for test in results['tests']:
        test['number'] = f"{test['number']}.py"


if __name__ == '__main__':
    suite = unittest.TestSuite()

    data_files = get_data()
    for filename in data_files:
        cls = build_test_class(filename)
        suite.addTest(unittest.makeSuite(cls))

    problem_scores = {}
    for filename in data_files:
        basename, _ = os.path.splitext(os.path.basename(filename))
        basename = strip_basename(basename)
        score_file = f"score_{basename}"
        try:
            with open(score_file, 'r') as f:
                score = float(f.read())
        except:
            score = 0
        problem_scores[basename] = score

    def proc_results(results):
        reweight_score(results, problem_scores)
        rename_tests(results)  # do last if test number is used

    results_path = '/autograder/results/results.json'
    if not os.getcwd().startswith('/autograder'):
        results_path = 'results.json'

    with open(results_path, 'w') as f:
        JSONTestRunner(
                stream=f,
                visibility='visible',
                post_processor=proc_results,
            ).run(suite)
