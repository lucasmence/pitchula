#coding: utf-8

import functions
import image
import jsonLib
import ocr
import os
import spellcheck
import sys
import tts

reload(sys)   
                
def systemStart():

    variables = "data/strings/variables.json"
    sys.setdefaultencoding(jsonLib.getValue(variables,"textType"))
    languageType = jsonLib.getValue(variables,"languageCurrent")
    languagePath = jsonLib.getValue(variables,"languagePath")+languageType+".json"

    if (len(sys.argv) <= 2):
        print(jsonLib.getValue(languagePath,"errorParameters"))
        return 1    

    pathImage = sys.argv[1]
    pathAudio = sys.argv[2]
    extension = os.path.splitext(pathImage)[1][1:]

    if not (os.path.isfile(pathImage)):
        print(jsonLib.getValue(languagePath,"errorInput"))
        return 1        
    if (not (os.path.dirname(pathAudio))) and (os.path.dirname(pathAudio) != ""):
        print(jsonLib.getValue(languagePath,"errorOutput"))
        return 1
    if not (extension in jsonLib.getValue(variables,"imageExtension")):
        print(jsonLib.getValue(languagePath,"errorFiletype"))
        return 1    

    print(jsonLib.getValue(languagePath,"messageWelcome")) 
    functions.clearAll(variables)

    internalImage = jsonLib.getValue(variables,"imagePath")+"/"+jsonLib.getValue(variables,"imageFilename")+"."+jsonLib.getValue(variables,"imageExtensionDefault")
    internalText = jsonLib.getValue(variables,"textPath")+"/"+jsonLib.getValue(variables,"textFilename")+"."+jsonLib.getValue(variables,"textExtension")
    
    image.fixImage(pathImage,internalImage)

    ocr.readPhoto(internalImage,internalText)

    spellcheck.verifyFile(internalText,languageType)

    ttsLanguage = jsonLib.getValue(languagePath,"gTTSCode")
    audioExists = tts.convertText(internalText,pathAudio,ttsLanguage)

    if (audioExists == 0):
        print(jsonLib.getValue(languagePath,"messageFinish"))
    
    return 0
            
systemStart()
            
    


    
