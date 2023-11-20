# Liste des librairies importées
import smartcard.System as scardsys
import smartcard.util as scardutil
import smartcard.Exceptions as scardexcp
import mysql.connector
from datetime import datetime
from pyfiglet import Figlet
import getpass

# Connexion à la base de données
cnx = mysql.connector.connect(user='root',
password ='root',
host='localhost',
database= 'purpledragon1')


# init_smart_card
''' Fonction init_smart_card qui permet d'initialiser la connexion avec la carte à puce
On vérifie si un lecteur de carte est connecté
On vérifie si il y a une carte dans le lecteur '''
def init_smart_card():
	try:
		liste_readerCard = scardsys.readers()
		print (liste_readerCard)
	except scardexcp.Exceptions as e:
		print (e)
		return

	taille_reader = len(liste_readerCard)
	print (taille_reader)
	if (taille_reader == 0):
		print ("Aucun lecteur de carte connecté")		
		exit()
	try:
		global conn_reader
		conn_reader = liste_readerCard[0].createConnection()
		conn_reader.connect()
		print ("ATR:", scardutil.toHexString(conn_reader.getATR()))
	except scardexcp.NoCardException as e:
		print ("Pas de carte dans le lecteur :", e)
		exit()
	return	 

# transmit_apdu
''' Fonction transmit_apdu qui permet d'envoyer l'APDU vers la mémoire flash de la carte
Récupération des codes d'erreurs sw1 et sw2 '''
def transmit_apdu(apdu):
    try:
        data, sw1, sw2 = conn_reader.transmit(apdu)
        return data, sw1, sw2
    except scardexcp.CardConnectionException as e:
        print("Error", e)
        return None, None, None

# print_apdu
''' Fonction print_apdu permet juste d'afficher les APDU sous forme d'hexadécimal
de base, les APDU envoyés par python sont en décimal '''
def __print_apdu(apdu):
        for x in apdu:
            print("0x%02X" % x, end=' ')
        print("\n")  

# generate_banner
''' Fonction generate_banner qui permet de générer une bannière stylisée
à l'aide de la librairie pyfiglet '''
def generate_banner(text, font="standard"):
    f = Figlet(font=font)
    banner = f.renderText(text)
    return banner

# print_menu
''' Fonction d'affichage du menu de l'appli '''
def print_menu():
	print ("1 - Afficher le solde")
	print ("2 - Acheter une boisson à 0.20c")
	print ("3 - Quitter")

# PINvalide
''' Fonction PINvalide qui permet de demander à l'utilisateur de rentrer son code PIN '''
def PINvalide():
	global PIN
	PIN = str(getpass.getpass("Saisir le code PIN : "))
	apdu = [0x81, 0x01, 0x00, 0x00]
	data, sw1, sw2 = conn_reader.transmit(apdu)
	apdu.append(sw2)
	data, sw1, sw2 = conn_reader.transmit(apdu)
	global pinConsult
	pinConsult = ""
	for e in data:
	    pinConsult += chr(e)	


# consult_sold
''' Fonction consult_sold qui permet de lire le solde de la carte 
(à partir de l'APDU 0x80, 0x07 0x00, 0x00 qui appelle la fonction C lire_perso) '''
def consult_sold():
	apdu = [0x80, 0x07, 0x00, 0x00]
	data, sw1, sw2 = conn_reader.transmit(apdu)
	# print("sw1 : 0x%02X | taille demandée : sw2 : 0x%02X" % (sw1, sw2))
    
	apdu.append(sw2)
	# print ("l'APDU pour afficher les données de l'eeprom est :")
	__print_apdu(apdu)

	data, sw1, sw2 = conn_reader.transmit(apdu)
	str = ""
	for e in data:
			str += chr(e)
	# print ("sw1 : 0x%02X | sw2 : 0x%02X | Les données sur l'eeprom sont : %s" % (sw1,sw2,str))ù
	print(str)
	return str


# debit_sold
''' Fonction debit_sold qui permet à l'utilisateur de simuler l'achat d'une boisson
soit un café, soit un thé, soit un chocolat à 0.20c et d'effectuer l'opération de 
transaction qui débite la carte ET la BDD de 0.20c. 
Cette fonction permet aussi de vérifier que le solde de la base de données est le
même que celui de la carte sinon il prend le solde de la BDD (sécurité pour éviter que
un utilisateur augmente le solde de sa carte tout seul avec l'APDU sans MDP 0x80, 0x04, 0x00, 0x00, 0x01 )'''
def debit_sold():

	# envoi de l'APDU pour lire les informations Nom, Prenom et Num Etu de la carte
	apdu = [0x80, 0x04, 0x00, 0x00, 0x01]
	data, sw1, sw2 = conn_reader.transmit(apdu)

	print("sw1 : 0x%02X | sw2 : 0x%02X" % (sw1, sw2))

	apdu[4] = sw2
	data, sw1, sw2 = conn_reader.transmit(apdu)
	infos = ""
	for e in data:
		infos += chr(e)
	num_etudiant = int(infos.split()[-1])

	# Définition des variables
	date_actuelle = datetime.now()
	libelle_cafe = "Cafe"
	libelle_chocolat = "Chocolat"
	libelle_the = "Thé"
	type_ope = "Dépense"
	ope_montant = "-0.20"
	ope_montant_float = -0.20

	# Vérifier si le numéro d'étudiant existe déjà
	check_query = "SELECT COUNT(*) FROM Etudiant WHERE etu_num = %s;"
	check_val = (num_etudiant,)
	cursor = cnx.cursor()
	cursor.execute(check_query, check_val)
	result = cursor.fetchone()

	# envoi de l'APDU pour récupérer le solde de la carte
	apdu = [0x80, 0x07, 0x00, 0x00]
	data, sw1, sw2 = conn_reader.transmit(apdu)
	apdu.append(sw2)
	data, sw1, sw2 = conn_reader.transmit(apdu)
	result_str = ""
	for e in data:
			result_str += chr(e)
	result_str = float(result_str)  # Conversion en float
	result_str = "{:.2f}".format(float(result_str) + 0.00) # Mise en forme de float avec deux 0 après la virgule
	result_str = float(result_str)



	# Requête pour récupérer le solde actuel de la base de données
	verif_solde_bdd = "SELECT etu_solde FROM Etudiant WHERE etu_num = %s;"
	cursor = cnx.cursor()
	cursor.execute(verif_solde_bdd, (num_etudiant,))
	result_solde_bdd = cursor.fetchone()
	solde_bdd = result_solde_bdd[0]

	# Extraction du solde de l'étudiant depuis la base de données
	sql = "SELECT etu_solde FROM Etudiant WHERE etu_num = %s;"
	cursor.execute(sql, (num_etudiant,))
	student_info = cursor.fetchone()
	#Conversion en float et mise en forme .00
	solde_value = float(student_info[0])
	solde_value = "{:.2f}".format(float(solde_value) + 0.00)
	solde_value2 = float(solde_value)


	# Si le solde de la BDD est égal au solde de la carte :
	if (result_str == solde_value2):


		choix_produit = int(input("Choix du produit (1: Café, 2: Chocolat, 3: Thé): "))


		if (result_str < 0.20):
			print("Pas assez de crédit, veuillez recharger")
		else:
			result_str -= 0.20

			if choix_produit == 1:
				libelle_produit = libelle_cafe
			elif choix_produit == 2:
				libelle_produit = libelle_chocolat
			elif choix_produit == 3:
				libelle_produit = libelle_the

			requete_operation = "UPDATE Etudiant SET etu_solde = %s WHERE etu_num = %s"
			cursor.execute(requete_operation,(result_str,num_etudiant))

			requete_cafe = "INSERT INTO Compte (etu_num, opr_date, opr_montant, opr_libelle, type_opeartion) VALUES (%s, %s, %s, %s, %s)"
			cursor.execute(requete_operation,(result_str,num_etudiant))
			var = (num_etudiant, date_actuelle, ope_montant_float, libelle_produit, type_ope)
			cursor.execute(requete_cafe,var)
			cnx.commit()


			solde_value2 -= 0.20
			solde_value2_str = "{:.2f}".format(solde_value2)
			apdu2 = [0x80, 0x08, 0x00, 0x00]
			length = len(solde_value2_str)
			apdu2.append(length)
			print (apdu2)
			__print_apdu(apdu2)

			for e in solde_value2_str:
				apdu2.append(ord(e))
			print (apdu2)
			try:
				data, sw1, sw2 = conn_reader.transmit(apdu2)
				print ("sw1 : 0x%02X | sw2 : 0x%02X" % (sw1,sw2))
			except scardexcp.CardConnectionException as e:
				print ("Error", e)
				return
	
	else:
		# Si les soldes ne sont pas les mêmes, mettre à jour le solde de la carte avec celui de la base de données
		# envoi de l'APDU pour modifier le solde de la carte
		apdu = [0x80, 0x08, 0x00, 0x00]

		length = len(str(solde_bdd))
		apdu.append(length)
		__print_apdu(apdu)

		for e in str(solde_bdd):
		    apdu.append(ord(e))
		print(apdu)

		transmit_apdu(apdu)

		print("Le solde de la carte a été mis à jour avec le solde de la base de données.")

	return



# main
''' Appel des fonctions définies ci-dessus'''
def main():
	init_smart_card()
	PINvalide()
	if PIN == pinConsult:
		while True:
			print_menu()
			cmd = int(input("Choix :"))
			if (cmd == 1):
				consult_sold()		
			elif (cmd == 2):
				debit_sold()
			elif (cmd == 3):
				return
			else:
				print ("erreur, saisissez une commande valide")
	else :
		print ("Code PIN incorrect")
		return
	print_menu()


if __name__ == '__main__':
	banner_text = "Kuroda"
	generated_banner = generate_banner(banner_text, font="slant")
	print(generated_banner)
	main()