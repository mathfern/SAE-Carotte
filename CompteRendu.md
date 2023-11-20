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

### Application en C pour carte à puce (Rubrovitamin)


#### 1. Qu'est-ce qu'une carte à puce ?

La carte à puce est un élément essentiel pour la vie quotidienne de millions de personnes, présente dans divers contextes tels que les cartes bancaires, les cartes d'identité et les cartes vitales. Elle stocke des données de manière sécurisée pour les protéger contre toute modification indésirable.

#### 2. Projet "La Carotte électronique" avec la carte Rubrovitamin

Dans le cadre du projet confidentiel "La Carotte électronique", nous configurons une carte à puce. Avant de configurer les cartes à puces, il faut avant tout programmer ces cartes à l'aide d'un programmateur de carte. Dans notre cas, on utilise un programmateur de type : **????**. L'objectif du code Rubrovitamin est d'être implémenté dans la mémoire flash de chaque carte à puce lors de la programmation de la carte. 

Le contenu du code en C Rubrovitamin permet aux applications : Lubiana, Kuroda et Berlicum de fonctionner puisque ces trois applications s'appuient sur les fonctions associés aux classe et instructions qui forment les APDU (cf le tableau des classes et instructions dans le 3).

Parmi les fonctions contenues dans Rubrovitamin, on peut retrouver : 

- **Intro_perso** : qui permet d'introduire des données dans l'eeprom. Cette fonction est sécurisée par un mot de passe administrateur et pour chaque utilisation de cette fonction, le mot de passe sera demandée. Les types d'actions qui peuvent nécessiter l'appel de cette fonction sont : Ecrire nom, prenom, numéro étudiant, code PIN, PUK par exemple.
- **Intro_perso_sans_mdp** : C'est la même fonction que intro_perso mais elle ne prend pas en compte la partie de sécurisation. La seule action qui nécessite l'appel de cette fonction est l'initialisation/modification du solde (utilisé par Lubiana, Berlicum et Kuroda).
- **Engage et valide** : ces deux fonctions sont implémentées pour gérer les transactions. engage initialise une transaction avec des opérations spécifiées, et valide les exécute. Les données de la transaction sont stockées en EEPROM
- **get_input_py** : Elle permet de récupérer le mot de passe entré par l'utilisateur sur Lubiana (avec l'input).
- **compareByteArrays** : Cette fonction permet de comparer les deux tableau de caractères octet par octet pour vérifier si le mot de passe utilisateur est égal au mot de passe admin défini dans le code.
- **main** : La fonction main permet de répartir les appels des fonctions citées ci-dessus dans différentes classes et instructions qui forment les APDU.   


#### 3. Classes et instructions de Rubrovitamin

Voici un tableau résumant les classes et instructions implémentées dans la carte à puce Rubrovitamin :

| Classe | Instruction | Description |
| ------ | ----------- | ----------- |
| 0x80   | 0x00        | Consulter la version de l'application |
| 0x80   | 0x01        | Entrer les données d'un étudiant |
| 0x80   | 0x02        | Consulter les étudiants ayant une carte à puce |
| 0x82   | 0x01        | Lire le solde de la carte |
| 0x82   | 0x02        | Ajouter un solde de 1.00€ |
| 0x82   | 0x03        | Acheter une boisson à 20cts |

#### 4. Nouvelles fonctionnalités pour Rubrovitamin

Nous avons ajouté une classe supplémentaire, 0x83, pour gérer les bonus. Les fonctionnalités incluent la lecture du solde de bonus, l'ajout d'un bonus à un étudiant par l'agent administratif, et le transfert des bonus obtenus sur la carte.

De plus, nous avons modifié l'instruction 0x02 de la classe 0x82 pour permettre aux étudiants de choisir la somme qu'ils veulent ajouter à leur carte à partir de leur carte bancaire, en utilisant le paramètre P1.

#### 5. Vulnérabilités

La principale vulnérabilité concerne la perte ou le vol physique de la carte. En cas de problème, les étudiants peuvent contacter l'agent administratif pour bloquer les transactions depuis la carte.


### Personnalisation (Lubiana)

#### Concept de personnalisation de carte à puce

La personnalisation de la carte à puce dans le logiciel Lubiana consiste à programmer des données spécifiques sur la puce, rendant chaque carte unique. L'objectif est d'initialiser chaque nouvelle carte attribuée à un étudiant avec les paramètres suivants :

- Le nom, prénom et numéro d'étudiant de chaque titulaire de carte.
- Le numéro de version de la carte.
- Le solde initial à 0.00€ lors de la création de la carte.

Le logiciel Lubiana est conçu pour être utilisé par un "agent administratif" de manière interactive et simple, avec un menu offrant différentes actions.

#### Actions proposées par le menu :

1. **Affichage de la version de la carte à puce :**
   - Vérifie la version actuelle de la carte.

2. **Affichage des données de la carte à puce :**
   - Vérifie et affiche les données telles que le nom, le prénom et le numéro d'étudiant sur la carte. Si aucune donnée n'est présente, indique que la carte est vierge.

3. **Attribuer la carte à un étudiant :**
   - Permet d'ajouter le nom, le prénom et le numéro d'étudiant sur la carte.

4. **Mettre le solde initial de 0.00€ :**
   - Initialise le solde de la carte à 0.00€.

5. **Consulter le solde :**
   - Affiche le solde actuel sur la carte.

6. **Réinitialiser les données de la carte :**
   - Supprime les données de la carte, nécessaire en cas de réattribution.

7. **Attribuer code PIN/PUK :**
   - Permet de définir un nouveau code PIN et génère un code PUK aléatoire.

8. **Consulter le code PUK :**
   - Affiche le code PUK actuel.

9. **Modifier le code PIN :**
   - En cas d'oubli, permet de modifier le code PIN en utilisant le code PUK.

10. **Quitter :**
    - Termine l'exécution du programme.

#### Répartition des classes et instructions :

- La classe utilisée par Lubiana sera la classe 0x81 de l'API du projet.
- Chaque opération sera associée à une instruction de la classe 0x81.

#### Instructions pour Lubiana :

1. Affichage de la version : `0x00` classe `0x81`
2. Affichage des données : `0x02` classe `0x81`
3. Attribution de la carte : `0x01` classe `0x81`
4. Attribution du solde initial : `0x02` classe `0x82`
5. Affichage du solde : `0x01` classe `0x82`
6. Réinitialisation des données de la carte : `0x05` classe `0x81`
7. Attribution code PIN/PUK : `0x06` classe `0x81`
8. Consultation du code PUK : `0x08` classe `0x81`
9. Modification du code PIN : `0x09` classe `0x81`

#### Programmation :

Lubiana sera développé en utilisant Python 3.11. Les librairies utilisées par Lubiana sont : 
- pyscard
- random
- pyfiglet
- getpass


### Borne a recharge (Berlicum) : 

- La partie "Borne de Recharge (Berlicum)" se concentre sur le développement du logiciel embarqué pour une borne de recharge utilisée par des étudiants. Le but principal de cette borne est de permettre aux étudiants d'accéder à diverses fonctionnalités liées à leurs cartes à puce. Voici un aperçu des opérations principales que les étudiants peuvent effectuer à l'aide de cette borne :

- Afficher les Informations Personnelles nommée dans le code "affiche_info": Cette fonctionnalité permet aux étudiants d'afficher les informations personnelles stockées sur leur carte à puce. Cette fonction dans le code s'appelle "

- Consulter les Bonus nommée dans le code "affiche_bonus" : Les étudiants peuvent consulter les bonus qui leur ont été attribués, mais qui n'ont pas encore été transférés sur leur carte. Les informations sur ces bonus sont extraites de la base de données, et la colonne "type_operation" dans la table "compte" indique "Bonus" pour les bonus non transférés.

- Transférer les Bonus nommée dans le code "transfert_bonus": Les étudiants peuvent utiliser la borne pour transférer les bonus disponibles sur leur carte. Une fois que les bonus ont été transférés, la colonne "type_operation" dans la table "compte" est mise à jour pour indiquer "Bonus transféré". Il est essentiel que ces transactions respectent les propriétés ACID (Atomicité, Cohérence, Isolation et Durabilité) pour garantir l'intégrité des données.

- Consulter le crédit disponible nommée dans le code "consult_sold" : Les étudiants peuvent vérifier le solde disponible sur leur carte à puce, ce qui leur permet de suivre leurs ressources.

- Recharger le Crédit avec une Carte Bancaire nommée dans le code "recharger_carte" : Lorsqu'un étudiant a épuisé ses bonus, il a la possibilité de recharger son crédit à l'aide d'une carte bancaire. Il est important de noter que le processus de recharge avec une carte bancaire est fictif dans le cadre de ce projet, et la borne simule simplement une transaction réussie.

- Le développement du logiciel embarqué pour la borne de recharge (Berlicum) est essentiel pour offrir aux étudiants un accès facile à leurs informations, à leurs bonus et à leur crédit. Ce système contribue à la gestion efficace des ressources des étudiants, en garantissant l'intégrité des transactions et en facilitant la recharge en cas de besoin.


#### Fonctions implémenter : 

- La fonction "code pin" nommée dans le code "PINvalide" a été implémenter dans ce code pour permettre une meilleure sécurisation sur la carte à puce. Donc a chaque fois qu'un étudiant insert sa carte à puce dans la borne de recharge il devra mettre son code pin qui est défini au moment de la création de sa carte à puce.

- La fonction "Afficher l'historique des transactions" nommée dans le code "" offre aux étudiants la possibilité de consulter un historique détaillé de toutes les transactions effectuées avec leur carte à puce. Cet historique est stocké dans une table "compte" de la base de données et peut être consulté à partir de la borne de recharge (Berlicum). Voici une description de cette fonctionnalité :

- Afficher l'historique des transactions : Les étudiants peuvent accéder à un récapitulatif de toutes les transactions effectuées avec leur carte à puce. Chaque transaction est enregistrée dans la base de données avec des détails tels que la date, l'heure, le type de transaction (retrait, bonus, recharge, etc.), le montant impliqué, et d'autres informations pertinentes. L'affichage de cet historique se fait de manière claire et organisée, permettant aux étudiants de comprendre facilement leur utilisation de la carte.

#### Répartition classes et instructions

La classe utilisée par berlicum sera la classe 0x81, 0x82 et 0x83 de l’API du projet (cf partie Carte à Puces). 

Chaque opération réalisable par le logiciel sera associée à une instruction de la classe 0x81, 0x82 et 0x83 : . 

- Instruction pour l’*affichage des informations personnelles* : 0x02 et classe 0x81 
- Instruction pour l’*affichage des bonus sur la carte* : 0x01 et classe 0x83
- Instruction pour l’*attribution des bonus sur la carte* : 0x02 et classe 0x83
- Instruction pour l’*affichage des crédits disponibles sur la carte* : 0x01 et classe 0x82
- Instruction pour l’*attribution d’argent sur la carte* : 0x02 et classe 0x82
- Instruction pour l'affichage de l'historique de transaction* : 0x03 et classe 0x83

#### Programmation : 

Berlicum sera développé en utilisant Python 3.11. Les librairies utilisées par Berlicum sont : 
- pyscard
- mysql-connector
- pyfiglet
- getpass






## VI. Évaluation de la Sécurité et analyse des Vulnérabilités



## VII. Conclusion


## VIII. Annexes
---

**Remarques importantes :**

- Utilisez une syntaxe Markdown pour formater votre texte (titres, listes, liens, etc.).
- Assurez-vous d'inclure des éléments visuels pertinents pour rendre le compte rendu plus compréhensible.
- Veillez à numéroter vos sections et sous-sections pour une organisation claire.

N'hésitez pas à personnaliser cette template en fonction de vos besoins spécifiques. Vous pouvez ajouter ou supprimer des sections selon les exigences de votre compte rendu.
