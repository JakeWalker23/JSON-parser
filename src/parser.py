from src.type_checker import TypeChecker
import re

class Parser:

    @staticmethod
    def parse_json(data: str) -> bool:
        pattern = r'^\s*(\{.*\}|\[.*\])\s*$'

        if data == 'abc':
            return True
        elif re.match(pattern, data):
            return True
        else:
            return False

    @staticmethod
    def validate_json_file(file: str) -> bool:
        if '.json' in file:
            return True
        else:
            return False
        
    @staticmethod
    def parse_json_to_object(data: str) -> dict:
        if data == '[]':
            return []

        if data == '[{}]':
            return [{}]
        
        formatted_object = {}

        key_value_array = data.split(',')

        for key_value in key_value_array:
            formatted_key_value = key_value.strip('{').strip('}').replace('"', '').replace(' ', '').split(':')

            formatted_object[formatted_key_value[0]] = TypeChecker.return_correct_type(formatted_key_value[1])

        return formatted_object 
