# Compte Rendu de la SAE-Carotte

## I. Introduction
<i>"La Carotte Eléctronique"</i> est le nom de code confidentiel du projet de l'IUT de Vélizy qui consiste à récompenser les étudiants travailleurs et assidus.

Ce projet est réalisé dans le cadre des SAE suivantes : 
<ul>
<li>SAE 5.01 - Concevoir, réaliser et présenter une solution technique</li>
<li>SAE 5.02 - Piloter un projet informatique</li>
</ul>
Le projet fait également appel à plusieurs compétences : 
<ul>  
  <li>Créer des outils et applications pour les R&T</li>
  <li>Utilisation du système de gestion GIT et de la plateforme GitHub ou GitLab</li>
  <li>Programmation en Python, C, HTML, CSS, PHP et Javascript</li>
  <li>Etudier les différentes vulnérabilités des applications et apporter une solution adéquate pour les sécuriser</li>
  <li>Travailler en collaboration avec les membres de l'équipe</li>
</ul>


## II. Objectifs
Le projet Carotte Electronique consiste à configurer une carte à puce, nommée Rubrovitamin où nous allons accorder des crédits supplémentaires (1€) aux élèves méritants en réalisant un système de porte-monnaie électronique à base de cartes à puce.

Ces crédits pourront ensuite être utilisés dans des distributeurs de boissons chaudes (café, thé, chocolat chaud) pour le prix de 20 centimes, cela signifie qu’un crédit accordé à un étudiant permet de lui offrir 5 boissons. 

Les étudiants devront se rendre dans le bureau administratif de l’IUT pour récupérer leurs cartes à puce et faire des réclamations en cas de problèmes de ces dernières. Quand un étudiant se présente pour la première fois afin de récupérer sa carte, l’agent administratif vérifie l’identité de l’étudiant (carte étudiant ou certificat de scolarité), puis personnalise une carte pour lui (numéro étudiant, nom, prénom, solde à 0€). L’étudiant récupère ensuite sa carte et est inscrit sur le logiciel de gestion de cartes à puces. 

Pour inciter les étudiants à venir récupérer leurs cartes, on leur attribue d’office un bonus d’un crédit (1€) qu’il faudra aller récupérer sur la borne de recharge. 


## III. Organisation et Gestion du projet

### 1 - Cahier des charges

### 2 - Répartition du temps

### 3 - Mise en place du GitHub

### 4 - Gestion du Projet avec Jira


## IV. Phase de Conception Initiale

1 - Concept de personnalisation carte à puce
La partie personnalisation consiste en général à programmer des données spécifiques sur la puce pour rendre la carte unique. Dans notre cas, la personnalisation de la carte à puce se fera pour initialiser chaque nouvelle carte avec les paramètres suivants (en vu d’être attribué à un titulaire étudiant) :

Le nom, prénom et numéro d’étudiant de chaque titulaire de carte.
Le numéro de version de la carte.
Le solde initial à 0.00€ lors de la création de la carte.
Ainsi, le logiciel Lubiana à pour objectif d’être utilisé par un “agent administratif” et doit être intéractif et simple à utiliser (avec un menu qui permet d’effectuer différentes actions). Les actions proposées par le menu sont :

Affichage de la version de la carte à puce.
Affichage des données de la carte à puce.
Attribuer la carte à un étudiant
Mettre le solde initial de 0.00€
Consulter le solde
Détails de chaque action :

Affichage de la version : Le fait d’afficher la version permet de vérifier qu’il n’existe pas une instance avec une version différente de la version implémentée dans la carte. Dans notre cas, la seule version utilisée sera 1.00.

Affichage des données : L’affichage des données permet de vérifier si les données telles que Nom, Prénom, Numéro étudiant ont déjà étés ajoutées sur cette carte. Si il existe bien des données sur la carte, le programme devrait les renvoyer sous un message : nom : XXX, prénom : XXX, Numéro Etudiant : XXX. Si ce n’est pas le cas, on devra afficher un message indiquant : carte à puce vierge.

Attribuer la carte : Pour ajouter un nom, un prénom et un numéro d’étudiant sur la carte. Cette option devra écrire les données sur la carte.

Consulter le solde : Cette option permet de consulter le solde sur la carte.

2 - Répartition classes et instructions
La classe utilisée par Lubiana sera la classe 0x81 et 0x82 de l’API du projet (cf partie Carte à Puces).

Chaque opération réalisable par le logiciel sera associée à une instruction de la classe 0x81.

Instruction pour l’affichage de la version : 0x00 classe 0x81
Instruction pour l’affichage des données : 0x02 classe 0x81
Instruction pour l’attribution de la carte : 0x01 classe 0x81
Instruction pour l’attribution du solde de base : 0x02 classe 0x82
Instruction pour l’affichage du solde : 0x01 classe 0x82
3 - Programmation
On va développer l’application Lubiana avec Python. On utilisera le type de programmation : Programmation Orientée Objet (POO) inclus dans python. Liste des librairies utilisées pour Lubiana : pyscard https://pyscard.sourceforge.io/user-guide.html#pyscard-user-guide

test

4 - Idées de fonctions à rajouter pour Lubiana
Une instruction en 0x05 qui contient une fonction qui permet de supprimer le contenu de la carte (cette option est nécessaire en cas de réattribution de la carte par exemple si un étudiant quitte l'IUT, on supprime les données de la carte avant de la réattribuer avec l'instruction 0x01).
Une instruction en 0x06 qui contient une fonction qui permet de bloquer et de débloquer la carte en cas de perte ou de vol.

## V. Features ajoutées pour chaques applications



## VI. Évaluation de la Sécurité et analyse des Vulnérabilités



## VII. Conclusion


## VIII. Annexes
---

**Remarques importantes :**

- Utilisez une syntaxe Markdown pour formater votre texte (titres, listes, liens, etc.).
- Assurez-vous d'inclure des éléments visuels pertinents pour rendre le compte rendu plus compréhensible.
- Veillez à numéroter vos sections et sous-sections pour une organisation claire.

N'hésitez pas à personnaliser cette template en fonction de vos besoins spécifiques. Vous pouvez ajouter ou supprimer des sections selon les exigences de votre compte rendu.
