# Liste des librairies importées
import smartcard.System as scardsys
import smartcard.util as scardutil
import smartcard.Exceptions as scardexcp
import mysql.connector
from pyfiglet import Figlet
from tabulate import tabulate
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
		# Tentative d'obtenir la liste des lecteurs de cartes à puce disponibles
		liste_readerCard = scardsys.readers()
		print (liste_readerCard)
	except scardexcp.Exceptions as e:
		 # Gestion des exceptions liées à la récupération de la liste des lecteurs
		print (e)
		return
	# Calcul de la taille de la liste des lecteurs
	taille_reader = len(liste_readerCard)
	print (taille_reader)
	
	# Vérification s'il y a au moins un lecteur de carte disponible
	if (taille_reader == 0):
		print ("Aucun lecteur de carte connecté")		
		exit()
	try:
		# Tentative d'établir une connexion avec le premier lecteur de carte de la liste
		global conn_reader
		conn_reader = liste_readerCard[0].createConnection()
		conn_reader.connect()
		# Affichage de l'ATR (Answer to Reset) de la carte à puce
		print ("ATR:", scardutil.toHexString(conn_reader.getATR()))
	except scardexcp.NoCardException as e:
		print ("Pas de carte dans le lecteur :", e)
		exit()
	return	 


# print_apdu
''' Fonction print_apdu permet juste d'afficher les APDU sous forme d'hexadécimal
de base, les APDU envoyés par python sont en décimal '''
def __print_apdu(apdu):
        for x in apdu:
            print("0x%02X" % x, end=' ')
        print("\n")  


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


def PINvalide():
	global PIN # Utilisation de la variable globale PIN pour stocker le code PIN saisi
	PIN = str(getpass.getpass("Saisir le code PIN : "))
	apdu = [0x81, 0x01, 0x00, 0x00] # Construction d'une commande APDU (Application Protocol Data Unit) pour envoyer au lecteur de carte
	data, sw1, sw2 = conn_reader.transmit(apdu) # Transmission de la commande APDU au lecteur de carte et récupération des données et des codes SW1 et SW2
	# Ajout de la valeur de SW2 à la commande APDU et retransmission pour obtenir la réponse complète
	apdu.append(sw2) 
	data, sw1, sw2 = conn_reader.transmit(apdu)
	# Utilisation de la variable globale pinConsult pour stocker la réponse du lecteur de carte
	global pinConsult
	pinConsult = ""
	# Conversion des données reçues en chaîne de caractères et stockage dans pinConsult
	for e in data:
	    pinConsult += chr(e)	


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
	print ("1 - Afficher mes informations")
	print ("2 - Consulter mes bonus ")
	print ("3 - Transférer mes bonus sur la carte")
	print ("4 - Consulter mon crédit disponible sur la carte")
	print ("5 - Recharger par carte bancaire")
	print ("6 - Afficher l'historique des transactions")
	print ("7 - Quitter")


def affiche_info():
	apdu = [0x80, 0x04, 0x00, 0x00, 0x01] # Construction d'une commande APDU pour récupérer des informations de la carte à puce
	data, sw1, sw2 = conn_reader.transmit(apdu) # Transmission de la commande APDU au lecteur de carte et récupération des données ainsi que des codes SW1 et SW2
	
	print ("sw1 : 0x%02X | sw2 : 0x%02X" % (sw1,sw2))
	apdu[4] = sw2 # Mise à jour de la dernière partie de la commande APDU avec la valeur de SW2
	data, sw1, sw2 = conn_reader.transmit(apdu) # Nouvelle transmission de la commande APDU modifiée pour obtenir la réponse complète du lecteur de carte
	infos = "" # Initialisation d'une chaîne de caractères pour stocker les informations extraites de la réponse
	# Conversion des données reçues en chaîne de caractères et stockage dans la variable infos
	for e in data:
		infos += chr(e)
	num_etudiant = int(infos.split()[-1]) # Extraction du numéro d'étudiant à partir des informations obtenues
	check_query = "SELECT COUNT(*) FROM Etudiant WHERE etu_num = %s;" # Vérification si le numéro d'étudiant existe déjà dans la base de données
	check_val = (num_etudiant,) 
	cursor = cnx.cursor() # Création d'un curseur pour interagir avec la base de données
	cursor.execute(check_query, check_val)# Exécution de la requête de vérification
	result = cursor.fetchone() # Récupération du résultat de la requête de vérification
	
	# Vérification si le numéro d'étudiant n'existe pas dans la base de données
	if result[0] < 0:
		print("Ce numéro d'étudiant n'existe pas allez voir l'agent administratif")
	else: 
		sql = "SELECT etu_num, etu_nom, etu_prenom FROM Etudiant WHERE etu_num = %s;" # Requête pour récupérer les informations de l'étudiant en fonction du numéro d'étudiant
		cursor.execute(sql, (num_etudiant,))
		student_info = cursor.fetchone() # Récupération des informations de l'étudiant
		print("Informations sur l'étudiant :", student_info) # Affichage des informations de l'étudiant
	return


def affiche_bonus():
	apdu = [0x80, 0x04, 0x00, 0x00, 0x01]
	data, sw1, sw2 = conn_reader.transmit(apdu)
	
	print ("sw1 : 0x%02X | sw2 : 0x%02X" % (sw1,sw2))
	apdu[4] = sw2
	data, sw1, sw2 = conn_reader.transmit(apdu)
	infos = ""
	for e in data:
		infos += chr(e)
	num_etudiant = int(infos.split()[-1])
	# print (type(num_etudiant))
	# Vérifiez si le numéro d'étudiant existe déjà
	check_query = "SELECT COUNT(*) FROM Etudiant WHERE etu_num = %s;"
	check_val = (num_etudiant,)
	cursor = cnx.cursor()
	cursor.execute(check_query, check_val)
	result = cursor.fetchone()
	if result[0] < 0:
		print("Ce numéro d'étudiant n'existe pas allez voir l'agent administratif")
	else: 
		sql = "SELECT etu_bonus FROM Etudiant WHERE etu_num = %s;" # Requête SQL pour sélectionner le bonus d'un étudiant spécifique en fonction de son numéro d'étudiant
		cursor.execute(sql, (num_etudiant,))
		student_info = cursor.fetchone()
		bonus_value = float(student_info[0]) # Extraction de la valeur du bonus de la première colonne du résultat (index 0)
		bonus_value = "{:.2f}".format(float(bonus_value) + 0.00) # Ajout d'une valeur fixe de bonus (0.00) à la valeur existante du bonus
		print("Vous avez :", bonus_value , " bonus \n") # Affichage du montant total du bonus de l'étudiant


def transfert_bonus():
	apdu = [0x80, 0x04, 0x00, 0x00, 0x01]
	data, sw1, sw2 = conn_reader.transmit(apdu)
	
	print ("sw1 : 0x%02X | sw2 : 0x%02X" % (sw1,sw2))
	apdu[4] = sw2
	data, sw1, sw2 = conn_reader.transmit(apdu)
	infos = ""
	for e in data:
		infos += chr(e)
	num_etudiant = int(infos.split()[-1])
	# print (type(num_etudiant))
	# Vérifiez si le numéro d'étudiant existe déjà
	check_query = "SELECT COUNT(*) FROM Etudiant WHERE etu_num = %s;"
	check_val = (num_etudiant,)
	cursor = cnx.cursor()
	cursor.execute(check_query, check_val)
	result = cursor.fetchone()
	if result[0] < 0:
		print("Ce numéro d'étudiant n'existe pas allez voir l'agent administratif")
	else: 
		sql = "SELECT etu_bonus FROM Etudiant WHERE etu_num = %s;"
		cursor.execute(sql, (num_etudiant,))
		student_info = cursor.fetchone()
		bonus_value = float(student_info[0])
		bonus_value = float(student_info[0])
		print("Vous avez :", bonus_value , " bonus \n")
		nb_bonus = float(input("Combien de bonus voulez-vous transférer ? ")) # Saisie du nombre de bonus à transférer
		if (nb_bonus <= bonus_value): # Vérification si le nombre de bonus à transférer est inférieur ou égal au bonus actuel de l'étudiant

			sql_ajout_solde = "UPDATE Etudiant SET etu_solde = etu_solde + %s WHERE etu_num = %s" # Requête SQL pour ajouter le montant transféré au solde de l'étudiant
			cursor.execute(sql_ajout_solde, (nb_bonus,num_etudiant))
			
			sql_enlever_bonus = "UPDATE Etudiant SET etu_bonus = etu_bonus - %s WHERE etu_num = %s" # Requête SQL pour enlever le montant transféré du bonus de l'étudiant
			cursor.execute(sql_enlever_bonus, (nb_bonus, num_etudiant))
			
			cnx.commit() # Validation des changements dans la base de données
			
			verif_bonus = "SELECT etu_bonus FROM Etudiant WHERE etu_num = %s;"
			cursor.execute(verif_bonus, (num_etudiant,))
			result_bonus = cursor.fetchone()
			verif_solde = "SELECT etu_solde FROM Etudiant WHERE etu_num = %s;"
			cursor.execute(verif_solde, (num_etudiant,))
			result_solde = cursor.fetchone()
			bonus_after_transfer = result_bonus[0]
			print ("Désormais il vous reste :", bonus_after_transfer, " bonus \n")
			solde_after_transfer = result_solde[0]
			solde_after_transfer_STR = str(solde_after_transfer)
			solde_after_transfer_STR = str(solde_after_transfer)  # Convertir le montant en chaîne
			apdu = [0x80, 0x08, 0x00, 0x00]
			length = len(solde_after_transfer_STR)
			apdu.append(length)
			__print_apdu(apdu)
#			 Ajouter chaque caractère de la chaîne à l'APDU
			for e in solde_after_transfer_STR:
				apdu.append(ord(e))
			print(apdu)
			transmit_apdu(apdu)
	return


def consult_sold():
	apdu = [0x80, 0x07, 0x00, 0x00, 0x00]
	data, sw1, sw2 = conn_reader.transmit(apdu)
	print("sw1 : 0x%02X | taille demandée : sw2 : 0x%02X" % (sw1, sw2))
    
	apdu[4] = sw2
	print ("l'APDU pour afficher les données de l'eeprom est :")
	__print_apdu(apdu)
	if (sw2 != 0x00):
		data, sw1, sw2 = conn_reader.transmit(apdu)
		data_str = ""
		str_sold = ""
		for e in data:
			str_sold += chr(e)
		print ("sw1 : 0x%02X | sw2 : 0x%02X | data : %s" % (sw1,sw2,str_sold))
		return
	else:
		print("l'EEPROM est vide, veuillez initialisez le solde")


def recharger_carte():
    apdu = [0x80, 0x04, 0x00, 0x00, 0x01]
    data, sw1, sw2 = conn_reader.transmit(apdu)
    print("sw1 : 0x%02X | sw2 : 0x%02X" % (sw1, sw2))
    apdu[4] = sw2
    data, sw1, sw2 = conn_reader.transmit(apdu)
    infos = ""
    for e in data:
        infos += chr(e)
    num_etudiant = int(infos.split()[-1])
    apdu = [0x80, 0x07, 0x00, 0x00, 0x00]
    data, sw1, sw2 = conn_reader.transmit(apdu)
    print("sw1 : 0x%02X | taille demandée : sw2 : 0x%02X" % (sw1, sw2))
    apdu[4] = sw2
    print("l'APDU pour afficher les données de l'eeprom est :")
    __print_apdu(apdu)
    if (sw2 != 0x00):
        data, sw1, sw2 = conn_reader.transmit(apdu)
        str_sold = ""
        for e in data:
            str_sold += chr(e)
        print("sw1 : 0x%02X | sw2 : 0x%02X | data : %s" % (sw1, sw2, str_sold))
    else:
        print("l'EEPROM est vide, veuillez initialisez le solde")
    str_sold = float(str_sold)
    # Requête pour récupérer le solde actuel de la base de données
    verif_solde_bdd = "SELECT etu_solde FROM Etudiant WHERE etu_num = %s;"
    cursor = cnx.cursor()
    cursor.execute(verif_solde_bdd, (num_etudiant,))
    result_solde_bdd = cursor.fetchone()
    solde_bdd = result_solde_bdd[0]
    if solde_bdd == str_sold:
        somme_recharge = float(input("De combien d'euros souhaitez-vous recharger la carte ?"))
        ajout_new_sold = somme_recharge + str_sold
        ajout_new_sold = "{:.2f}".format(float(ajout_new_sold) + 0.00)
        apdu = [0x80, 0x08, 0x00, 0x00]
        length = len(ajout_new_sold)
        apdu.append(length)
        __print_apdu(apdu)
        for e in ajout_new_sold:
            apdu.append(ord(e))
        print(apdu)
        transmit_apdu(apdu)
        # Mettre à jour le solde dans la base de données
        sql_ajout_solde = "UPDATE Etudiant SET etu_solde = etu_solde + %s WHERE etu_num = %s"
        cursor.execute(sql_ajout_solde, (somme_recharge, num_etudiant))
        cnx.commit()
        verif_solde_apres_recharge = "SELECT etu_solde FROM Etudiant WHERE etu_num = %s;"
        cursor.execute(verif_solde_apres_recharge, (num_etudiant,))
        result_solde = cursor.fetchone()
        solde_after_recharge = result_solde[0]
        solde_after_recharge_STR = str(solde_after_recharge)
        print("Le solde après la recharge est :", solde_after_recharge_STR)
    else:
        # Si les soldes ne sont pas les mêmes, mettre à jour le solde de la carte avec celui de la base de données
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


def histo_transac():
    apdu = [0x80, 0x04, 0x00, 0x00, 0x01]
    data, sw1, sw2 = conn_reader.transmit(apdu)

    print("sw1 : 0x%02X | sw2 : 0x%02X" % (sw1, sw2))

    apdu[4] = sw2
    data, sw1, sw2 = conn_reader.transmit(apdu)
    infos = ""
    for e in data:
        infos += chr(e)
    num_etudiant = int(infos.split()[-1])

    # Vérifiez si le numéro d'étudiant existe déjà
    check_query = "SELECT COUNT(*) FROM Etudiant WHERE etu_num = %s;"
    check_val = (num_etudiant,)

    cursor = cnx.cursor()
    cursor.execute(check_query, check_val)
    result = cursor.fetchone()

    if result[0] < 0:
        print("Ce numéro d'étudiant n'existe pas allez voir l'agent administratif")
    else:
        sql = "SELECT etu_num, opr_date, opr_montant, opr_libelle, type_opeartion FROM Compte WHERE etu_num = %s;"
        cursor.execute(sql, (num_etudiant,))
        histo_transac = cursor.fetchall()

        if histo_transac:
            headers = ["Numéro Étudiant", "Date", "Montant", "Libellé", "Type Opération"]
            print("Historique de transactions:")
            print(tabulate(histo_transac, headers=headers, tablefmt="grid"))
        else:
            print("Aucune transaction trouvée pour cet étudiant.")

    return


def main():
	init_smart_card()
	PINvalide()
	if PIN == pinConsult:
		while True:
			print_menu()
			cmd = int(input("Choix :"))
			if (cmd == 1):
				affiche_info()		
			elif (cmd == 2):
				affiche_bonus()
			elif (cmd == 3):
				transfert_bonus()
			elif (cmd == 4):
				consult_sold()
			elif (cmd == 5):
				recharger_carte()
			elif (cmd == 6):
				histo_transac()
			elif (cmd == 7):
				print("Au revoir !!")
				return
			else :
				print ("erreur, saisissez une commande valide")
				return
	else:
		print ("Code PIN incorrect")
		return
	print_menu()
if __name__ == '__main__':
	banner_text = "Berlicum"
	generated_banner = generate_banner(banner_text, font="slant")
	print(generated_banner)
	main()
