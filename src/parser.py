import re



class Parser:

    @staticmethod
    def parse_json(data: str) -> bool:
        pattern = r'^\s*(\{.*\}|\[.*\])\s*$'

        if data == "{}":
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