from subprocess import call
import speech_recognition

def recognizeAudio(languageAudio):
    record = speech_recognition.Recognizer()
    record.energy_threshold=4000
    with speech_recognition.Microphone(device_index = 2, sample_rate = 44100) as source:
        print('Listening...')
        audio = record.listen(source)
        print('Processing...')
     
        try:
            if (languageAudio == 'pt_br'):
                languageAudio = 'pt-br'
            elif (languageAudio == 'en_us'):
                languageAudio = 'en-us'
                
            print('passei daqui')
                
            message = record.recognize_google(audio, language=languageAudio)
            
            print('aqui ta acabando')
            
            print(message)
            
            return message    
        except:
            print('Audio not even recognized!')
            return ''
