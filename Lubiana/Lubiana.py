# Liste des librairies importées
import smartcard.System as scardsys
import smartcard.util as scardutil
import smartcard.Exceptions as scardexcp
import random
from pyfiglet import Figlet
import getpass
import struct


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


# generate_banner
''' Fonction generate_banner qui permet de générer une bannière stylisée
à l'aide de la librairie pyfiglet '''
def generate_banner(text, font="standard"):
    f = Figlet(font=font)
    banner = f.renderText(text)
    return banner


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
        print("Sent APDU:", [hex(x) for x in apdu])  # Ajout de cet affichage
        print("Raw response: sw1 = 0x%02X, sw2 = 0x%02X" % (sw1, sw2))
        return data, sw1, sw2
    except scardexcp.CardConnectionException as e:
        print("Error", e)
        return data, sw1, sw2


def password_adm():
    user_password = getpass.getpass("Saisir le mot de passe : ")

    apdu = [0x80, 0x01, 0x00, 0x00]

    length = len(user_password)
    apdu.append(length)
    # __print_apdu(apdu)

    for e in user_password:
        apdu.append(ord(e))

    data, sw1, sw2 = transmit_apdu(apdu)

    if sw1 == 0x90:
        return True  # Mot de passe administrateur correct
    elif sw1 == 0xA0:
        print("Mot de passe non entré (code d'erreur personnalisé). \n")
        return False
    else:
        print("Mot de passe administrateur incorrect. \n")
        return False

# print_menu
''' Fonction d'affichage du menu de l'appli '''
def print_menu():
	print ("1 - Afficher la version de carte")
	print ("2 - Afficher les données de la carte")
	print ("3 - Attribuer la carte")
	print ("4 - Mettre le solde initial")
	print ("5 - Consulter le solde")
	print ("6 - Réinitialiser les données de la carte")
	print ("7 - Attribuer code PIN/PUK")
	print ("8 - Consulter le code PUK")
	print ("9 - Modifier le code PIN")
	print ("10 - Quitter")

# print_version 
''' Fonction pour afficher la version écrite dans la mémoire flash 
avec gestion des erreurs associées'''
def print_version():
	apdu = [0x80, 0x00, 0x00, 0x00, 0x04]
	try:
		data, sw1, sw2 = conn_reader.transmit(apdu)
	except scardexcp.Exceptions as e:
		print("Error", e)
		return
	if(sw1 != 0x90 and sw2 != 0x00):
		print ("sw1 : 0x%02X | sw2 : 0x%02X | version : erreur de lecture version" % (sw1,sw2))
	str = ""
	for e in data:
		str += chr(e)
	print ("sw1 : 0x%02X | sw2 : 0x%02X | version %s" % (sw1,sw2,str))
	return

# print_data
''' Fonction pour afficher les données écrites sur la carte sur les 32 premiers bits
de l'EEPROM avec gestion des erreurs associées'''
def print_data():

	apdu = [0x80, 0x04, 0x00, 0x00, 0x04]
	data, sw1, sw2 = conn_reader.transmit(apdu)
	
	print ("sw1 : 0x%02X | sw2 : 0x%02X" % (sw1,sw2))

	apdu[4] = sw2
	__print_apdu(apdu)

	if (sw2 != 0x00):
		data, sw1, sw2 = conn_reader.transmit(apdu)
		str_data = ""
		for e in data:
			str_data += chr(e)
		student_info = str_data.split()
		if len(student_info) == 3:
			print("\nNom de l'étudiant :", student_info[1])
			print("Prénom de l'étudiant :", student_info[0])
			print("Numéro de l'étudiant :", student_info[2])
			print("\n")
		else:
			print("erreur de taille de données")
		# print ("sw1 : 0x%02X | sw2 : 0x%02X | data : %s" % (sw1,sw2,str))
		return
	else:
		print("l'EEPROM est vide, veuillez attribuer la carte")

def assign_card():
    if not password_adm():
        return

    apdu = [0x80, 0x03, 0x00, 0x00]

    prenom = str(input("Saisir le prénom : "))
    nom = str(input("Saisir le nom : "))
    numero_etudiant = str(input("Saisir le numéro étudiant : "))

    infos = prenom + " " + nom + " " + numero_etudiant
    length = len(infos)

    apdu.append(length)
    apdu.extend(map(ord, infos))

    print("Données envoyées vers le programme C:")
    print("APDU :", [hex(x) for x in apdu])

    transmit_apdu(apdu)

def init_sold():
		
    print("Mot de passe administrateur correct. Initialisation du solde en cours...")

    apdu = [0x80, 0x08, 0x00, 0x00]

    # Solde initial (00000.00)
    solde = "00000.00"
    length = len(solde)

    apdu.append(length)  

    for char in solde:
        apdu.append(ord(char))

    print("APDU pour l'initialisation du solde :")
    __print_apdu(apdu)

    data, sw1, sw2 = conn_reader.transmit(apdu)

    if sw1 == 0x90:
        print("Initialisation du solde réussie.")
    else:
        print(f"Échec de l'initialisation du solde. SW1: 0x{sw1:02X}, SW2: 0x{sw2:02X}")


# consult_sold
''' Fonction pour afficher les données écrites sur la carte sur les entre le 32ème bit et
le 36ème bit (la ou est ecrit le solde) de l'EEPROM avec gestion des erreurs associées'''
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
		str = ""
		for e in data:
			str += chr(e)
		print ("sw1 : 0x%02X | sw2 : 0x%02X | data : %s" % (sw1,sw2,str))
		return
	else:
		print("l'EEPROM est vide, veuillez initialisez le solde")


def delete_data():

	if not password_adm():
		return

	apdu = [0x80, 0x05, 0x00, 0x00]
	data, sw1, sw2 = conn_reader.transmit(apdu)
	
	print ("sw1 : 0x%02X | sw2 : 0x%02X" % (sw1,sw2))

	apdu.append(sw2)
	data, sw1, sw2 = conn_reader.transmit(apdu)
	str = ""
	for e in data:
		str += chr(e)
	if (sw1 == 0x90):
		print ("Les données de NOM, PRENOM et N°ETUDIANT ont bien été supprimés")



def codePIN():

	if not password_adm():
		return

	apdu = [0x80, 0x06, 0x00, 0x00]
	PIN = str(input("saisir un code PIN à 4 chiffres :"))

	length = len(PIN)
	apdu.append(length)
	__print_apdu(apdu)

	for e in PIN:
		apdu.append(ord(e))

	transmit_apdu(apdu)

def codePUK():
	apdu = [0x80, 0x09, 0x00, 0x00]
	PUK = random.choices(range(10), k=4) 
	print (PUK)
	PUK_str = ''.join(map(str, PUK))
	print (PUK_str)
	length = len(PUK_str)
	apdu.append(length)
	__print_apdu(apdu)

	for e in PUK_str:
		apdu.append(ord(e))

	transmit_apdu(apdu)

# consult_PUK
''' Fonction pour afficher les données écrites sur la carte sur les entre le 40ème bit et
le 44ème bit (la ou est ecrit le code PUK) de l'EEPROM avec gestion des erreurs associées'''
def consult_PUK():
	apdu = [0x81, 0x00, 0x00, 0x00]
	data, sw1, sw2 = conn_reader.transmit(apdu)
	print("sw1 : 0x%02X | taille demandée : sw2 : 0x%02X" % (sw1, sw2))
    
	apdu.append(sw2)
	print ("l'APDU pour afficher les données de l'eeprom est :")
	__print_apdu(apdu)

	data, sw1, sw2 = conn_reader.transmit(apdu)
	str = ""
	for e in data:
			str += chr(e)
	print ("sw1 : 0x%02X | sw2 : 0x%02X | Les données sur l'eeprom sont : %s" % (sw1,sw2,str))
	return


# consult_PIN (non utilisée dans le code, seulement pour tests)
''' Fonction pour afficher les données écrites sur la carte sur les entre le 36ème bit et
le 40ème bit (la ou est ecrit le code PIN) de l'EEPROM avec gestion des erreurs associées'''
def consult_PIN():
	apdu = [0x81, 0x01, 0x00, 0x00]
	data, sw1, sw2 = conn_reader.transmit(apdu)
	print("sw1 : 0x%02X | taille demandée : sw2 : 0x%02X" % (sw1, sw2))
    
	apdu.append(sw2)
	print ("l'APDU pour afficher les données de l'eeprom est :")
	__print_apdu(apdu)

	data, sw1, sw2 = conn_reader.transmit(apdu)
	str = ""
	for e in data:
			str += chr(e)
	print ("sw1 : 0x%02X | sw2 : 0x%02X | Les données sur l'eeprom sont : %s" % (sw1,sw2,str))
	return

def modifPIN():
    if not password_adm():
        return  # Sortir de la fonction si le mot de passe n'est pas entré

    PUK = str(input("Saisir le code PUK : "))
    apdu = [0x81, 0x00, 0x00, 0x00]
    data, sw1, sw2 = conn_reader.transmit(apdu)
    apdu.append(sw2)
    data, sw1, sw2 = conn_reader.transmit(apdu)
    pukConsult = ""
    for e in data:
        pukConsult += chr(e)

    if PUK == pukConsult:
        PIN = str(input("Saisir votre nouveau PIN : "))
        apdu2 = [0x80, 0x06, 0x00, 0x00]
        length = len(PIN)
        apdu2.append(length)
        __print_apdu(apdu2)
        for e in PIN:
            apdu2.append(ord(e))

        transmit_apdu(apdu2)
    else:
        print("Code PUK incorrect. La modification du PIN a échoué.")

# main
''' Appel des fonctions définies ci-dessus'''
def main():
	init_smart_card()
	while True:
		print_menu()
		cmd = input("Choix :")
		if (cmd == '1'):
			print_version()		
		elif (cmd == '2'):
			print_data()
		elif (cmd == '3'):
			assign_card()
		elif (cmd == '4'):
			init_sold()
		elif (cmd == '5'):
			consult_sold()
		elif (cmd == '6'):
			delete_data()
		elif (cmd == '7'):
			codePIN()
			codePUK()
		elif (cmd == '8'):
			consult_PUK()
		elif (cmd == '9'):
			modifPIN()
		elif (cmd == '10'):
			return
		else :
			print ("erreur, saisissez une commande valide")
			return
	print_menu()

if __name__ == '__main__':
	banner_text = "Lubiana"
	generated_banner = generate_banner(banner_text, font="slant")
	print(generated_banner)
	main()
