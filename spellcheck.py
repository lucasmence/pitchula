# -*- coding: utf-8 -*-
import enchant
import const
import os
import funct
import codecs
import cmd
# encoding=utf8  
import sys
import re
import config

reload(sys)  
sys.setdefaultencoding('utf8')


def wordCheck(input):
    
    if (len(input) <= 1):
        return input
    
    language = config.getLanguage()
    if (language == "pt_br"):
        language = "pt_BR"
    elif (language == "en_us"):
        language = "en_US"
    
    dictionary = enchant.Dict(language)
    
    if (dictionary.check(input) == False):
        fixedWordlist = dictionary.suggest(input)
        if (len(fixedWordlist) > 0):
            return fixedWordlist[0]
        else:
            return input
    else:
        return input

def replaceWords(value):
    
    newWord = value
    
    value = value.lower().strip()
    if (value == "deã"):
        newWord = "dela"
    elif (value == "empatla"):
        newWord = "empatia"
        
    return newWord
    
def verifyFile():
    
    fileInput = const.All.PATH_TEXT+const.All.FILENAME_TEXT+const.All.EXTENSION_TEXT
    if (os.path.isfile(fileInput) == False):
        print(colors.bashColors.FAIL+'Arquivo texto nao encontrado, execute o processamento da img novamente digitando "'+colors.bashColors.OKBLUE+cmd.All.OCR+colors.bashColors.FAIL+'"!')
        return
    
    fileText = ''
    for listItem in open(fileInput,'r').read().splitlines():   
        fileText = fileText+' '+listItem
    
    fileText = funct.removeAccents(fileText)
    if ((fileText == None) or (len(fileText.strip()) < 4)):
        print(colors.bashColors.FAIL+'O arquivo texto esta em branco, realize a captura da imagem novamente digitando "'+colors.bashColors.OKBLUE+cmd.All.CAMERA+colors.bashColors.FAIL+'"!')
        return ""
    else:
        fileOutput = const.All.PATH_TEXT+const.All.FILENAME_TEXT+const.All.EXTENSION_TEXT
        
        print('Antigo:' + fileText)
        wordlist = fileText.split()
        
        textOutput = ''
        
        language = config.getLanguage()
        if (language == "pt_br"):
            language = "pt_BR"
        elif (language == "en_us"):
            language = "en_US"
        
        dictionary = enchant.Dict(language)
            
        for word in wordlist:
           
            word = re.sub(r'[^\w\s]','',word.strip())  #remove todos o tipo de espacamento e substitui caracteres malignos
            oldWord = word
            if (len(word) > 2):          
                if (dictionary.check(word) == False):
                    fixedWordlist = dictionary.suggest(word)
                    if (len(fixedWordlist) > 0):
                        word = fixedWordlist[0]
             
            oldWordChecked = replaceWords(oldWord)
            newWord = ""
            if (oldWord == word):
                newWord = replaceWords(word)    
            elif (oldWordChecked != oldWord):
                newWord = oldWordChecked
            elif (oldWord != word and oldWord == oldWordChecked):
                newWord = replaceWords(word)    
            
            textOutput = textOutput + newWord + ' '
        
        print('Novo:' + textOutput)
        
        if (os.path.isfile(fileOutput)):
            os.remove(fileOutput)
              
        os.system('touch '+fileOutput)
        fileOutputText = codecs.open(fileOutput,'w','utf-8')
        fileOutputText.write(u"\ufeff"+textOutput)
        fileOutputText.close()  
    
        return textOutput