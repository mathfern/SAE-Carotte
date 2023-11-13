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
	print ("Bienvenue sur Kuroda, la borne de paiement de café")
	print ("-------------------------------------------------------------------")
	print ("\n")

def print_menu():
    print ("1 - Afficher le solde")
    print ("2 - Acheter un café à 0.20c")
    print ("3 - Quitter")

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

def debit_sold():
	apdu = [0x80, 0x07, 0x00, 0x00]
	data, sw1, sw2 = conn_reader.transmit(apdu)
	apdu.append(sw2)
	data, sw1, sw2 = conn_reader.transmit(apdu)
	result_str = ""
	for e in data:
			result_str += chr(e)
	solde = float(result_str)
	solde -= 0.20

	solde_str = "{:.2f}".format(solde)
	print (solde_str)
	apdu2 = [0x80, 0x08, 0x00, 0x00]
	length = len(solde_str)
	apdu2.append(length)
	print (apdu2)
	__print_apdu(apdu2)

	for e in solde_str:
		apdu2.append(ord(e))
	print (apdu2)
	try:
		data, sw1, sw2 = conn_reader.transmit(apdu2)
		print ("sw1 : 0x%02X | sw2 : 0x%02X" % (sw1,sw2))
	except scardexcp.CardConnectionException as e:
		print ("Error", e)
		return




def main():
	print_hello_message()
	init_smart_card()
	while True:
		print_menu()
		cmd = int(input("Choix :"))
		if (cmd == 1):
			consult_sold()		
		elif (cmd == 2):
			debit_sold()
		elif (cmd == 3):
			return
		else :
			print ("erreur, saisissez une commande valide")
			return
	print_menu()


if __name__ == '__main__':
	main()