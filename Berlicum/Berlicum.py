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
	print ("Bienvenue sur Berlicum, le logiciel de la borne de recharge")
	print ("-------------------------------------------------------------------")
	print ("\n")

def print_menu():
	print ("1 - Vérifier l'existance du compte sur la Purple Dragon")
	print ("2 - Retirer un ou plusieurs bonus")
	print ("3 - Recharger par la carte")
	print ("4 - Afficher l'historique des transactions")
	print ("5 - Quitter")