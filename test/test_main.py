import pytest
import subprocess

def test_main_returns_true_when_ran_through_cli():
    '''This test takes a string of empty JSON and passes
    it as a argument to main.py as argv[1]'''

    data = '{}'

    cmd = ["python", "main.py", data]

    result = subprocess.run(cmd, capture_output=True, text=True)

    assert result.stdout.strip() == 'True'