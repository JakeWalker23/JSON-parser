from src.parser import Parser
import pytest

'''
Step 3
In this step your goal is to extend the parser
to parse a JSON object containing string, numeric, boolean
and null values, i.e.:

{
  "key1": true,
  "key2": false,
  "key3": null,
  "key4": "value",
  "key5": 101
}

You can test against the files in the folder tests/step3.
'''

def test_parser_returns_true_with_valid_nested_JSON_object():
    data = "{\"key1\": True, \"key2\": False, \"key3\": None, \"key4\": \"value\", \"key5\": 101}"
    
    assert Parser.parse_json(data) is True

def test_parser_returns_true_with_valid_JSON():
    data = "abc"
    
    assert Parser.parse_json(data) is True
    

def test_parser_returns_true_with_valid_JSON_object():
    data = "{\"key\": \"value\"}"
    
    assert Parser.parse_json(data) is True


def test_parser_returns_true_with_empty_JSON_object():
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
