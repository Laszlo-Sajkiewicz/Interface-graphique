# add package
import sys
from PyQt4.QtGui import QApplication, QWidget

class Fenetre(QWidget):
    def __init__(self):
        # create window
        QWidget.__init__(self)
        self.setWindowTitle("Tomography Treatment")
        self.show()
    def mousePressEvent(self,event):
        # mouse event
        print("click")

app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)
fen = Fenetre()
app.exec_()
