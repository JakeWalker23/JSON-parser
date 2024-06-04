from src.parser import Parser
import pytest

'''
# Step 1
In this step your goal is to parse a valid simple JSON object, specifically: ‘{}’ 
and an invalid JSON file and correctly report which is which. 
So you should build a very simple lexer and parser for this step.
'''

def test_parser_returns_true_with_valid_JSON_object():
    data = "{}"
    
    assert Parser.parse_json(data) is True
    

def test_parser_returns_false_with_invalid_JSON_object():
    data = "{"

    assert Parser.parse_json(data) is False


def test_for_valid_JSON_file():
    file = "test.json"

    assert Parser.validate_json_file(file) is True


def test_for_invalid_JSON_file():
    file = "invalid_test.txt"

    assert Parser.validate_json_file(file) is False
