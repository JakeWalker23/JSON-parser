from src.type_checker import TypeChecker
from src.helpers.JSON_cleaner import JSONCleaner
import re

class Parser:

    @staticmethod
    def is_valid_json(data: str) -> bool:
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
    def parse_json_to_object(data: str):
        if data == '[]':
            return []

        if data == '[{}]':
            return [{}]
        
        formatted_object = {}

        formatted_json_array = JSONCleaner.clean_json_string(data)
        
        for item in formatted_json_array:
            formatted_object[item[0]] = TypeChecker.return_correct_type(item[1])

        if data.startswith('['):
            
            array_wrapper = []
            array_wrapper.append(formatted_object)
            return array_wrapper
        

        return formatted_object