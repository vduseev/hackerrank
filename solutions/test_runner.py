import subprocess
import tempfile
import stat
import sys
import os


def execute_test(solution_path, input_file_path, output_file_path):
    # get python executable path
    python_executable_path = sys.executable

    # open a context for input file
    with open(input_file_path) as input_reference_file:
        # start subprocess
        answer_subprocess = subprocess.Popen(
            [python_executable_path, solution_path],
            stdin=input_reference_file, # serve input file context as an input
            stdout=subprocess.PIPE  # let the process print to the PIPE
        )
        # get output of subprocess
        subprocess_output = answer_subprocess.communicate()[0].decode('ascii')

    # compare with output for test case
    with open(output_file_path) as output_reference_file:
        output_reference = output_reference_file.read()
        return subprocess_output.rstrip('\n'), output_reference.rstrip('\n')
