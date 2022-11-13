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
def convertTuple(tup):
    pass

#Sert a remplir la liste de sauvegarde avec les noms des joueurs
def remplirListeSauvegarde(self):
    # remplir la liste des sauvegardes
    mycursor= mydb.cursor()
    mycursor.execute("SELECT decrypter(nom) FROM joueur_sauvegarde")
    monResultat = mycursor.fetchall()
    count= mycursor.rowcount
    texte = ""
    #si il y a des sauvegardes on les affiche
    if count > 0:
        self.listSauvegarde.clear()
        for x in monResultat:
            for y in x:
                texte = y
                self.listSauvegarde.addItem(texte)
    #Si aucune partie n'est sauvegarder
    else:
        self.listSauvegarde.addItem("Aucune partie sauvegarder")

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # On va créer la fenêtre avec cette commande
        self.setupUi(self)
        
        remplirListeSauvegarde(self)
        

    # insertion du joueur dans la BD
    #Encrypte le nom du joueur
    def insertionJoueur(self):
        mycursor = mydb.cursor()
        nom = self.lineEditNom.text()
        if nom !="":
            sql ="INSERT INTO joueur_sauvegarde (nom, chapitre_pogression, point_de_vie, combat, endurance) VALUES (crypter(""'"+nom+"'""), 0, 100, 0, 0)"
            print(sql)
            mycursor.execute(sql)
            mydb.commit()
            print(mycursor.rowcount, "record inserted")
            remplirListeSauvegarde(self)
        else:
            print("Veuillez entrer un nom")
    
    # Select du premier chapitre du livre
    def selectChapitre1(self):
        mycursor= mydb.cursor()
        mycursor.execute("SELECT texte FROM chapitre WHERE no_chapitre = 0")
        chapitre = 'Avertir le roi'
        monResultat = mycursor.fetchall()
        texte = ""
        for x in monResultat:
            for y in x:
                texte = y
        self.labelTexte.setText(texte)
        self.labelChapitre.setText(chapitre)

    
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
        mycursor = mydb.cursor()
        sql = "SELECT CONVERT(no_chapitre_destination, CHAR) from lien_chapitre inner join chapitre on no_chapitre_origine = no_chapitre where no_chapitre_origine = %s"
        self.lineEditNom.setText(self.listSauvegarde.selectedItems)
        #chapitre_actuel = 
        mycursor.execute(sql)
        resultat = mycursor.fetchall()
        for x in resultat:
            for y in x:
                self.listChapitre.addItem(y)
        pass

    def supprimerSauvegarde(self):
        item = self.listSauvegarde.currentRow()
        if(item >= 0):
            self.listSauvegarde.takeItem(item)
            mycursor= mydb.cursor()
            print(item)
            #mycursor.execute("DELETE FROM joueur_sauvegarde WHERE nom = ")
        

   

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
