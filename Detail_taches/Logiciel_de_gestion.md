## Logiciel de gestion (Rodelika)
 
### 1-	Concept de gestion de l’administration 
Le logiciel de gestion (Rodelika) va permettre de gérer le suivi des cartes, des bonus, des débits. Dans notre cas, l’application permettra de rentrer en communication avec la base de données PurpleDragon ou on aura accès aux informations suivante :
-	Liste des étudiants
-	Solde des étudiants
-	Solde des bonus des étudiants  
    
Le logiciel de gestion va permettre plusieurs actions :
1. Afficher la liste des étudiants
   -	L’option 1 permettra d’afficher la liste de l’ensemble des étudiants possédant une carte.
2. Afficher le solde des étudiants
   -	L’option 2 permettra d’afficher le solde total de chaque étudiant.
3. Saisir un nouvel étudiant
   -	L’option 3 permettra d’attribuer une nouvelle carte à un étudiant. Elle ne permet pas la personnalisation de la carte. Elle se fait via le logiciel Lubiana.
4. Attribuer un bonus
   -	L’option 4 permettra à l’agent administratif lorsqu’il reçoit un email d’un enseignant d’attribuer un bonus. Le mail doit contenir le numéro de l’étudiant. Dans le cas contraire, l’agent administratif doit effectuer une recherche par nom et prénom avec l’option 1.
5. Quitter
   -	L’option 5 permettra de quitter.



### 2-	Programmation

L’application Rodelika sera développée avec Python. En connexion avec la base de données PurpleDragon. Pour communiquer avec la base de données MySql nous allons installer les librairies Python suivantes :
- Pip3 install mysql
- Pip3 install mysql-connector 


### 3-	Répartition classes et instructions 

La classe utilisée par Rodelika sera la classe 0x81, 0x82 et 0x83 de l’APU du projet (cf partie Carte à Puces)

Chaque opération réalisable par le logiciel sera associée à une instruction :
- Instruction pour l’affichage liste étudiante : 0x01 classe 0x81
- Instruction pour l’affichage solde étudiant : 0x01 classe 0x81
- Instruction pour l’attribution d’une nouvelle carte : 0x01 classe 0x81
- Instruction pour l’attribution d’un bonus : 0x02 classe 0x83


### 4-	Idées de fonctions à rajouter pour Rodelika

- Une instruction qui permet l’ajout d’un bonus lors de l’anniversaire
- Créer un users agent administratif pour sécuriser l'application

### 5- Vulnérabilités sur Rodelika 
- Il n'y a pas d'users donc un étudiant peut se rajouter de l'argent sans mdp
- Un hacker peut avoir accès a toutes la base de données (nom, prénom, solde)
- Possibilité de bloquer la carte
- Possibilité de bloquer le compte de l'étudiant 
