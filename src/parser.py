class Parser:

    def parse_json(data):
        if data == {}:
            return True
        else:
            return False

    def validate_json_file(file):
        if file.split('.')[1] == 'json':
            return True
        else:
            return False