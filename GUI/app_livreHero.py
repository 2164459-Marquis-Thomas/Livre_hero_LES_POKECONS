import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
# Importer la classe Ui_MainWindow du fichier GUI.py
from GUI import Ui_MainWindow

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql",
  database="Livre_hero"
)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # On va créer la fenêtre avec cette commande
        self.setupUi(self)
        # On connecter un événement sur le line edit

    # On défini la fonction qu'on avait déclaré pour le clique sur le bouton
    def insertionJoueur(self):
        mycursor = mydb.cursor()
        texte = self.texteChapitre.text()
        nom = self.lineEditNom.text()
        mycursor.execute("INSERT nom(), chapitre_progression(), point_de_vie(), combat(), endurance() INTO joueur_sauvegarde")
        
    
    def selectChapitre1(self):
        # ti select sur chapitre
        # afficher dans gros texte box
        pass

    def selectPartieSauvegarde(self):
        # Get la partie du joueur
        # Après ça select le texte du chapitre
        # affiche moe ça dans gros texte box
        pass
    
    def updateChapitreJoueur(self):
        # faire un update sur la table joueur_sauvegarde
        # avec le chapitre du joueur est rendu ou
        pass
    
    def updateStats(self):
        # update des stats dans la table joueur_sauvegarde
        pass

    def selectTexte(self):
        # juste un select pour afficher le texte du chapitre
        pass
    def selectChapitre(self):
        # un select du texte pour le prochain chapitre
        pass
    def updateChapitre(self):
        # update le chapitre la bien simple
        pass

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
