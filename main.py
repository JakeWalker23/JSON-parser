from src.parser import Parser
import sys

data = sys.argv[1]

print(Parser.parse_json(data))