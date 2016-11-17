import sys
from PyQt4 import QtCore, QtGui


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(334, 323)
        self.labelImage = QtGui.QLabel(Form)
        self.labelImage.setGeometry(QtCore.QRect(5, 15, 320, 240))
        self.labelImage.setStyleSheet(_fromUtf8("background-color: rgb(180, 180, 180);"))
        self.labelImage.setText(_fromUtf8(""))
        self.labelImage.setObjectName(_fromUtf8("labelImage"))
        self.pushButtonNouveauImage = QtGui.QPushButton(Form)
        self.pushButtonNouveauImage.setGeometry(QtCore.QRect(5, 290, 86, 27))
        self.pushButtonNouveauImage.setObjectName(_fromUtf8("pushButtonNouveauImage"))
        self.pushButtonEnregistrerImage = QtGui.QPushButton(Form)
        self.pushButtonEnregistrerImage.setGeometry(QtCore.QRect(185, 290, 86, 27))
        self.pushButtonEnregistrerImage.setObjectName(_fromUtf8("pushButtonEnregistrerImage"))
        self.lineEditCheminImage = QtGui.QLineEdit(Form)
        self.lineEditCheminImage.setGeometry(QtCore.QRect(5, 262, 321, 26))
        self.lineEditCheminImage.setObjectName(_fromUtf8("lineEditCheminImage"))
        self.pushButtonOuvrirImage = QtGui.QPushButton(Form)
        self.pushButtonOuvrirImage.setGeometry(QtCore.QRect(95, 290, 85, 27))
        self.pushButtonOuvrirImage.setObjectName(_fromUtf8("pushButtonOuvrirImage"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Tomography Treatment", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonNouveauImage.setText(QtGui.QApplication.translate("Form", "Nouveau", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnregistrerImage.setText(QtGui.QApplication.translate("Form", "Enregistrer", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonOuvrirImage.setText(QtGui.QApplication.translate("Form", "Ouvrir", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
