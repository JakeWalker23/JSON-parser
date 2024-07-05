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


def test_parser_returns_value_from_dict_key():
    data = "{\"name\": \"jake\"}"

    result = Parser.parse_json_to_object(data) 
    
    assert result['name'] == 'jake'


def test_parser_returns_values_from_dict_keys():
    data = "{\"name1\": \"Jake\", \"name2\": \"Thomas\"}"
    
    result = Parser.parse_json_to_object(data)

    assert result['name1'] == 'Jake'
    assert result['name2'] == 'Thomas'


def test_parser_returns_correct_values_for_string_and_int():
    data = "{\"name\": \"Jake\", \"age\": 23}"
    
    result = Parser.parse_json_to_object(data)

    assert result['name'] == 'Jake'
    assert result['age'] == 23


def test_parser_returns_values_for_string_number_and_boolean():
    data = "{\"name\": \"Jake\", \"age\": \"23\", \"bellend\": True}"
    
    result = Parser.parse_json_to_object(data)

    assert result['name'] == 'Jake'
    assert result['age'] == 23
    assert result['bellend'] == True 


def test_parser_returns_values_for_multiple_string_number_and_boolean():
    data = "{\"name1\": \"Jake\", \"age1\": \"23\", \"bellend1\": True, \"name2\": \"Thomas\", \"age2\": \"40\", \"bellend2\": True}"
    
    result = Parser.parse_json_to_object(data)

    assert result['name1'] == 'Jake'
    assert result['age1'] == 23
    assert result['bellend1'] == True 

    assert result['name2'] == 'Thomas'
    assert result['age2'] == 40
    assert result['bellend2'] == True 


def test_parser_returns_correct_values_for_None_values():
    data = "{\"name\": \"Jake\", \"age\": \"23\", \"bellend\": None}"
    
    result = Parser.parse_json_to_object(data)

    assert result['name'] == 'Jake'
    assert result['age'] == 23
    assert result['bellend'] == None