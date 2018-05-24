#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, QtWidgets

#reload(sys)
#sys.setdefaultencoding('utf-8')

class WindowHome(QtWidgets.QMainWindow):
         
    def __init__(self, parent=None):
        #criando nossa janela
        
        super(WindowHome, self).__init__(parent)
        self.setWindowTitle('Processamento Digital de Imagens')
        self.resize(320,240)
        self.setStyleSheet('background-color: purple')
        
        btnLayout = QPushButton('',self)
        btnLayout.move(0,0)
        btnLayout.setFixedWidth(320)
        btnLayout.setFixedHeight(240)
        btnLayout.setStyleSheet('border: 5px solid white')
        
        lblTitle = QLabel('Miracle Reader', self)
        lblTitle.move(80,10)
        lblTitle.setStyleSheet('font-size: 20px; color: white')
        lblTitle.adjustSize()

        lblVersion = QLabel('versão 2018.5', self)
        lblVersion.move(80,30)
        lblVersion.setStyleSheet('font-size: 15px; font-style: italic; color: white')
        lblVersion.adjustSize()

        lblStatusDescription = QLabel('Acessibilidade:', self)
        lblStatusDescription.move(40,60)
        lblStatusDescription.setStyleSheet('font-size: 20px; color: yellow')
        lblStatusDescription.adjustSize()
        
        lblModeStatus = QLabel('Ativado', self)
        lblModeStatus.move(175,60)
        lblModeStatus.setStyleSheet('font-size: 20px; color: pink')
        lblModeStatus.adjustSize()    

        btnImageBorder = QPushButton('',self)
        btnImageBorder.move(120,100)
        btnImageBorder.setFixedWidth(64)
        btnImageBorder.setFixedHeight(64)
        btnImageBorder.setStyleSheet('border: 1px solid white')

        statusList = ('Modo de Captura de Câmera'
                     ,'Capturando imagem...'
                     ,'Tratamento de imagem...'
                     ,'Leitura OCR: Bloco 1/n'
                     ,'Ortografia: Bloco 1/n'
                     ,'Geração de audio: Bloco 1/n'
                     ,'Lendo o bloco 1/n da folha'
                     ,'Opções de finalização'
                     ,'Guia de Ajuda')

        lblCurrentStatus = QLabel(statusList[0], self)
        lblCurrentStatus.move(30,180)
        lblCurrentStatus.setStyleSheet('font-size: 20px; color: pink')
        lblCurrentStatus.adjustSize()    

        lblInfo = QLabel('Lucas Silva - UniSALESIANO Aracatuba - SP - lucas21021996@gmail.com', self)
        lblInfo.move(6,222)
        lblInfo.setStyleSheet('font-size: 9px; color: white')
        lblInfo.adjustSize()
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = WindowHome()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
