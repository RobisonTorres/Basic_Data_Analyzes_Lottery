import json

def open_file():
     
     # This function opens and loads json files.
     try:
        file = open('results.json')
        previous_result = json.load(file)
        return previous_result
     except:
         return 'File not found.'