import re

class TypeChecker:

    @staticmethod
    def return_correct_type(data):
        if '"' in data:
            return str(data.replace('"', ""))
        
        elif data.isnumeric():
            return int(data)
        
        elif data == 'True':
            return True
        
        elif data == 'False':
            return False
            
        elif data == 'None':
            return None
        
        return str(data)