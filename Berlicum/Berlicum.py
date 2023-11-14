import smartcard.System as scardsys
import smartcard.util as scardutil
import smartcard.Exceptions as scardexcp
import mysql.connector

cnx = mysql.connector.connect(user='root',
password ='root',
host='localhost',
database= 'purpledragon1')

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
	print ("1 - Afficher mes informations")
	print ("2 - Consulter mes bonus")
	print ("3 - Transférer mes bonus sur la carte")
	print ("4 - Consulter mon crédit disponible sur la carte")
	print ("5 - Recharger par carte bancaire")
	print ("6 - Afficher l'historique des transactions")
	print ("7 - Quitter")

def affiche_info():
	apdu = [0x80, 0x04, 0x00, 0x00, 0x01]
	data, sw1, sw2 = conn_reader.transmit(apdu)
	
	print ("sw1 : 0x%02X | sw2 : 0x%02X" % (sw1,sw2))

	apdu[4] = sw2
	data, sw1, sw2 = conn_reader.transmit(apdu)
	infos = ""
	for e in data:
		infos += chr(e)
	num_etudiant = int(infos.split()[-1])
	# print (type(num_etudiant))
	# Vérifiez si le numéro d'étudiant existe déjà
	check_query = "SELECT COUNT(*) FROM Etudiant WHERE etu_num = %s;"
	check_val = (num_etudiant,)

	cursor = cnx.cursor()
	cursor.execute(check_query, check_val)
	result = cursor.fetchone()

	if result[0] < 0:
		print("Ce numéro d'étudiant n'existe pas allez voir l'agent administratif")
	else: 
		sql = "SELECT etu_num, etu_nom, etu_prenom FROM Etudiant WHERE etu_num = %s;"
		cursor.execute(sql, (num_etudiant,))
		student_info = cursor.fetchone()
		print("Informations sur l'étudiant :", student_info)
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
	# print (type(num_etudiant))
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
		print("Vous avez :", student_info , " bonus")
	return




def main():
	print_hello_message()
	init_smart_card()
	while True:
		print_menu()
		cmd = int(input("Choix :"))
		if (cmd == 1):
			affiche_info()		
		elif (cmd == 2):
			affiche_bonus()
		# elif (cmd == 3):
		# 	assign_card()
		# elif (cmd == 4):
		# 	init_sold()
		# elif (cmd == 5):
		# 	consult_sold()
		# elif (cmd == 6):
		# 	delete_data()
		elif (cmd == 7):
			return
		else :
			print ("erreur, saisissez une commande valide")
			return
	print_menu()

if __name__ == '__main__':
	main()
