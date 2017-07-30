import os
import re
import sys
import unittest

from test_runner import execute_test


class TestCase(unittest.TestCase):
    """
    Template for a python 3 test case for hackerrank-challenge project.

    Assumes that project has a following structure:
    - solutions
      - category
        - sub category
          - language 1
            - inversed_baseline
              - answer.py
              - test_answer.py
            - solution_...
          - language ...
          - test_data
            - tc_run_code.in
            - tc_run_code.out
            - ...
      - test_case.py
      - test_runner.py
    """

    def setUp(self):
        self.maxDiff = None
        self.langDir = os.path.dirname(os.getcwd())
        self.problemDir = os.path.dirname(self.langDir)
        self.testCaseDir = os.path.join(self.problemDir, 'test_data')
        self.answerFilePath = os.path.join(os.getcwd(), 'answer.py')

    def execute_test_case(self):
        caller_name = sys._getframe().f_back.f_code.co_name
        digits_pattern = re.compile(r'(test_case_)(.+)')
        digits = digits_pattern.search(caller_name).group(2)
        test_case_name = 'tc_' + digits
        input_path = os.path.join(self.testCaseDir, test_case_name + '.in')
        output_path = os.path.join(self.testCaseDir, test_case_name + '.out')
        script_output, ref_output = execute_test(self.answerFilePath, input_path, output_path)
        self.assertEqual(script_output, ref_output)
