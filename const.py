import cmd

class All:
    APP_TITLE = 'Pitchula'
    APP_NAME = 'pitchula'
    APP_VERSION = '1.0.0'
    AUTHOR = 'lucasmence'
    AUTHOR_EMAIL = 'mencethedeveloper@gmail.com'
    DIVISOR = '_'
    DEFAULT_TEXT_INPUT = colors.bashColors.HEADER+APP_NAME+DIVISOR+colors.bashColors.OKGREEN+APP_VERSION+colors.bashColors.ENDC 
    
    TEXT_TYPE = 'utf-8'
    
    PATH_IMAGE = 'Images/'
    FILENAME_IMAGE = 'photo'
    FILENAME_IMAGE_TEST_CAMERA = 'photoTest'
    FILENAME_IMAGE_TEST_OCR = 'imgTest'
    EXTENSIONS_IMAGE = ('.jpg','.png')
    EXTENSION_IMAGE_TEST_CAMERA = '.jpg'
    EXTENSION_IMAGE_TEST_OCR = '.png'
    FILE_TYPE_IMAGE = 'image'
    
    PATH_IMAGE_CROPPED = 'Temp/'
    FILENAME_IMAGE_CROPPED = 'photo'
    EXTENSION_IMAGE_CROPPED = ('.png')
    FILE_TYPE_IMAGE_CROPPED = 'cropped'
    
    PATH_TEXT = 'Text/'
    FILENAME_TEXT = 'data'
    EXTENSION_TEXT = '.txt'
    FILE_TYPE_TEXT = 'text'
    
    PATH_AUDIO = 'Audio/'
    FILENAME_AUDIO = 'sound'
    EXTENSION_AUDIO = '.mp3'
    FILE_TYPE_AUDIO = 'audio'
    
    PATH_ACCESSIBILITY = 'Accessibility/'
    EXTENSION_ACCESSIBILITY = '.mp3'
    FILE_TYPE_ACCESSIBILITY = 'audio'
       
    PATH_TEMP = 'Temp/'
    