import unittest
import os
from solutions.test_runner import execute_test


class TestCase(unittest.TestCase):
    """
    Template for a python 3 test case for hackerrank-challenge project.

    Assumes that project has a following structure:
    - solutions
      - category
        - sub category
          - language 1
            - solution_01
              - answer.py
              - test_answer.py
            - solution_...
          - language ...
          - tests
            - tc_0.in
            - tc_0.out
            - ...
      - test_case.py
      - test_runner.py
    """

    def setUp(self):
        self.maxDiff = None
        self.langDir = os.path.dirname(os.getcwd())
        self.problemDir = os.path.dirname(self.langDir)
        self.testCaseDir = os.path.join(self.problemDir, 'tests')
        self.answerFilePath = os.path.join(os.getcwd(), 'answer.py')

    def run_test(self, input_file_path, output_file_path):
        input_path = os.path.join(self.testCaseDir, input_file_path)
        output_path = os.path.join(self.testCaseDir, output_file_path)
        script_output, ref_output = execute_test(self.answerFilePath, input_path, output_path)
        self.assertEqual(script_output, ref_output)
