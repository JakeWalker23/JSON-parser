from src.parser import Parser
import sys

file_name = sys.argv[1]

file = open(file_name, "r")
content = file.read()
print(content)
print(Parser.parse_json(str(content)))
file.close()
