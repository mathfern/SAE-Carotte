import mysql.connector

cnx = mysql.connector.connect(user='root',
password='root',
host='localhost',
database='purpledragon1') #a renommer

def print_hello_message():
    print ("-----------------------------------")
    print ("-- Logiciel de gestion : Rodelika --")
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
    sql="""select etudiant.*, sum(compte.opr_montant) as sold from Etudiant,
    compte where etudiant.etu_num = compte.etu_num group by compte.etu_num"""
    cursor = cnx.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()

def new_student():
    num_etudiant = input("Numéro Etudiant : ")
    nom_etudiant = input(\n"Nom Etudiant : ")
    prenom_etudiant = input(\n"Prénom Etudiant : ")

    #Vérifie si le num-etudiant existe ou non
    check_query = "SELECT COUNT(*) FROM etudiant WHERE etu_num = %s;"
    check_val = (num_etudiant,)
    cursor.execute(check_query, check_val)
    result = cursor.fetchone()
    
    if result[0] > 0:
        print("Le numéro d'étudiant existe déja.")
    else

    #Ajoute un nouvel étudiant à la BDD
    sql = """INSERT INTO etudiant (etu_num, etu_nom, etu_prenom) VALUES (NULL, %s,%s);""" #Requete sql
    val = (num_etudiant, nom_etudiant, prenom_etudiant) #Insere les valeurs dans la base de donnees
    cursor = cnx.cursor() #Creation du curseur 
    cursor.execute(sql, val) #Execute la requete sql sur la base de donnees
    cnx.commit() #Valide les changements effectués dans la base de donnees

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
        elif choix == 2:
            get_list_student_with_sold()
        elif choix == 3:
            new_student()
        elif choix == 4:
            add_bonus()
        elif choix == 5:
            print("Au revoir !")
            break
        else:
            print("Numéro invalide. Veuillez entrer 1,2,3,4 ou 5")
        
    
main()
