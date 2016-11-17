from PyQt4.QtGui import *
from PyQt4.QtCore import *  # inclut QTimer..
import os,sys
from  Pyqt.QtDesigner import * # fichier obtenu a partir QtDesigner et pyuic4

# +/- variables et objets globaux

class myApp(QWidget, Ui_Form): # la classe recoit le Qwidget principal etla classe definie dans test.py obtenu avec pyuic4
        def __init__(self, parent=None):
                QWidget.__init__(self) # initialise le Qwidget principal
                self.setupUi(parent) # Obligatoire

                # --- Variables de classe

                # --- Parametrage des widgets de l'interface GUI si necessaire ---

                # --- Connexions entre signaux des widgets et fonctions
                # connecte chaque signal utilise des objets a l'appel de la fonction voulue

                self.connect(self.pushButtonOuvrirImage, SIGNAL("clicked()"), self.pushButtonOuvrirImageClicked)  # connecte le signal Clicked de l'objet a l'appel de la fonction voulue
                self.connect(self.pushButtonEnregistrerImage, SIGNAL("clicked()"), self.pushButtonEnregistrerImageClicked) # connecte le signal Clicked de l'objet bouton a l'appel de la fonction voulue
                self.connect(self.pushButtonNouveauImage, SIGNAL("clicked()"), self.pushButtonNouveauImageClicked) # connecte le signal Clicked de l'objet bouton a l'appel de la fonction voulue

                # --- Code actif initial  ---


                # Dessin avec QPixmap (affichage) et QImage (I/O, acces pixels)

                # creation d'un QImage permettant l'acces aux pixels
                self.image=QImage(self.labelImage.size(),QImage.Format_RGB32) # cree image RGB 32 bits meme taille que label

                #-- initialisation du QImage
                self.image.fill(QColor(255,255,255)) # fond blanc

                # coordonnees centre du QPixmap (meme taille que label)
                xo=self.image.width()/2
                yo=self.image.height()/2

                #trace le point
                #self.image.setPixel(xo,yo,qRgb(0,0,0)) # modifie la couleur du pixel x,y - noter qRgb renvoie valeur RGB 0xFFRRGGBB

                #--- dessin initial sur QImage --
                self.painterImage=QPainter(self.image) # associe QPainter (classe de dessin) au Qimage


                # trace de formes
                self.painterImage.setPen(QPen(QColor(0,0,255),2)) # fixe la couleur du crayon et la largeur pour le dessin
                self.painterImage.drawRect(10,10,50,50) # dessin rectangle : drawRect (self, int x, int y, int w, int h)
                #self.painterImage.drawPoint(xo,yo) # trace un point drawPoint (self, int x, int y)
                #self.painterImage.fillRect(150,150,30,30,QColor(255,255,0)) # fillRect (self, int x, int y, int w, int h, QColor b)
                self.painterImage.drawEllipse(xo,yo,50,50) # dessin cercle - x-y = coin sup gauche rect encadrant : drawEllipse (self, int x, int y, int w, int h)
                #self.painterImage.drawEllipse(QPointF(xo,yo),50,50) # dessin cercle avec x,y centre et rayon : drawEllipse (self, QPointF center, float rx, float ry)
                self.painterImage.drawLine(0,0,xo*2,yo) # trace une ligne : drawLine (self, int x1, int y1, int x2, int y2)
                #self.painterImage.drawText(QPointF(xo/2, yo/2), "Hello") # drawText (self, QPointF p, QString s)



                self.painterImage.end() # ferme le painter - n'est plus accessible apres

                # -- fin dessin sur QImage

                #-- Initialisation du QPixmap
                self.pixmap=QPixmap.fromImage(self.image) # initialise  le QPixmap...

                self.updatePixmap()

        # --- les fonctions appelees, utilisees par les signaux des widgets ---

        def pushButtonOuvrirImageClicked(self):
                #print("Bouton <Selectionner Fichier> appuye")

                # ouvre fichier en tenant compte du chemin deja saisi dans le champ
                if self.lineEditCheminImage.text()=="":
                        self.filename=QFileDialog.getOpenFileName(self, 'Ouvrir fichier', QDir.currentPath()) # ouvre l'interface fichier - chemin courant par defaut
                else:
                        info=QFileInfo(self.lineEditCheminImage.text()) # definit un objet pour manipuler info sur fichier a partir chaine champ
                        print info.absoluteFilePath() # debug
                        self.filenameImage=QFileDialog.getOpenFileName(self, 'Ouvrir fichier', info.absoluteFilePath()) # ouvre l'interface fichier - a partir chemin


                #self.filename=QFileDialog.getOpenFileName(self, 'Ouvrir fichier', QDir.currentPath()) # ouvre l'interface fichier - chemin courant par defaut
                # getOpenFileName ouvre le fichier sans l'effacer

                print(self.filenameImage) # affiche le chemin obtenu dans la console
                self.lineEditCheminImage.setText(self.filenameImage) # affiche le chemin obtenu dans le champ texte

                self.image.load(self.filenameImage)
                self.image=self.image.scaled(self.labelImage.size()) # redimensionne l'image
                self.updatePixmap() # met a jour le pixmap et qlabel


        def pushButtonNouveauImageClicked(self):
                #print("Bouton NOUVEAU appuye")

                # ouvre fichier en tenant compte du chemin deja saisi dans le champ
                if self.lineEditCheminImage.text()=="":

                        self.filename=QFileDialog.getOpenFileName(self, 'Ouvrir fichier', QDir.currentPath()) # ouvre l'interface fichier - chemin courant par defaut
                else:
                        info=QFileInfo(self.lineEditCheminImage.text()) # definit un objet pour manipuler info sur fichier a partir chaine champ
                        print info.absoluteFilePath() # debug
                        self.filenameImage=QFileDialog.getSaveFileName(self, 'Ouvrir fichier', info.absoluteFilePath(), "*.png *.jpg;; *.gif") # ouvre l'interface fichier - a partir chemin - avec selection

                print(self.filenameImage)
                self.lineEditCheminImage.setText(self.filenameImage)


        def pushButtonEnregistrerImageClicked(self):
                print("Bouton <ENREGISTRE> appuye")

                if self.lineEditCheminImage.text()!="":

                        self.image.save(self.filenameImage) # le suffixe utilise est celui du nom de fichier

        # --- les fonctions appelees, utilisees par les signaux hors widgets ---

        # --- fonctions de classes autres---

        # fonction de MAJ du QPixmap : chargement QImage +/- dessin + affichage dans QLabel
        def updatePixmap(self):

                # chargement du QImage dans le QPixmap
                self.pixmap.convertFromImage(self.image) # recharge le QImage dans le QPixmap existant - met a jour le QPixmap

                #-- affichage du QPixmap dans QLabel
                self.labelImage.setPixmap(self.pixmap) # met a jour le qpixmap affiche dans le qlabel

# -- Autres Classes utiles --

# -- Classe principale (lancement)  --
def main(args):
        a=QApplication(args) # cree l'objet application
        f=QWidget() # cree le QWidget racine
        c=myApp(f) # appelle la classe contenant le code de l'application
        f.show() # affiche la fenetre QWidget
        r=a.exec_() # lance l'execution de l'application
        return r

if __name__=="__main__": # pour rendre le code executable
        main(sys.argv) # appelle la fonction main
