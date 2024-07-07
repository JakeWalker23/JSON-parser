from src.parser import Parser
import sys

file_path = sys.argv[1]

if Parser.validate_json_file(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()

        Parser.is_valid_json(file_contents)
            
        print(str(Parser.is_valid_json(file_contents))) 

    file.close()

else:
    try:
        Parser.is_valid_json(file_path)
        print(str(Parser.is_valid_json(file_path)))
    except Exception:
        print('False')