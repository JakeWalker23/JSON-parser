from src.parser import Parser
import sys
import json

json_data = sys.argv[1]

if Parser.validate_json_file(json_data):
    with open(json_data) as file:
        content = json.load(file)

        Parser.parse_json(content)
            
        print(Parser.parse_json(content)) 

    file.close()

else:
    try:
        json_payload = json.loads(json_data)
        
        Parser.parse_json(json_payload)
        print(Parser.parse_json(json_payload))
    except:
        print('False')