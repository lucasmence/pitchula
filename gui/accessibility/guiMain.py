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
        lblStatusDescription.move(80,60)
        lblStatusDescription.setStyleSheet('font-size: 20px; color: yellow')
        lblStatusDescription.adjustSize()
        
        lblStatus = QLabel('Ativado', self)
        lblStatus.move(215,60)
        lblStatus.setStyleSheet('font-size: 20px; color: pink')
        lblStatus.adjustSize()    

        btnExit = QPushButton('Sair', self)
        btnExit.move(100,180)
        btnExit.setFixedWidth(120)
        btnExit.setFixedHeight(40)
        btnExit.setStyleSheet('font-size: 30px; color: white; background-color: red')

        btnConfig = QPushButton('Configurações', self)
        btnConfig.move(50,130)
        btnConfig.setFixedWidth(220)
        btnConfig.setFixedHeight(40)
        btnConfig.setStyleSheet('font-size: 30px; color: white; background-color: orange')

        lblInfo = QLabel('Lucas Silva - UniSALESIANO Aracatuba - SP - lucas21021996@gmail.com', self)
        lblInfo.move(6,222)
        lblInfo.setStyleSheet('font-size: 9px; color: white')
        lblInfo.adjustSize()
        
        #criando as acoes
        @pyqtSlot()
        def on_btnExitClick():
            self.close()
            
        btnExit.clicked.connect(on_btnExitClick)
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = WindowHome()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
