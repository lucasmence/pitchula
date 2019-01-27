#!/usr/bin/env python
# coding: utf-8

import enchant
import os
import codecs
import sys
import re as refactoring

class Spellcheck():

    def __init__(self, constants):
        self._constants = constants
    
    def verifyFile(self, filename, language, textType, textTypeCodecs):
        reload(sys);
        sys.setdefaultencoding(textType)
        fileInput = filename
        fileText = self._constants._FIELD_EMPTY_STRING

        for listItem in open(fileInput,self._constants._COMMAND_READ_MODE).read().splitlines():   
            fileText = fileText+self._constants._FIELD_SPACE+listItem
        
        if ((fileText == None) or (len(fileText.strip()) < self._constants._MINIMUM_TEXT_SIZE)):
            return self._constants._INDEX_RETURN_ERROR
        
        fileOutput = filename  
        textOutput = self._constants._FIELD_EMPTY_STRING
        wordlist = fileText.split()      
        dictionary = enchant.Dict(language)
            
        for word in wordlist:
        
            word = refactoring.sub(self._constants._COMMAND_FIX_CHARACTERS,self._constants._FIELD_EMPTY_STRING,word.strip())
            oldWord = word
            if (len(word) > self._constants._MINIMUM_WORD_SIZE):          
                if (dictionary.check(word) == False):
                    fixedWordlist = dictionary.suggest(word)
                    if (len(fixedWordlist) > self._constants._MINIMUM_WORD_NEW_SIZE):
                        word = fixedWordlist[self._constants._INDEX_RECOMMENDED_WORD]
            
            newWord = oldWord 
            if (oldWord != word):
                newWord = word    
            
            textOutput = textOutput + newWord + self._constants._FIELD_SPACE
        
        if (os.path.isfile(fileOutput)):
            os.remove(fileOutput)
        
        os.system(self._constants._COMMAND_CREATE_FILE+fileOutput)
        fileOutputText = codecs.open(fileOutput,self._constants._COMMAND_WRITE_MODE,textTypeCodecs)
        fileOutputText.write(self._constants._COMMAND_WRITE_FILE+textOutput)
        fileOutputText.close()  

        return self._constants._INDEX_RETURN_OK
