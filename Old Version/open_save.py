import json

def open_file():
     
     # This function opens and loads json files.
     try:
        file = open('pre_results.json')
        previous_result = json.load(file)
        return previous_result
     except:
         return 'File not found.'

def save_file(x):
    
    # This function saves the updated results.
    with open('pre_results.json', 'w') as file:
        json.dump(x, file, indent = 1)

