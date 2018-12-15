
import os
import cmd
import const

def speech():
    print(colors.bashColors.WARNING+'Reproduzindo audio...'+colors.bashColors.ENDC)
    
    file = const.All.PATH_AUDIO + const.All.FILENAME_AUDIO + const.All.EXTENSION_AUDIO
    
    if (os.path.isfile(file) == False):
        print(colors.bashColors.FAIL+'Audio nao encontrado! Digite "'+colors.bashColors.OKBLUE+cmd.All.TTS+colors.bashColors.FAIL+'" para converter o texto local em audio!'+colors.bashColors.ENDC)
     
    os.system("mpg321 -q "+file)
    
    return
    



