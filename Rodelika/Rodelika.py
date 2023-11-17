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
    print("")
    print (" 1 - Afficher la liste des étudiants ")
    print (" 2 - Afficher le sold des étudiants ")
    print (" 3 - Saisir un nouvel étudiant ")
    print (" 4 - Attribuer un bonus ")
    print (" 5 - Supprimer un étudiant ")
    print (" 6 - Quitter")

from tabulate import tabulate

def get_list_student():
    sql = "SELECT etu_num, etu_nom, etu_prenom FROM Etudiant" // Choisi la colonne etu_num, etu_nom, etu_prenom dans la table etudiant
    cursor = cnx.cursor() // créé pour interagir avec la base de données
    cursor.execute(sql) // exécute la requète "sql" 
    rows = cursor.fetchall() // Stockent les résultats dans la variable "rows"

    if rows:
        headers = ["Numéro Etudiant", "Nom", "Prénom"]
        table = tabulate(rows, headers=headers, tablefmt="pretty") //les données sont formatées en tableau avec des en-têtes spécifiques "Numéro Etudiant", "Nom", "Prénom" à laide de la bibliothèque tabulate
        print(table) // Affiche le tableau 
    else:
        print("Aucun étudiant trouvé dans la base de données.")

def get_list_student_with_sold():
    sql = "SELECT etu_num, etu_nom, etu_prenom, etu_solde, etu_bonus FROM Etudiant" // Choisi la colonne etu_num, etu_nom, etu_prenom, etu_solde, etu_bonus dans la table etudiant
    cursor = cnx.cursor() // créé pour interagir avec la base de données
    cursor.execute(sql)
    rows = cursor.fetchall()

    if rows:
        headers = ["Numéro Etudiant", "Nom", "Prénom", "Solde", "Bonus"]
        table = tabulate(rows, headers=headers, tablefmt="pretty")
        print(table)
    else:
        print("Aucun étudiant trouvé dans la base de données.")


def new_student():
    num_etudiant = input("Numéro Etudiant : ")

    # Vérifiez si le numéro d'étudiant existe déjà
    check_query = "SELECT COUNT(*) FROM Etudiant WHERE etu_num = %s;"
    check_val = (num_etudiant,)

    cursor = cnx.cursor()
    cursor.execute(check_query, check_val)
    result = cursor.fetchone()

    if result[0] > 0:
        print("Le numéro d'étudiant existe déjà.")
    else:
        nom_etudiant = input("Nom Etudiant : ")
        prenom_etudiant = input("Prénom Etudiant : ")
        solde_etudiant = input("Solde etudiant : ")
        bonus_etudiant = input("Bonus_etudiant : ")

        # Ajoute un nouvel étudiant à la BDD
        sql = """INSERT INTO Etudiant (etu_num, etu_nom, etu_prenom, etu_solde, etu_bonus) VALUES (%s, %s, %s, %s, %s);"""
        val = (num_etudiant, nom_etudiant, prenom_etudiant, solde_etudiant, bonus_etudiant)

        cursor.execute(sql, val)
        cnx.commit()
        print("Nouvel étudiant ajouté avec succès.")

        cursor.close()




def add_bonus():
    num = input("Numéro Etudiant : ")
    #com = input("Commentaire : ")
    bonus = 1.00
    sql = "UPDATE Etudiant SET etu_bonus = etu_bonus + %s WHERE etu_num = %s;"
    cursor = cnx.cursor()
    cursor.execute(sql,(bonus,num))
    cnx.commit()
    # compléter le code
    print ("Bonus + 1.00 euros")

def suppr_etudiant():
    num = input("Numéro Etudiant : ")
    check_query = "SELECT COUNT(*) FROM Etudiant WHERE etu_num = %s;"
    check_val = (num,)

    cursor = cnx.cursor()
    cursor.execute(check_query, check_val)
    result = cursor.fetchone()

    if result[0] > 0:
        sql_delete_compte = "DELETE FROM Compte WHERE etu_num = %s;"
        cursor = cnx.cursor()
        cursor.execute(sql_delete_compte, (num,))
        cnx.commit()

    
        sql_delete_etudiant = "DELETE FROM Etudiant WHERE etu_num = %s;"
        cursor.execute(sql_delete_etudiant, (num,))
        cnx.commit()
        print("L'étudiant a bien été supprimer")
        
    else:
        print("Le numéro d'étudiant n'existe pas.")
    
    
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
            suppr_etudiant()
        elif choix == 6:
            print("Au revoir !")
            break
        else:
            print("Numéro invalide. Veuillez entrer 1,2,3,4 ou 5")
        
    
main()
