import re
import os
import sys
import pytest
import subprocess
from answer import *


@pytest.fixture(scope='module')
def graph_tc_0():
    return {
        1: {2,3},
        2: {1},
        3: {1,4,5},
        4: {3},
        5: {3}
    }


@pytest.fixture(scope='module')
def graph_tc_31():
    return {
        1: {2, 3},
        2: {1,4,5},
        3: {1,6,7},
        4: {2},
        5: {2},
        6: {3},
        7: {3}
    }


def test_bfs_tc_0(graph_tc_0):
    visiting_order = bfs(graph_tc_0, 1)
    assert visiting_order == [1, 3, 2, 5, 4]


def test_bfs_tc_31(graph_tc_31):
    visiting_order = bfs(graph_tc_31, 1)
    assert visiting_order == [1, 3, 2, 7, 6, 5, 4]


def test_get_rooted_tree(graph_tc_0):
    rooted_tree, _ = get_rooted_tree(graph_tc_0, 1)

    assert rooted_tree[1]['CHILDREN'] == {2, 3}
    assert rooted_tree[1]['PARENT'] is None
    assert rooted_tree[1]['IS_LEAF'] is False

    assert rooted_tree[2]['CHILDREN'] == set()
    assert rooted_tree[2]['PARENT'] == 1
    assert rooted_tree[2]['IS_LEAF'] is True

    assert rooted_tree[3]['CHILDREN'] == {4,5}
    assert rooted_tree[3]['PARENT'] == 1
    assert rooted_tree[3]['IS_LEAF'] is False

    assert rooted_tree[4]['CHILDREN'] == set()
    assert rooted_tree[4]['PARENT'] == 3
    assert rooted_tree[4]['IS_LEAF'] is True

    assert rooted_tree[5]['CHILDREN'] == set()
    assert rooted_tree[5]['PARENT'] == 3
    assert rooted_tree[5]['IS_LEAF'] is True


def test_calculate_combinations_tc_0(graph_tc_0):
    rooted_tree, visiting_order = get_rooted_tree(graph_tc_0, 1)
    memo = calculate_combinations(rooted_tree, visiting_order)
    assert memo[1, 'RED', 'BLUE'] + memo[1, 'BLUE', 'RED'] == 4


def test_calculate_combinations_tc_31(graph_tc_31):
    rooted_tree, visiting_order = get_rooted_tree(graph_tc_31, 1)
    memo = calculate_combinations(rooted_tree, visiting_order)
    assert memo[1, 'RED', 'BLUE'] + memo[1, 'BLUE', 'RED'] == 6


def test_answer():
    print('This is dir:', os.getcwd())
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
            return subprocess_output.rstrip('\n').rstrip('\r'), output_reference.rstrip('\n').rstrip('\r')

    langDir = os.path.dirname(os.getcwd())
    problemDir = os.path.dirname(langDir)
    testCaseDir = os.path.join(problemDir, 'test_data')
    answerFilePath = os.path.join(os.getcwd(), 'answer.py')
    input_path = os.path.join(testCaseDir, 'tc_11.in')
    output_path = os.path.join(testCaseDir, 'tc_11.out')
    script_output, ref_output = execute_test(answerFilePath, input_path, output_path)
    assert script_output == ref_output
