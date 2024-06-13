import pytest
import subprocess

def test_main_returns_true_when_valid_json_passed_in_argv_1():
    '''This test takes an empty JSON and passes
    it as a argument to main.py as argv[1]'''

    data = "{}"

    cmd = ["python", "main.py", data]

    result = subprocess.run(cmd, capture_output=True, text=True)

    assert result.stdout.strip() == 'True'


def test_main_returns_false_when_passed_invalid_json_in_argv_1():
    data = "[}"

    cmd = ["python", "main.py", data]

    result = subprocess.run(cmd, capture_output=True, text=True)

    assert result.stdout.strip() == 'False'


def test_main_returns_true_when_valid_json_file_is_passed_in_sys_argv_1():
    '''This test takes a valid json file containing valid json
    and returns True'''

    json_file = 'test\\data\\pass1.json'

    cmd = ["python", "main.py", json_file]

    result = subprocess.run(cmd, capture_output=True, text=True)

    assert result.stdout.strip() == 'True'