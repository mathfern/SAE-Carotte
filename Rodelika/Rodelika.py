import mysql.connector

cnx = mysql.connector.connect(user='root',
password='root',
host='localhost',
database='purpledragon1') #a renommer

def print_hello_message():
    print ("-----------------------------------")
    print ("-- Logiciel de gestion : Rodlika --")
    print ("-----------------------------------")

def print_menu():
    print (" 1 - Afficher la liste des étudiants ")
    print (" 2 - Afficher le sold des étudiants ")
    print (" 3 - Saisir un nouvel étudiant ")
    print (" 4 - Attribuer un bonus ")
    print (" 5 - Quitter")

def get_list_student():
    sql="select * from Etudiant"
    cursor = cnx.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()

def get_list_student_with_sold():
    sql="""select etudiant.*, sum(compte.opr_montant) as sold from etudiant,
    compte where etudiant.etu_num = compte.etu_num group by compte.etu_num"""
    cursor = cnx.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()

def new_student():
    nom = input("Nom Etudiant : ")
    pre = input("Pre Etudiant : ")
    sql = """INSERT INTO etudiant (etu_num, etu_nom, etu_prenom) VALUES (NULL, %s,%s);"""
    val = (nom, pre)
    cursor = cnx.cursor()
    cursor.execute(sql, val)
    cnx.commit()

def add_bonus():
    num = input("Num Etudiant : ")
    com = input("Commentaire : ")
    # compléter le code
    print ("Bonus + 1.00 euros")

def main():
    print_hello_message()
    while True :
        print_menu()
        choix = int(input("Quel est votre choix ? : "))
        if choix == 1:
            get_list_student()
        
    
main()
