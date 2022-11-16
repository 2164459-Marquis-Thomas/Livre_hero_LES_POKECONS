import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
# Importer la classe Ui_MainWindow du fichier GUI.py
from GUI import Ui_MainWindow

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Gab",
  password="jouet",
  database="Livre_hero"
)


#Sert a remplir la liste de sauvegarde avec les noms des joueurs
def remplirListeSauvegarde(self):
    # remplir la liste des sauvegardes
    mycursor= mydb.cursor()
    mycursor.execute("SELECT CONVERT(id, char), decrypter(nom) FROM joueur_sauvegarde")
    monResultat = mycursor.fetchall()
    count= mycursor.rowcount
    #si il y a des sauvegardes on les affiche
    if count > 0:
        self.comboBoxSauvegarde.clear()
        for x in monResultat:
            #for y in x: 
            self.comboBoxSauvegarde.addItem(x[1], x[0])
    #Si aucune partie n'est sauvegarder
    else:
        self.comboBoxSauvegarde.addItem("Aucune partie sauvegarder")

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
            sql ="INSERT INTO joueur_sauvegarde (nom, chapitre_pogression) VALUES (crypter(""'"+nom+"'""), 0)"
            mycursor.execute(sql)
            mydb.commit()
            remplirListeSauvegarde(self)
            id = mycursor.lastrowid
            sql1 ="INSERT INTO fiche_personnage (player_id, endurance, habilite) VALUES (%s, %s, %s)"
            data = (id, 0, 0 )
            mycursor.execute(sql1, data)
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

    # Méthode qui selectionne les données sauvegarder pour chaque joueur. Donc le chapitre ou le joueur est rendu
    # sa fiche personnage etc. CECI EST ASSOCIÉ AU BOUTON "CHARGER"
    def selectPartieSauvegarde(self):
        self.plainTextEditArmes.clear()
        self.plainTextEditKai.clear()
        self.plainTextEditSac.clear()
        self.spinBoxEndu.clear()
        self.spinBoxHab.clear() 

        id = self.comboBoxSauvegarde.currentData()
        mycursor = mydb.cursor()

        sqlJoueur = "SELECT habilite, endurance, discipline_kai, arme, sac_a_dos FROM fiche_personnage WHERE player_id = " + id
        mycursor.execute(sqlJoueur)
        joueur = mycursor.fetchall()

        sqlChapitre = "SELECT CONVERT(chapitre_pogression, CHAR) FROM joueur_sauvegarde WHERE id = " + id
        mycursor.execute(sqlChapitre)
        chapitre = mycursor.fetchone()

        sql = "SELECT texte from chapitre where no_chapitre = %s"
        mycursor.execute(sql, chapitre)
        monResultat = mycursor.fetchall()

        texte = ""
        
        for x in monResultat:
            for y in x:
                texte = y
                self.labelTexte.setText(texte)

        for x in chapitre:
            self.labelChapitre.setText(x)

        if(joueur[0]!="None"):
            for x in joueur:
                self.plainTextEditArmes.setPlainText(x[3])
                self.plainTextEditKai.setPlainText(x[2])
                self.plainTextEditSac.setPlainText(x[4])
                self.spinBoxEndu.setValue(x[1])
                self.spinBoxHab.setValue(x[0])

    #Aussitôt que tu change de chapitre le update se lance dans la table de la sauvegarde du joueur 
    # CECI EST ASSOCIÉ AU BOUTON "PROCHAIN CHAPITRE"
    def updateChapitreJoueur(self):
        mycursor = mydb.cursor()
        id = self.comboBoxSauvegarde.currentData()
        chapitreUpdate = self.comboBox_2.currentText()
        sql = "UPDATE joueur_sauvegarde set chapitre_pogression = "+chapitreUpdate+" where id = " + id
        mycursor.execute(sql)
        mydb.commit()
        mycursor.execute("SELECT texte FROM chapitre WHERE no_chapitre = "+ chapitreUpdate)
        resultat = mycursor.fetchall()
        texte = ""
        for x in resultat:
            for y in x:
                texte = y
        self.labelTexte.setText(texte)
        self.labelChapitre.setText(chapitreUpdate)

    #Change le readonly de la fiche personnage pour que l'utilisateur soit capable d'éditer sa fiche
    #CECI EST ASSOCIÉ AU BOUTON "EDITER FICHE PERSONNAGE"
    def updateStats(self):
        self.plainTextEditArmes.setReadOnly(False)
        self.plainTextEditKai.setReadOnly(False)
        self.plainTextEditSac.setReadOnly(False)
        self.spinBoxEndu.setReadOnly(False)
        self.spinBoxHab.setReadOnly(False)

    #Enregistre les modifications qu'à apporter l'utilisateur à sa fiche
    #CECI EST ASSOCIÉ AU BOUTON "ENREGISTRER"
    def enregistrerStats(self):
        mycursor = mydb.cursor()
        id = self.comboBoxSauvegarde.currentData()
        habilite = self.spinBoxHab.value()
        endurance = self.spinBoxHab.value()
        kai = self.plainTextEditKai.toPlainText()
        arme = self.plainTextEditArmes.toPlainText()
        sac = self.plainTextEditSac.toPlainText()
        sql = "UPDATE fiche_personnage set habilite = %s, endurance = %s, discipline_kai = %s, arme = %s, sac_a_dos = %s WHERE player_id = %s"
        param = (habilite, endurance, kai, arme, sac, id)
        print(sql)
        mycursor.execute(sql, param)
        mydb.commit()
        self.plainTextEditArmes.setReadOnly(True)
        self.plainTextEditKai.setReadOnly(True)
        self.plainTextEditSac.setReadOnly(True)
        self.spinBoxEndu.setReadOnly(True)
        self.spinBoxHab.setReadOnly(True)

    #Charge les prochains chapitre selon le chapitre actuel de l'utilisateur
    #CECI EST ASSOCIÉ AU BOUTON "CHOIX CHAPITRE"
    def updateChapitre(self):
        mycursor = mydb.cursor()
        id = self.comboBoxSauvegarde.currentData()
        sql = "SELECT CONVERT(no_chapitre_destination, CHAR) From lien_chapitre  where no_chapitre_origine = %s"
        sqlChapitre = "SELECT chapitre_pogression From joueur_sauvegarde where id = %s"
        mycursor.execute(sqlChapitre, (id, ))
        resultat = mycursor.fetchone()
        for x in resultat:
            resultat = x
        if(resultat==0):
            resultat=1
        mycursor.execute(sql, (resultat, ))
        prochainChapitre = mycursor.fetchall()
        self.comboBox_2.clear()
        for x in prochainChapitre:
            for y in x:
                self.comboBox_2.addItem(y)
        
    #Supprime tout les données d'un uyilisateur dans la table de sauvegarde lorsqu'il est selectionner dans le combobox
    #CECI EST ASSOCIÉ AU BOUTON "SUPPRIMER"
    def supprimerSauvegarde(self):
        index = self.comboBoxSauvegarde.currentIndex()
        id = self.comboBoxSauvegarde.currentData()
        print(id)
        if(index >= 0):
            self.comboBoxSauvegarde.removeItem(index)
            mycursor = mydb.cursor()
            sql = "DELETE FROM joueur_sauvegarde WHERE id = " + id 
            mycursor.execute(sql)
            mydb.commit()
            
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
