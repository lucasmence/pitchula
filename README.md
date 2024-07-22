[![Code Quality](https://scrutinizer-ci.com/g/lucasmence/pitchula-photoreader/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/lucasmence/pitchula-photoreader/?branch=master) ![ ](https://scrutinizer-ci.com/g/lucasmence/pitchula-photoreader/badges/build.png?b=master)

# ![ ](./data/image/logo-eye-32-32.png) **Pitchula Text Photoreader**

Current version: **1.0.2**

Convert any image-text into audio with a single command line, e. g.: 
> python pitchula.py input.jpg output.mp3

# Languages

The project has avaiable these four languages right now!

![ ](./data/image/flag-united-states-32-32.png) ![ ](./data/image/flag-spain-32-32.png) ![ ](./data/image/flag-brazil-32-32.png) ![ ](./data/image/flag-france-32-32.png)

# How to install

- Clone the project directory using **git clone** command:
> git clone https://github.com/lucasmence/pitchula-photoreader/

- Install the **OpenCV** library for python using the command below:
> pip install opencv-python

- Install the **Pillow** library using the command below:
> pip install Pillow

- Install the **python-setuptools** using the command below:
>  sudo apt install python-setuptools

- Install the **Tesseract-OCR** libraries to continue, just copy the commands below:
> sudo apt install tesseract-ocr

> sudo apt install libtesseract-dev

- Install the **Tesseract for python** library using the command below:
> pip install pytesseract

- Install the spellcheck libraries, **enchant** and **pyenchant**, just use the commands below:
> sudo apt install enchant

> pip install pyenchant

- Install the text-to-speech API library the **gTTS** by using the command below:
> pip install gTTS

Okay, now you're ready to use this tool!

# Extensions

Input image types suported: **JPG** and **PNG**

Output audio type suported: **MP3**

# Credits

**[OpenCV for Python library](https://github.com/skvark/opencv-python)**

**[Pillow library](https://github.com/python-pillow/Pillow/)**

**[python-setuptools](https://github.com/pypa/setuptools)**

**[Tesseract-OCR library](https://github.com/tesseract-ocr/tesseract)**

**[pytesseract library](https://github.com/madmaze/pytesseract)** 

**[pyenchant library](https://github.com/rfk/pyenchant)** 

**[Google Text-to-Speech](https://github.com/pndurette/gTTS)** 

**Icons**
<div>Project logo icon and country flags made by <a href="https://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" 			    title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" 			    title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>

# version-log
 
 01/28/2019: Released the version 1.0.2

    > Object instance otimization for a better performance;

    > Fixed languagePath definition bug;

    > Updated the languages JSON files w/ new repository environment;
    

 01/27/2019: Released the version 1.0.1

    > Removed unused lines;

    > Updated all the project files to use OOP;

    > Replaced the run.py file to pitchula.py to test the project;

    > Use the Reader class on reader.py file to use the project functions inside of your own project;
    

 12/23/2018: Released the version 1.0.0

#

> Last update: July, 22 of 2024.
