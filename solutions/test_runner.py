import subprocess
import tempfile
import stat
import sys
import os


def execute_test(solution_path, input_file_path, output_file_path):
    # create a temporary executable based on solution source
    # do not delete it as we'll need to make this file executable later
    with tempfile.NamedTemporaryFile(delete=False) as executable_solution_file:
        # get the contents of the solution script
        with open(solution_path) as solution_file:
            solution_text = solution_file.read()
            # get python executable path
            python_executable_path = sys.executable
            # add shebang line
            shebang_line = '#!' + python_executable_path + '\n'
            executable_solution_file.write(shebang_line.encode('ascii'))
            # add sys import
            executable_solution_file.write('import sys\n'.encode('ascii'))
            # append the rest as the contents of solution script
            executable_solution_file.write(solution_text.encode('ascii'))

    # make temporary file executable
    current_stat = os.stat(executable_solution_file.name)
    os.chmod(executable_solution_file.name, current_stat.st_mode | stat.S_IEXEC)

    # open a context for input file
    with open(input_file_path) as input_reference_file:
        # start subprocess
        answer_subprocess = subprocess.Popen(
            executable_solution_file.name,
            stdin=input_reference_file, # serve input file context as an input
            stdout=subprocess.PIPE  # let the process print to the PIPE
        )
        # get output of subprocess
        subprocess_output = answer_subprocess.communicate()[0].decode('ascii')

    # compare with output for test case
    with open(output_file_path) as output_reference_file:
        output_reference = output_reference_file.read()
        return subprocess_output.rstrip('\n'), output_reference.rstrip('\n')
