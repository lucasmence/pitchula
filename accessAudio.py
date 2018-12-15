import os
import cmd
import const

def executeAudio(filePath):
    if (os.path.isfile(filePath) == True):
        os.system("mpg321 -q "+filePath);
    return            

def speech(argument,language):
    
    if isinstance(argument,tuple):    
        for index in range(0, len(argument)):
            filePath = const.All.PATH_ACCESSIBILITY + language + '/' + argument[index] + const.All.EXTENSION_AUDIO
            executeAudio(filePath)
                    
    elif isinstance(argument,str):
        filePath = const.All.PATH_ACCESSIBILITY + language + '/' + argument + const.All.EXTENSION_AUDIO
        executeAudio(filePath)
        
                
    return

def speechLanguagesTypes():
    
    filePath = const.All.PATH_ACCESSIBILITY + 'pt_br' + '/' + '099' + const.All.EXTENSION_AUDIO
    executeAudio(filePath)
    
    filePath = const.All.PATH_ACCESSIBILITY + 'en_us' + '/' + '099' + const.All.EXTENSION_AUDIO
    executeAudio(filePath)    
    




