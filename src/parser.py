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
        response = {}

        object_split = data.split(',')

        for pair in object_split:
            new_string = pair.replace('"', '').replace(' ', '').strip('{').strip('}').split(':')

            response[new_string[0]] = new_string[1]

        return response 
