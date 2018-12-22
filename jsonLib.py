import json

def getValue(path, field):

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
