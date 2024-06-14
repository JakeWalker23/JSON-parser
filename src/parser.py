import json

class Parser:

    def parse_json(data):
        if data == "{}":
            return True
        
        try:
            json.loads(data)
            return True
        except ValueError:
            return False

    def validate_json_file(file):
        if '.json' in file:
            return True
        else:
            return False