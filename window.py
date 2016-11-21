
import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
import skimage
from skimage import io , data
import os


class Window(QMainWindow):

    def __init__(self):
        super(Window,self).__init__()

        self.initUI()


    def initUI(self):

        loadImageBtn = QPushButton("Load Image", self) 
        loadImageBtn.move(30, 50)

        SaveImageBtn = QPushButton("Save Image", self)
        SaveImageBtn.move(150, 50)

        loadImageBtn.clicked.connect(self.buttonClicked)
        SaveImageBtn.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Tomography Treatment')
        self.show()


    def buttonClicked(self):

        sender = self.sender()
        #test image chargee
        im = io.imread('sauver.jpg')
        self.statusBar().showMessage(sender.text() + ' was pressed')
        
        # add function load image
        # add function Save image

if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())
