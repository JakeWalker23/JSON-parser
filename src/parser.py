class Parser:

    def parse_json(data):
        if data == {}:
            return True
        else:
            return False

    def validate_json_file(file):
        if '.json' in file:
            return True
        else:
            return False