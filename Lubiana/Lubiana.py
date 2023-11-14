import smartcard.System as scardsys
import smartcard.util as scardutil
import smartcard.Exceptions as scardexcp
import random

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

def __print_apdu(apdu):
        for x in apdu:
            print("0x%02X" % x, end=' ')
        print("\n")  


def transmit_apdu(apdu):
    try:
        data, sw1, sw2 = conn_reader.transmit(apdu)
        return data, sw1, sw2
    except scardexcp.CardConnectionException as e:
        print("Error", e)
        return None, None, None

def print_hello_message():
	print ("-------------------------------------------------------------------")
	print ("Bienvenue sur Lubiana, le logiciel de Personnalisation")
	print ("-------------------------------------------------------------------")
	print ("\n")

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
	print ("10 - Consulter le code PIN")
	print ("11 - Quitter")

def print_version():
	apdu = [0x81, 0x00, 0x00, 0x00, 0x04]
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

def print_data():

	apdu = [0x80, 0x04, 0x00, 0x00, 0x01]
	data, sw1, sw2 = conn_reader.transmit(apdu)
	
	print ("sw1 : 0x%02X | sw2 : 0x%02X" % (sw1,sw2))

	apdu[4] = sw2
	data, sw1, sw2 = conn_reader.transmit(apdu)
	str = ""
	for e in data:
		str += chr(e)
	print ("sw1 : 0x%02X | sw2 : 0x%02X | data : %s" % (sw1,sw2,str))
	return

def assign_card():
	apdu = [0x80, 0x03, 0x00, 0x00]
	prenom = str(input("saisir prenom :"))
	nom = str(input("saisir nom :"))
	numero_etudiant = str(input("saisir numero etudiant :"))

	__print_apdu(apdu)

	infos = prenom + " " + nom + " " + numero_etudiant
	length = len(infos)
	apdu.append(length)

	for e in infos:
		apdu.append(ord(e))

	transmit_apdu(apdu)

def init_sold():
	apdu = [0x80, 0x08, 0x00, 0x00]
	sold = "9.00"

	length = len(sold)
	apdu.append(length)
	__print_apdu(apdu)

	for e in sold:
		apdu.append(ord(e))

	transmit_apdu(apdu)

def consult_sold():
	apdu = [0x81, 0x03, 0x00, 0x00]
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

def delete_data():
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
	return


def codePIN():
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


def main():
	print_hello_message()
	init_smart_card()
	while True:
		print_menu()
		cmd = int(input("Choix :"))
		if (cmd == 1):
			print_version()		
		elif (cmd == 2):
			print_data()
		elif (cmd == 3):
			assign_card()
		elif (cmd == 4):
			init_sold()
		elif (cmd == 5):
			consult_sold()
		elif (cmd == 6):
			delete_data()
		elif (cmd == 7):
			codePIN()
			codePUK()
		elif (cmd == 8):
			consult_PUK()
		elif (cmd == 9):
			modifPIN()
		elif (cmd == 10):
			consult_PIN()
		elif (cmd == 11):
			return
		else :
			print ("erreur, saisissez une commande valide")
			return
	print_menu()

if __name__ == '__main__':
	main()
