
import json

def getLanguage():
    
    with open('Language/config.json') as file:
            jsonObject = json.load(file)
            
    return format(jsonObject['language'])

def getVersion():
    
    with open('Language/config.json') as file:
            jsonObject = json.load(file)
            
    return format(jsonObject['version'])

def getGuiMode():
    
    with open('guiMode.json') as file:
            jsonObject = json.load(file)
            
    return format(jsonObject['guiMode'])

def getRemoteInput():
    
    with open('remoteInput.json') as file:
            jsonObject = json.load(file)
            
    return format(jsonObject['value'])

def getFirstTime():
    
    with open('Language/config.json') as file:
            jsonObject = json.load(file)
            
    return format(jsonObject['firstTime'])

def getAlwaysAsk():
    
    with open('Language/config.json') as file:
            jsonObject = json.load(file)
            
    return format(jsonObject['alwaysAsk'])

def getJsonText(value):
    language = getLanguage();
    with open('Language/'+language+'.json') as file:
            jsonObject = json.load(file)
            
    return format(jsonObject[value])

def getInputType():
    
    with open('inputType.json') as file:
            jsonObject = json.load(file)
            
    return format(jsonObject['inputType'])

def getWordList():
              
    return open('wordList.json')


#setters   
def setLanguage(value):
    
    version = getVersion()
    firstTime = getFirstTime()
    alwaysAsk = getAlwaysAsk()
    
    jsonFile = {'language':value, 'version':version, 'firstTime':firstTime, 'alwaysAsk':alwaysAsk}

    with open('Language/config.json', 'w') as file:
         json.dump(jsonFile, file)

def setGuiMode(value):
    
    jsonFile = {'guiMode':value}

    with open('guiMode.json', 'w') as file:
         json.dump(jsonFile, file)

def setRemoteInput(value):
    
    jsonFile = {'value':value}

    with open('remoteInput.json', 'w') as file:
         json.dump(jsonFile, file)

def setFirstTime(value):
    
    language = getLanguage()
    version = getVersion()
    alwaysAsk = getAlwaysAsk()

    jsonFile = {'language':language, 'version':version, 'firstTime':value, 'alwaysAsk':alwaysAsk}

    with open('Language/config.json', 'w') as file:
         json.dump(jsonFile, file)

def setInputType(value):
    
    jsonFile = {'inputType':value}

    with open('inputType.json', 'w') as file:
         json.dump(jsonFile, file)

