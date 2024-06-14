from src.parser import Parser
import sys
import json

file_path = sys.argv[1]

if Parser.validate_json_file(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()

        Parser.parse_json(file_contents)
            
        print(str(Parser.parse_json(file_contents))) 

    file.close()

else:
    try:
        Parser.parse_json(data=file_path)
        print(str(Parser.parse_json(data=file_path)))
    except Exception:
        print('False')