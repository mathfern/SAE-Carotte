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

Personnalisation (Lubiana)

Concept de personnalisation de carte à puce

La personnalisation de la carte à puce dans le logiciel Lubiana consiste à programmer des données spécifiques sur la puce, rendant chaque carte unique. L'objectif est d'initialiser chaque nouvelle carte attribuée à un étudiant avec les paramètres suivants :

Le nom, prénom et numéro d'étudiant de chaque titulaire de carte.
Le numéro de version de la carte.
Le solde initial à 0.00€ lors de la création de la carte.
Le logiciel Lubiana est conçu pour être utilisé par un "agent administratif" de manière interactive et simple, avec un menu offrant différentes actions.

Actions proposées par le menu :

Affichage de la version de la carte à puce :

Vérifie la version actuelle de la carte.
Affichage des données de la carte à puce :

Vérifie et affiche les données telles que le nom, le prénom et le numéro d'étudiant sur la carte. Si aucune donnée n'est présente, indique que la carte est vierge.
Attribuer la carte à un étudiant :

Permet d'ajouter le nom, le prénom et le numéro d'étudiant sur la carte.
Mettre le solde initial de 0.00€ :

Initialise le solde de la carte à 0.00€.
Consulter le solde :

Affiche le solde actuel sur la carte.
Réinitialiser les données de la carte :

Supprime les données de la carte, nécessaire en cas de réattribution.
Attribuer code PIN/PUK :

Permet de définir un nouveau code PIN et génère un code PUK aléatoire.
Consulter le code PUK :

Affiche le code PUK actuel.
Modifier le code PIN :

En cas d'oubli, permet de modifier le code PIN en utilisant le code PUK.
Quitter :

Termine l'exécution du programme.
Répartition des classes et instructions :

La classe utilisée par Lubiana sera la classe 0x81 de l'API du projet.
Chaque opération sera associée à une instruction de la classe 0x81.
Instructions pour Lubiana :

Affichage de la version : 0x00 classe 0x81
Affichage des données : 0x02 classe 0x81
Attribution de la carte : 0x01 classe 0x81
Attribution du solde initial : 0x02 classe 0x82
Affichage du solde : 0x01 classe 0x82
Réinitialisation des données de la carte : 0x05 classe 0x81
Attribution code PIN/PUK : 0x06 classe 0x81
Consultation du code PUK : 0x08 classe 0x81
Modification du code PIN : 0x09 classe 0x81
Programmation :

Lubiana sera développé en utilisant la Programmation Orientée Objet (POO) avec Python, en utilisant la librairie pyscard.

Fonctions supplémentaires pour Lubiana :

Une instruction en 0x05 pour supprimer le contenu de la carte.
Une instruction en 0x06 pour bloquer et débloquer la carte en cas de perte ou de vol.
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
