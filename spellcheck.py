#!/usr/bin/env python
# coding: utf-8

import constants
import enchant
import os
import codecs
import sys
import re as refactoring
    
def verifyFile(filename, language, textType, textTypeCodecs):

    reload(sys)  
    sys.setdefaultencoding(textType)
    fileInput = filename
    fileText = constants.FIELD_EMPTY_STRING

    for listItem in open(fileInput,constants.COMMAND_READ_MODE).read().splitlines():   
        fileText = fileText+constants.FIELD_SPACE+listItem
    
    if ((fileText == None) or (len(fileText.strip()) < constants.MINIMUM_TEXT_SIZE)):
        return constants.INDEX_RETURN_ERROR
    
    fileOutput = filename  
    textOutput = constants.FIELD_EMPTY_STRING
    wordlist = fileText.split()      
    dictionary = enchant.Dict(language)
        
    for word in wordlist:
    
        word = refactoring.sub(constants.COMMAND_FIX_CHARACTERS,constants.FIELD_EMPTY_STRING,word.strip())
        oldWord = word
        if (len(word) > constants.MINIMUM_WORD_SIZE):          
            if (dictionary.check(word) == False):
                fixedWordlist = dictionary.suggest(word)
                if (len(fixedWordlist) > constants.MINIMUM_WORD_NEW_SIZE):
                    word = fixedWordlist[constants.INDEX_RECOMMENDED_WORD]
        
        newWord = oldWord 
        if (oldWord != word):
            newWord = word    
        
        textOutput = textOutput + newWord + constants.FIELD_SPACE
    
    if (os.path.isfile(fileOutput)):
        os.remove(fileOutput)
        
    os.system(constants.COMMAND_CREATE_FILE+fileOutput)
    fileOutputText = codecs.open(fileOutput,constants.COMMAND_WRITE_MODE,textTypeCodecs)
    fileOutputText.write(constants.COMMAND_WRITE_FILE+textOutput)
    fileOutputText.close()  

    return constants.INDEX_RETURN_OK