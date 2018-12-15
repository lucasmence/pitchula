#coding: utf-8

import accessAudio
import audio
import config
import const
import funct
import image
import json
import ocr
import os
import speechRecognition
import spellcheck
import sys
import time
import tts

reload(sys)
sys.setdefaultencoding(const.All.TEXT_TYPE)

language = config.getLanguage()
thread = None

def getUserCommand(mode):
    
    currentInput = config.getInputType()
    print(currentInput)
    if (currentInput == 'keyboard'):
        return "K"
    elif (currentInput == 'voice'):
        language = config.getLanguage()
        speechTimes = 0
        audioStart = ()
        fullWordListJson = config.getWordList()
        fullWordList = json.load(fullWordListJson)
        wordList = []
        
        listStandardCharA = ['primeira', 'ajuda', 'capturar', 'anterior']
        listStandardCharB = ['segunda', 'começar', 'leitura']
        listStandardCharC = ['terceira', 'configurar', 'proximo']
        listStandardCharD = ['sair', 'cancelar']
        listStandardCharE = ['repita']
        if (language == 'en_us'):
            listStandardCharA = ['first', 'help', 'capture', 'previous']
            listStandardCharB = ['second', 'start', 'read']
            listStandardCharC = ['third', 'configure', 'next']
            listStandardCharD = ['leave', 'cancel']
            listStandardCharE = ['repeat']
        
        if (mode == 'home'):
            audioStart = ('030', '040', '041', '042', '043', '044')
            wordList.append(fullWordList[language]['040'])
            wordList.append(fullWordList[language]['041'])
            wordList.append(fullWordList[language]['042'])
            wordList.append(fullWordList[language]['043'])
            wordList.append(fullWordList[language]['044'])
        elif (mode == 'captureMode'):
            audioStart = ('030', '045', '046', '044')
            wordList.append(fullWordList[language]['045'])
            wordList.append(fullWordList[language]['046'])
            wordList.append(fullWordList[language]['044'])
        elif (mode == 'blockStart'):
            audioStart = ('030', '047', '046', '044')
            wordList.append(fullWordList[language]['047'])
            wordList.append(fullWordList[language]['046'])
            wordList.append(fullWordList[language]['044'])
        elif (mode == 'blockLoop'):
            audioStart = ('030', '048', '047', '049', '046','044')
            wordList.append(fullWordList[language]['048'])
            wordList.append(fullWordList[language]['047'])
            wordList.append(fullWordList[language]['049'])
            wordList.append(fullWordList[language]['046'])
            wordList.append(fullWordList[language]['044'])
        elif (mode == 'blockFinish'):''
            audioStart = ('030', '045', '046', '044')
            wordList.append(fullWordList[language]['045'])
            wordList.append(fullWordList[language]['046'])
            wordList.append(fullWordList[language]['044'])
        elif (mode == 'config'):
            audioStart = ('030', '032', '033', '034', '046', '044')
            wordList.append(fullWordList[language]['032'])
            wordList.append(fullWordList[language]['033'])
            wordList.append(fullWordList[language]['034'])
            wordList.append(fullWordList[language]['046'])
            wordList.append(fullWordList[language]['044'])
        elif (mode == 'configLanguageVoice'):
            audioStart = ('030', '032', '033', '046', '044')
            wordList.append(fullWordList[language]['032'])
            wordList.append(fullWordList[language]['033'])
            wordList.append(fullWordList[language]['046'])
            wordList.append(fullWordList[language]['044'])
        elif (mode == 'configLanguageChoose'):
            audioStart = ('030', '032', '033', '046', '044')
            wordList.append(fullWordList[language]['032'])
            wordList.append(fullWordList[language]['033'])
            wordList.append(fullWordList[language]['046'])
            wordList.append(fullWordList[language]['044'])
                
        accessAudio.speech(audioStart,language)

        word = ""
        wordCorrect = False
        finalResult = ""
        attempts = 2
 
        for index in range(0,attempts):
            
            if (wordCorrect == False):
                os.system("mpg321 -q AppData/speechStart.mp3")
                word = speechRecognition.recognizeAudio(language)
                os.system("mpg321 -q AppData/speechEnd.mp3")
                
                print("("+word+")")
                for currentWord in wordList:
                    print("<"+currentWord+">")
                    if (word == currentWord):
                        wordCorrect = True
                        break

                if (wordCorrect):
                    for currentWord in listStandardCharA:
                        print("*"+currentWord+"*")
                        if (word == currentWord): 
                            finalResult = "A"
                            break   
                    if (finalResult == ""):
                        for currentWord in listStandardCharB:
                            if (word == currentWord): 
                                finalResult = "B"
                                break
                    if (finalResult == ""):
                        for currentWord in listStandardCharC:
                            if (word == currentWord): 
                                finalResult = "C"
                                break 
                    if (finalResult == ""):
                        for currentWord in listStandardCharD:
                            if (word == currentWord): 
                                finalResult = "D"
                                break   
                    if (finalResult == ""):
                        for currentWord in listStandardCharE:
                            if (word == currentWord): 
                                finalResult = "E"
                                break
                    break
                elif (index < (attempts-1)):
                    audioError = ("031")
                    accessAudio.speech(audioError,language)
                    accessAudio.speech(audioStart,language)

        if (finalResult == ""):
            audioFail = ("035")        
            accessAudio.speech(audioFail,language)
            finalResult = "K"

        return finalResult

def destroyGui():
    global thread
    if (thread != None):
        config.setGuiMode('None')
        thread.form.close()
        #del thread
        
def createGui(value):
    #destroyGui()
    global thread  
    if (thread == None):
        thread = guiThread.Thread(value)
        thread.start()
    else:
        #thread.deleteAll()
        config.setGuiMode(value)
        thread.reload()
    
def restartLanguage():
    global language
    language = config.getLanguage()

def delCurrentForm():
    global form
    global app
    if (form != None):
        del form
    if (app != None):
        del app    

def readerMode(sliceCount):
    index = 0
    repeatMode = False
    silentMode = False #para leitura de blocos em brancos e evitar repeticao de frases de acesibilidade
    print sliceCount
    while index < sliceCount:
        audioSpeech = None
        createGui("ocrinit")
        if index == 0:
            audioSpeech = ('006','007','013')
            accessAudio.speech(audioSpeech,language)
            audioSpeech = ('009','010','013')
        elif (silentMode == False): 
            audioSpeech = ('008','009','010','013')
            accessAudio.speech(audioSpeech,language)
        
        input = ''
        while True: 
            #accessAudio.speech(audioSpeech,language)
            
            if (silentMode == False):
                input = getUserCommand('blockLoop')
                if (input == "K"):
                    input = buttons.takeAction()
            else:
                input = cmd.All.BUTTONS[cmd.All.BTN_TWO_DOT]
                
            if (input == cmd.All.BUTTONS[cmd.All.BTN_NONE_DOT]):
                createGui("audioinit")
                accessAudio.speech(audioSpeech,language)
                createGui("audiofinish")
                
            elif (input == cmd.All.BUTTONS[cmd.All.BTN_ONE_DOT] and index > 0):
                index = index - 1
                createGui("ocrinit")
                ocr.readPhoto(const.All.PATH_IMAGE_CROPPED + str(index)+'_'+ const.All.FILENAME_IMAGE_CROPPED + const.All.EXTENSION_IMAGE_CROPPED)
                createGui("spellcheckinit")
                spellcheck.verifyFile()
                createGui("ttsinit")
                audioExists = tts.convertText()
                
                if (audioExists == True):
                    createGui("audioinit")
                    audio.speech()
                else:
                    index = index + 1
                break
                
            elif (input == cmd.All.BUTTONS[cmd.All.BTN_TWO_DOT]):
                audioExists = False
                if (repeatMode == False):
                    repeatMode = True
                    createGui("ocrinit")
                    ocr.readPhoto(const.All.PATH_IMAGE_CROPPED + str(index)+'_'+ const.All.FILENAME_IMAGE_CROPPED + const.All.EXTENSION_IMAGE_CROPPED)
                    createGui("spellcheckinit")
                    spellcheck.verifyFile()
                    createGui("ttsinit")
                    audioExists = tts.convertText()
                    
                    if (audioExists == True):
                        createGui("audioinit")
                        audio.speech()
                        createGui("audiofinish")
                        if index == 0:
                            audioSpeech = ('009','010','013')
                        else: 
                            audioSpeech = ('008','009','010','013')
                        accessAudio.speech(audioSpeech,language)
                        if silentMode == True:
                            silentMode = False
                    else:
                        silentMode = True
                        index = index + 1
                        repeatMode = False
                        break
                else:
                    createGui("audioinit")
                    audio.speech()
                    createGui("audiofinish")
                         
            elif (input == cmd.All.BUTTONS[cmd.All.BTN_THREE_DOT] and index < sliceCount):
                index = index + 1
                repeatMode = False
                silentMode = True
                break
                
            elif (input == cmd.All.BUTTONS[cmd.All.BTN_FOUR_DOT]):
                createGui("menu")
                audioSpeech = ('014')
                accessAudio.speech(audioSpeech,language)
                index = sliceCount+1
                break
    
    if (input == cmd.All.BUTTONS[cmd.All.BTN_FOUR_DOT]):
        return ''
    
    audioSpeech = ('016','017','013')
    accessAudio.speech(audioSpeech,language)
    input = getUserCommand('blockFinish')
    if (input == "K"):
        input = buttons.takeAction()
    if (input != cmd.All.BUTTONS[cmd.All.BTN_TWO_DOT]):
        audioSpeech = ('014')
        accessAudio.speech(audioSpeech,language)
        led.activate(0,0)
        return ''
    else:
        return cmd.All.BUTTONS[cmd.All.BTN_TWO_DOT]
                
    
def imageMode():
    createGui("imageinit")
    currentAudio = ('005')
    accessAudio.speech(currentAudio,language)
    
    funct.clearFile(const.All.FILE_TYPE_IMAGE_CROPPED)
    image.fixImage()
    createGui("imagefinish")
    sliceCount = image.sliceImage()
    return readerMode(sliceCount)
    
def cameraMode():
    #ligar led de recepcao
    led.activate(0,0)
    led.activate(1,2)
    
    createGui("camerainit")
    
    currentAudio = ('003','023','024')
    accessAudio.speech(currentAudio,language)
    
    createGui("cameraready")
    
    #laco de repeticao
    input = None
    currentAudio = ('023','024')
    input = config.getRemoteInput()
    while (input != cmd.All.BUTTONS[cmd.All.BTN_ONE_DOT]) and (input != cmd.All.BUTTONS[cmd.All.BTN_FOUR_DOT]):
        input = getUserCommand('captureMode')
        if (input == "K"):
            input = buttons.takeAction()
        if (input == cmd.All.BUTTONS[cmd.All.BTN_NONE_DOT]):
            accessAudio.speech(currentAudio,language)
        elif (input != cmd.All.BUTTONS[cmd.All.BTN_ONE_DOT]):
            audioSpeech = '014'
            accessAudio.speech(audioSpeech,language)
            led.activate(0,0)
            return ''
    if (input == cmd.All.BUTTONS[cmd.All.BTN_FOUR_DOT]):
        audioSpeech = ('014')
        accessAudio.speech(audioSpeech,language)
        led.activate(0,0)
        return ''        
    #captura da imagem
    
    #ligar led - branco
    led.activate(1,2)
    led.activate(1,3)
    createGui("cameracapture")
    photoPath = const.All.PATH_IMAGE+const.All.FILENAME_IMAGE+const.All.EXTENSIONS_IMAGE[0]
    os.system("raspistill -o "+photoPath) #removido +" -w 1920 -h 1080 "
    createGui("camerafinish")
    #desligar led
    led.activate(0,0)
    currentAudio = ('004')
    accessAudio.speech(currentAudio,language)
    return imageMode()

def changeLanguage():
    accessAudio.speechLanguagesTypes()
    inputCmd = getUserCommand('configLanguageChoose')
    if (inputCmd == "K"):
        inputCmd = buttons.takeAction()
    if (inputCmd == cmd.All.BUTTONS[cmd.All.BTN_ONE_DOT]):
        config.setLanguage('pt_br')
    elif (inputCmd == cmd.All.BUTTONS[cmd.All.BTN_TWO_DOT]):
        config.setLanguage('en_us')
    restartLanguage()    

def configurationMode():
    led.activate(0,0)
    
    createGui("config")
    
    currentAudio = ('076', '074', '075', '025')
    accessAudio.speech(currentAudio,language)

    inputCmd = ''

    while (inputCmd != cmd.All.BUTTONS[cmd.All.BTN_FOUR_DOT]):
        inputCmd = getUserCommand('config')
        if (inputCmd == "K"):
            inputCmd = buttons.takeAction()

        if (inputCmd == cmd.All.BUTTONS[cmd.All.BTN_NONE_DOT]):
            accessAudio.speech(currentAudio,language)

        elif (inputCmd == cmd.All.BUTTONS[cmd.All.BTN_ONE_DOT]): 
            #linguagem e usabilidade de voz

            speechVoiceCode = ''
            print(config.getInputType )
            if (config.getInputType == 'keyboard'):
                    speechVoiceCode = '077'
            else:
                    speechVoiceCode = '078'	

            currentAudio = ('061', speechVoiceCode, '025')
            accessAudio.speech(currentAudio,language)

            inputCmd = ''

            while (inputCmd != cmd.All.BUTTONS[cmd.All.BTN_FOUR_DOT]):
                    inputCmd = getUserCommand('configLanguageVoice')
                    if (inputCmd == "K"):
                        inputCmd = buttons.takeAction()

                    if (inputCmd == cmd.All.BUTTONS[cmd.All.BTN_NONE_DOT]):
                        accessAudio.speech(currentAudio,language)

                    elif (inputCmd == cmd.All.BUTTONS[cmd.All.BTN_ONE_DOT]):           		
                        #troca de linguagem
                        changeLanguage()
                        optionAudio = ('067')
                        accessAudio.speech(optionAudio,language)
                        break

                    elif (inputCmd == cmd.All.BUTTONS[cmd.All.BTN_TWO_DOT]):
                            if (config.getInputType == 'voice'):
                                    config.setInputType('keyboard')
                            else:
                                    config.setInputType('voice')

                            optionAudio = ('079','067')
                            accessAudio.speech(optionAudio,language)
                            break

        elif (inputCmd == cmd.All.BUTTONS[cmd.All.BTN_TWO_DOT]):
            #teste de camera e led
            optionAudio = ('062')
            accessAudio.speech(optionAudio,language)
            
            photoPath = const.All.PATH_IMAGE+const.All.FILENAME_IMAGE_TEST_CAMERA+const.All.EXTENSION_IMAGE_TEST_CAMERA
            if (os.path.isfile(photoPath)):
                os.remove(photoPath)
                
            os.system("raspistill -o "+photoPath+" -w 1920 -h 1080 ")
            
            cameraWorking = False
            if (os.path.isfile(photoPath)):
                cameraWorking = True
                os.remove(photoPath)
            
            
            if (cameraWorking == True):
                optionAudio = ('063','064')
            else:
                optionAudio = ('063','064')
            
            accessAudio.speech(optionAudio,language)
            
            optionAudio = ('066')
            accessAudio.speech(optionAudio,language)
            
            led.activate(0,0)
            led.activate(1,1)
            time.sleep(0.5)
            led.activate(0,0)
            led.activate(1,2)
            time.sleep(0.5)
            led.activate(0,0)
            led.activate(1,3)
            time.sleep(0.5)
            led.activate(0,0)
            led.activate(1,1)
            led.activate(1,2)
            time.sleep(0.5)
            led.activate(0,0)
            led.activate(1,1)
            led.activate(1,3)
            time.sleep(0.5)
            led.activate(0,0)
            led.activate(1,2)
            led.activate(1,3)
            time.sleep(0.5)
            led.activate(1,0)
            time.sleep(2)            
            led.activate(0,0)
                        
            optionAudio = ('063','064')
            accessAudio.speech(optionAudio,language)
            
            optionAudio = ('067')
            accessAudio.speech(optionAudio,language)
            
            
        elif (inputCmd == cmd.All.BUTTONS[cmd.All.BTN_THREE_DOT]):
            #teste de framework e internet
            optionAudio = ('068')
            accessAudio.speech(optionAudio,language)
            
            photoPath = const.All.PATH_IMAGE+const.All.FILENAME_IMAGE_TEST_OCR+const.All.EXTENSION_IMAGE_TEST_OCR
            if (os.path.isfile(photoPath)):
                ocrStatus = False
                spellcheckStatus = False
                ttsStatus = False
                
                ocrText = ocr.readPhoto(photoPath)
                      
                fileText = const.All.PATH_TEXT+const.All.FILENAME_TEXT+const.All.EXTENSION_TEXT

                if (os.path.isfile(fileText)):
                 
                    if (ocrText == 'testee'):
                        ocrStatus = True
                        
                    spellcheckText = spellcheck.verifyFile()
                    
                    if (spellcheckText.strip() == 'teste'):
                        spellcheckStatus = True
                    
                    ttsStatus = tts.convertText()
                    
                    optionAudio = ('069')
                    accessAudio.speech(optionAudio,language)
                    if (ocrStatus == True):
                        optionAudio = ('070')
                    else:
                        optionAudio = ('071')         
                    accessAudio.speech(optionAudio,language)
                    
                    optionAudio = ('072')
                    accessAudio.speech(optionAudio,language)
                    if (ttsStatus == True):
                        optionAudio = ('070')
                    else:
                        optionAudio = ('071')         
                    accessAudio.speech(optionAudio,language)
                    
                    optionAudio = ('073')
                    accessAudio.speech(optionAudio,language)
                    if (spellcheckStatus == True):
                        optionAudio = ('070')
                    else:
                        optionAudio = ('071')         
                    accessAudio.speech(optionAudio,language)
                    
                    optionAudio = ('067')
                    accessAudio.speech(optionAudio,language)
                    
                
                else:
                    optionAudio = ('019')
                    accessAudio.speech(optionAudio,language)     
            
            else:
                optionAudio = ('019')
                accessAudio.speech(optionAudio,language)    
            
        elif (inputCmd == cmd.All.BUTTONS[cmd.All.BTN_FOUR_DOT]):
            currentAudio = ('014')
            accessAudio.speech(currentAudio,language)
            led.activate(0,0)
            return ''

    return ''    
    
def systemStart():

    led.activate(0,0)
    
    createGui("menu")
    
    if ((config.getFirstTime() == "0") or (config.getAlwaysAsk() == "True")):
        changeLanguage()
        config.setFirstTime("1")
    
    audioStart = ('001', '020', '002', '060', '024')
    accessAudio.speech(audioStart,language)

    inputCmd = ''
    lastAudio = audioStart
    lastActionResult = ''
    
    while (inputCmd != cmd.All.BUTTONS[cmd.All.BTN_FOUR_DOT]):
        if (config.getGuiMode != "menu"):
            createGui("menu")
            
        if (lastActionResult == ''):
            inputCmd = getUserCommand('home')
            print(inputCmd)
            if (inputCmd == "K"):
                inputCmd = buttons.takeAction()
        else:
            inputCmd = lastActionResult

        currentAudio = None
            
        if (inputCmd == cmd.All.BUTTONS[cmd.All.BTN_NONE_DOT]):
            accessAudio.speech(lastAudio,language)
            lastActionResult = ''
        elif (inputCmd == cmd.All.BUTTONS[cmd.All.BTN_TWO_DOT]):
            lastActionResult = cameraMode()
        elif (inputCmd == cmd.All.BUTTONS[cmd.All.BTN_ONE_DOT]):
            currentAudio = ('021','022')
            accessAudio.speech(currentAudio,language)
            lastActionResult = ''
        elif (inputCmd == cmd.All.BUTTONS[cmd.All.BTN_THREE_DOT]):
            lastActionResult = configurationMode()
        elif (inputCmd == cmd.All.BUTTONS[cmd.All.BTN_FOUR_DOT]):
            currentAudio = ('014')
            accessAudio.speech(currentAudio,language)
            led.activate(0,0)                  
        
        if (currentAudio != None):
            lastAudio = currentAudio
    
    destroyGui()
    global thread
    thread.deleteAll()
    return 0
            
#system boot
#systemStart()
            
    


    
