import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication)
"""from skimage import io
"""


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

        self.initUI()


    def initUI(self):

        loadImageBtn = QPushButton("Load Image")
        SaveImageBtn = QPushButton("Save")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(loadImageBtn) # add button
        hbox.addWidget(SaveImageBtn) # add button

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Tomography Treatment')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = Window()
    sys.exit(app.exec_())
