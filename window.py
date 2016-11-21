import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QAction , qApp
import skimage
from skimage import io , data
import os
from PIL.Image import *


class Window(QMainWindow):

    def __init__(self):
        super(Window,self).__init__()

        self.initUI()


    def initUI(self):
        # shortcut
        exitAction = QAction('&Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Close the app')
        exitAction.triggered.connect(qApp.exit)
        # end of shorcut
        
        #menu bar
        menu = self.menuBar()
        FileMenu=menu.addMenu('&File')
        FileMenu.addAction(exitAction)
        
        # end menu bar
        
        # button and position
        loadImageBtn = QPushButton("Load Image", self) # button 1
        loadImageBtn.move(30, 50) 

        SaveImageBtn = QPushButton("Save Image", self) # buttun 2
        SaveImageBtn.move(150, 50)
        # end button and position
        
        # connect + cliked
        loadImageBtn.clicked.connect(self.buttonClicked)
        SaveImageBtn.clicked.connect(self.buttonClicked)
        # end connect + cliked
        
        # status bar
        self.statusBar()
        # end status bar
        
        # window
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Tomography Treatment')
        self.show()
        # end window


    def buttonClicked(self): # method button

        sender = self.sender()
        #display
 
        im = open("sauver.jpg")
        Image.show(im)
        self.statusBar().showMessage(sender.text() + ' was pressed')
        
        # add function load image
        # add function Save image

if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())
