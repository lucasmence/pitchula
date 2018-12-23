import json

def getValue(path, field):
    """Get the value from the json file"""

    value = None
    try:    
        with open(path, 'r') as file:
            jsonFile = json.load(file)  

        value = format(jsonFile[field]) 
    except:
        return ''

    if (value is None):        
        return  ''
    else:
        return value
