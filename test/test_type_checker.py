from src.type_checker import TypeChecker
import pytest

def test_type_checker_recognises_string():
    data = '\"abc\"'

    assert type(TypeChecker.return_correct_type(data)) is str
    assert TypeChecker.return_correct_type(data) == 'abc'

def test_type_checker_recognises_int():
    data = '23'

    assert type(TypeChecker.return_correct_type(data)) is int
    assert TypeChecker.return_correct_type(data) == 23

def test_type_checker_recognises_string_is_not_int():
    data = '"23"'

    assert type(TypeChecker.return_correct_type(data)) is str
    assert TypeChecker.return_correct_type(data) == '23'