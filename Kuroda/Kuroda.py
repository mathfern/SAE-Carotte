import smartcard.System as scardsys
import smartcard.util as scardutil
import smartcard.Exceptions as scardexcp
import mysql.connector
from datetime import datetime
from pyfiglet import Figlet

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

def generate_banner(text, font="standard"):
    f = Figlet(font=font)
    banner = f.renderText(text)
    return banner

def print_menu():
	print ("1 - Afficher le solde")
	print ("2 - Acheter un café à 0.20c")
	print ("3 - Acheter un chocolat chaud à 0.20c")
	print ("4 - Acheter un thé à 0.20c")
	print ("5 - Quitter")

def PINvalide():
	global PIN
	PIN = str(input("Saisir le code PIN : "))
	apdu = [0x81, 0x01, 0x00, 0x00]
	data, sw1, sw2 = conn_reader.transmit(apdu)
	apdu.append(sw2)
	data, sw1, sw2 = conn_reader.transmit(apdu)
	global pinConsult
	pinConsult = ""
	for e in data:
	    pinConsult += chr(e)	



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

	date_actuelle = datetime.now()

	libelle = "Cafe"

	type_ope = "Dépense"

	ope_montant = "-0.20"

	ope_montant_float = -0.20

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

	apdu = [0x80, 0x07, 0x00, 0x00]
	data, sw1, sw2 = conn_reader.transmit(apdu)
	apdu.append(sw2)
	data, sw1, sw2 = conn_reader.transmit(apdu)
	result_str = ""
	for e in data:
			result_str += chr(e)
	result_str = float(result_str)
	result_str = "{:.2f}".format(float(result_str) + 0.00)
	result_str = float(result_str)
	print (result_str)

	sql = "SELECT etu_solde FROM Etudiant WHERE etu_num = %s;"
	cursor.execute(sql, (num_etudiant,))
	student_info = cursor.fetchone()
	solde_value = float(student_info[0])
	solde_value = "{:.2f}".format(float(solde_value) + 0.00)
	solde_value2 = float(solde_value)
	print(solde_value2)

	if (result_str == solde_value2):


		if (result_str < 0.20):
			print("Pas assez de crédit, veuillez recharger")
		else:
			result_str -= 0.20

			requete_operation = "UPDATE Etudiant SET etu_solde = %s WHERE etu_num = %s"
			cursor.execute(requete_operation,(result_str,num_etudiant))


			requete_cafe = "INSERT INTO Compte (etu_num, opr_date, opr_montant, opr_libelle, type_opeartion) VALUES (%s, %s, %s, %s, %s)"
			cursor.execute(requete_operation,(result_str,num_etudiant))
			var = (num_etudiant, date_actuelle, ope_montant_float, libelle, type_ope)
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
				debit_sold()
			elif (cmd == 4):
				debit_sold()
			elif (cmd == 5):
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