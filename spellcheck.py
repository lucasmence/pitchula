# -*- coding: utf-8 -*-
# encoding=utf8  

import enchant
import os
import codecs
import sys
import re as refactoring
    
def verifyFile(filename, language):

    reload(sys)  
    sys.setdefaultencoding("utf8")
    fileInput = filename
    fileText = ""

    for listItem in open(fileInput,"r").read().splitlines():   
        fileText = fileText+" "+listItem
    
    if ((fileText == None) or (len(fileText.strip()) < 4)):
        return 1
    
    fileOutput = filename  
    textOutput = ""
    wordlist = fileText.split()      
    dictionary = enchant.Dict(language)
        
    for word in wordlist:
    
        word = refactoring.sub(r'[^\w\s]',"",word.strip())
        oldWord = word
        if (len(word) > 2):          
            if (dictionary.check(word) == False):
                fixedWordlist = dictionary.suggest(word)
                if (len(fixedWordlist) > 0):
                    word = fixedWordlist[0]
        
        newWord = oldWord 
        if (oldWord != word):
            newWord = word    
        
        textOutput = textOutput + newWord + " "
    
    if (os.path.isfile(fileOutput)):
        os.remove(fileOutput)
        
    os.system("touch "+fileOutput)
    fileOutputText = codecs.open(fileOutput,"w","utf-8")
    fileOutputText.write(u"\ufeff"+textOutput)
    fileOutputText.close()  

    return 0