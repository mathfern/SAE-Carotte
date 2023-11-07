## Personnalisation (Lubiana) 

### 1 - Concept de personnalisation carte à puce
La partie personnalisation consiste en général à programmer des données spécifiques sur la puce pour rendre la carte unique. Dans notre cas, la personnalisation de la carte à puce se fera pour initialiser chaque nouvelle carte avec les paramètres suivants (en vu d’être attribué à un titulaire étudiant) : 

- Le nom, prénom et numéro d’étudiant de chaque titulaire de carte.
- Le numéro de version de la carte.
- Le solde à 1.00€ pour la création de la carte.

Ainsi, le logiciel Lubiana à pour objectif d’être utilisé par un “agent administratif” et doit être intéractif et simple à utiliser (avec un menu qui permet d’effectuer différentes actions). Les actions proposées par le menu sont : 

- Affichage de la version de la carte à puce. 
- Affichage des données de la carte à puce.
- Attribuer la carte à un étudiant
- Mettre le solde initial de 1.00€
- Consulter le solde

Détails de chaque action : 

*Affichage de la version* : Le fait d’afficher la version permet de vérifier qu’il n’existe pas une instance avec une version différente de la version implémentée dans la carte. Dans notre cas, la seule version utilisée sera 1.00.

*Affichage des données* : L’affichage des données permet de vérifier si les données telles que Nom, Prénom, Numéro étudiant ont déjà étés ajoutées sur cette carte. Si il existe bien des données sur la carte, le programme devrait les renvoyer sous un message : nom : XXX, prénom : XXX, Numéro Etudiant : XXX. Si ce n’est pas le cas, on devra afficher un message indiquant : carte à puce vierge.

*Attribuer la carte* : Pour ajouter un nom, un prénom et un numéro d’étudiant sur la carte. Cette option devra écrire les données sur la carte.

*Mettre le solde à 1.00€* : Cette option ajoute 1.00€ sur la carte.

*Consulter le solde* : Cette option permet de consulter le solde sur la carte.

### 2 - Répartition classes et instructions

La classe utilisée par Lubiana sera la classe 0x81 et 0x82 de l’API du projet (cf partie Carte à Puces). 

Chaque opération réalisable par le logiciel sera associée à une instruction de la classe 0x81. 

- Instruction pour l’*affichage de la version* : **0x00** classe 0x81
- Instruction pour l’*affichage des données* : **0x02** classe 0x81
- Instruction pour l’*attribution de la carte* : **0x01** classe 0x81
- Instruction pour l’*attribution du solde de base* : **0x02** classe 0x82
- Instruction pour l’*affichage du solde* : **0x01** classe 0x82


### 3 - Programmation

On va développer l’application Lubiana avec **Python**. On utilisera le type de programmation : Programmation Orientée Objet (POO) inclus dans python. 
Liste des librairies utilisées pour Lubiana : 
pyscard https://pyscard.sourceforge.io/user-guide.html#pyscard-user-guide


``` test ```

### 4 - Idées de fonctions à rajouter pour Lubiana

- Une instruction en 0x05 qui contient une fonction qui permet de supprimer le contenu de la carte (cette option est nécessaire en cas de réattribution de la carte par exemple si un étudiant quitte l'IUT, on supprime les données de la carte avant de la réattribuer avec l'instruction 0x01).
- Une instruction en 0x06 qui contient une fonction qui permet de bloquer et de débloquer la carte en cas de perte ou de vol. 
