import unittest
import os
from solutions.test_runner import execute_test


class TestEqual(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.langDir = os.path.dirname(os.getcwd())
        self.problemDir = os.path.dirname(self.langDir)
        self.testCaseDir = os.path.join(self.problemDir, 'tests')
        self.answerFilePath = os.path.join(os.getcwd(), 'answer.py')

    def test_case_0(self):
        input_path = os.path.join(self.testCaseDir, 'tc_0.in')
        output_path = os.path.join(self.testCaseDir, 'tc_0.out')
        script_output, ref_output = execute_test(self.answerFilePath, input_path, output_path)
        self.assertEqual(script_output, ref_output)

    def test_case_1(self):
        input_path = os.path.join(self.testCaseDir, 'tc_1.in')
        output_path = os.path.join(self.testCaseDir, 'tc_1.out')
        script_output, ref_output = execute_test(self.answerFilePath, input_path, output_path)
        self.assertEqual(script_output, ref_output)

    def test_case_15(self):
        input_path = os.path.join(self.testCaseDir, 'tc_1.in')
        output_path = os.path.join(self.testCaseDir, 'tc_1.out')
        script_output, ref_output = execute_test(self.answerFilePath, input_path, output_path)
        self.assertEqual(script_output, ref_output)
