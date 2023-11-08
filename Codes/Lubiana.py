import smartcard.System as scardsys
import smartcard.util as scardutil
import smartcard.Exceptions as scardexcp

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
	print ("6 - Quitter")

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

def print_data():
	apdu = [0x80, 0x04, 0x00, 0x00]
	data, sw1, sw2 = conn_reader.transmit(apdu)
	print("sw1 : 0x%02X | sw2 : 0x%02X" % (sw1, sw2))
    # except scardexcp.CardConnectionException as e:
	#	print("Erreur", e)
	#	return

	apdu.append(sw2)
	__print_apdu(apdu)

	data, sw1, sw2 = conn_reader.transmit(apdu)
	#str = ""
	#for e in data:
	#		str += chr(e)
	#print ("sw1 : 0x%02X | sw2 : 0x%02X | version %s" % (sw1,sw2,str))
	return

def assign_card():
	apdu = [0x80, 0x03, 0x00, 0x00]
	prenom = str(input("saisir prenom :"))
	nom = str(input("saisir nom :"))
	numero_etudiant = str(input("saisir numero etudiant :"))

	length = len(prenom) + len(nom) + len(numero_etudiant)

	
	apdu.append(length)
	__print_apdu(apdu)

	for e in prenom + nom + numero_etudiant:
		apdu.append(ord(e))
	print (apdu)
	try:
		data, sw1, sw2 = conn_reader.transmit(apdu)
		print ("sw1 : 0x%02X | sw2 : 0x%02X" % (sw1,sw2))
	except scardexcp.CardConnectionException as e:
		print ("Error", e)
		return

def main():
	print_hello_message()
	init_smart_card()
	print_menu()
	cmd = int(input("Choix :"))
	if (cmd == 1):
		print_version()		
	elif (cmd == 2):
		print_data()
	elif (cmd == 3):
		assign_card()
	elif (cmd == 6):
		return
	else :
		print ("erreur, saisissez une commande valide")
		return

if __name__ == '__main__':
	main()
