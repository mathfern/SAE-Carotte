# Importation des bibliothèques nécessaires
import mysql.connector
from pyfiglet import Figlet
from tabulate import tabulate

# Établissement d'une connexion à la base de données MySQL
cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='purpledragon1') 

# Fonction pour générer une bannière à l'aide de pyfiglet
def generate_banner(text, font="standard"):
    f = Figlet(font=font)
    banner = f.renderText(text)
    return banner

# Fonction pour afficher les options du menu principal
def print_menu():
    print("")
    print(" 1 - Afficher la liste des étudiants ")
    print(" 2 - Afficher le solde des étudiants ")
    print(" 3 - Saisir un nouvel étudiant ")
    print(" 4 - Attribuer un bonus ")
    print(" 5 - Supprimer un étudiant ")
    print(" 6 - Quitter")

# Fonction pour récupérer et afficher la liste des étudiants
def get_list_student():
    sql = "SELECT etu_num, etu_nom, etu_prenom FROM Etudiant"
    cursor = cnx.cursor()  # Création d'un curseur pour interagir avec la base de données
    cursor.execute(sql)  # Exécution de la requête SQL à l'aide du curseur
    rows = cursor.fetchall() # Récupération de toutes les lignes résultantes de la requête


    # Vérification si des étudiants ont été trouvés dans la base de données
    if rows:
        headers = ["Numéro Etudiant", "Nom", "Prénom"] # Définition des en-têtes pour le tableau résultant
        table = tabulate(rows, headers=headers, tablefmt="pretty") # Utilisation de la bibliothèque tabulate pour formater les données en un tableau lisible
        print(table)
    else:
        print("Aucun étudiant trouvé dans la base de données.")

# Fonction pour récupérer et afficher la liste des étudiants avec leur solde et bonus
def get_list_student_with_sold():
    sql = "SELECT etu_num, etu_nom, etu_prenom, etu_solde, etu_bonus FROM Etudiant"
    cursor = cnx.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()

    if rows:
        headers = ["Numéro Etudiant", "Nom", "Prénom", "Solde", "Bonus"]
        table = tabulate(rows, headers=headers, tablefmt="pretty")
        print(table)
    else:
        print("Aucun étudiant trouvé dans la base de données.")

# Fonction pour ajouter un nouvel étudiant à la base de données
def new_student():
    num_etudiant = input("Numéro Etudiant : ")

    # Vérification si le numéro d'étudiant existe déjà
    check_query = "SELECT COUNT(*) FROM Etudiant WHERE etu_num = %s;"
    check_val = (num_etudiant,)

    cursor = cnx.cursor()
    cursor.execute(check_query, check_val)
    result = cursor.fetchone() # Récupération du résultat de la requête de vérification


    # Vérification si le numéro d'étudiant existe déjà
    if result[0] > 0:
        print("Le numéro d'étudiant existe déjà.")
    else:
        # Saisie des autres informations de l'étudiant
        nom_etudiant = input("Nom Etudiant : ")
        prenom_etudiant = input("Prénom Etudiant : ")
        solde_etudiant = 0.00
        bonus_etudiant = 0.00

        # Ajout d'un nouvel étudiant à la base de données
        sql = """INSERT INTO Etudiant (etu_num, etu_nom, etu_prenom, etu_solde, etu_bonus) VALUES (%s, %s, %s, %s, %s);"""
        val = (num_etudiant, nom_etudiant, prenom_etudiant, solde_etudiant, bonus_etudiant)

        cursor.execute(sql, val)
        cnx.commit() # Validation des changements dans la base de données
        print("Nouvel étudiant ajouté avec succès.")

        cursor.close()

# Fonction pour ajouter un bonus au solde d'un étudiant
def add_bonus():
    num = input("Numéro Etudiant : ")
    bonus = 1.00 # Montant du bonus à attribuer
    sql = "UPDATE Etudiant SET etu_bonus = etu_bonus + %s WHERE etu_num = %s;" # Requête SQL pour mettre à jour le bonus de l'étudiant
    cursor = cnx.cursor()
    cursor.execute(sql, (bonus, num))
    cnx.commit()
    print("Bonus + 1.00 euros")

# Fonction pour supprimer un étudiant de la base de données
def suppr_etudiant():
    num = input("Numéro Etudiant : ")
    check_query = "SELECT COUNT(*) FROM Etudiant WHERE etu_num = %s;"
    check_val = (num,)

    cursor = cnx.cursor()
    cursor.execute(check_query, check_val)
    result = cursor.fetchone()


    # Vérification si le numéro d'étudiant existe
    if result[0] > 0:
        # Suppression du compte et de l'enregistrement de l'étudiant
        sql_delete_compte = "DELETE FROM Compte WHERE etu_num = %s;"
        cursor = cnx.cursor()
        cursor.execute(sql_delete_compte, (num,))
        cnx.commit()
	
        sql_delete_etudiant = "DELETE FROM Etudiant WHERE etu_num = %s;"
        cursor.execute(sql_delete_etudiant, (num,))
        cnx.commit()
        print("L'étudiant a bien été supprimé") # Affichage d'un message indiquant le succès de la suppression
    else:
        print("Le numéro d'étudiant n'existe pas.")

# Fonction principale pour exécuter le programme
def main():
    while True:
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
            print("Numéro invalide. Veuillez entrer 1, 2, 3, 4 ou 5")

# Vérification si le script est exécuté directement
if __name__ == '__main__':
    # Affichage d'une bannière et exécution de la fonction principale
    banner_text = "Rodelika"
    generated_banner = generate_banner(banner_text, font="slant")
    print(generated_banner)
    main()

