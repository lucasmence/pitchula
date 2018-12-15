
import cmd
import const
import cv2
import os
import numpy

def fixImage():

    fileImage = ''
    fileExistsInput = False
    
    for extInput in const.All.EXTENSIONS_IMAGE:
            fileImage = const.All.PATH_IMAGE+const.All.FILENAME_IMAGE+extInput
            fileExistsInput = (os.path.isfile(fileImage))
            if (fileExistsInput):
                break
            
    if (fileExistsInput == False):
        print(colors.bashColors.FAIL+'Arquivo da imagem nao encontrado! Necessario capturar a foto novamente!'+colors.bashColors.ENDC)
        print(colors.bashColors.FAIL+'Digite "'+colors.bashColors.OKBLUE+cmd.All.CAMERA+colors.bashColors.FAIL+'"!')
        return
    
    #gradientImage(fileImage)
    #edgeImage(fileImage)
    grayscaleImage(fileImage)

def grayscaleImage(fileImage):
    print('Realizando ajustes e correcoes na imagem...')
    image = cv2.imread(fileImage)
    originalGamma = numpy.double(image)
    newGamma = originalGamma + 30
    image = numpy.uint8(newGamma)
    
    imageGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    (thresh, im_bw) = cv2.threshold(imageGray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    thresh = 127
    im_bw = cv2.threshold(imageGray, thresh, 255, cv2.THRESH_BINARY)[1]
    
    if (os.path.isfile(fileImage)):
        os.remove(fileImage)
        
    cv2.imwrite(fileImage,im_bw)
    print('Tratamento da imagem concluido!')
    
def edgeImage(fileImage):

    img = cv2.imread(fileImage,0)
    edges = cv2.Canny(img,100,300)

    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    
    plt.show()

def gradientImage(fileImage):
    img = cv2.imread(fileImage,0)

    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

    plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

    plt.show()
    
def sliceImage():
    
    fileImage = ''
    fileExistsInput = False
    
    for extInput in const.All.EXTENSIONS_IMAGE:
            fileImage = const.All.PATH_IMAGE+const.All.FILENAME_IMAGE+extInput
            fileExistsInput = (os.path.isfile(fileImage))
            if (fileExistsInput):
                break
            
    if (fileExistsInput == False):
        print(colors.bashColors.FAIL+'Arquivo da imagem nao encontrado! Necessario capturar a foto novamente!'+colors.bashColors.ENDC)
        print(colors.bashColors.FAIL+'Digite "'+colors.bashColors.OKBLUE+cmd.All.CAMERA+colors.bashColors.FAIL+'"!')
        return
    
   # CROP_HEIGHT_RANGE = 200
    
    img = cv2.imread(fileImage)
    height = numpy.size(img, 0)
    width = numpy.size(img, 1)
    
    CROP_HEIGHT_RANGE = height 
    
    cropTimes = height // CROP_HEIGHT_RANGE #div
    imgHeightStart = 1
    
    for x in range(0, cropTimes):
        imgHeightCurrentLimit = imgHeightStart+CROP_HEIGHT_RANGE
        
        if (imgHeightCurrentLimit > height):
            imgHeightCurrentLimit =  height
        
        imageCropFilename = const.All.PATH_IMAGE_CROPPED + str(x)+'_'+ const.All.FILENAME_IMAGE_CROPPED + const.All.EXTENSION_IMAGE_CROPPED
        croppedImg = img[imgHeightStart:imgHeightCurrentLimit, 1:width]
        cv2.imwrite(imageCropFilename,croppedImg)
        imgHeightStart = imgHeightCurrentLimit
    
    return cropTimes
    
    
    
