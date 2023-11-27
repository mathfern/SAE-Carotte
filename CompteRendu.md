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
  <li>Apprentissage du fonctionnement d'une carte à puce et utilisation de celle-ci avec programmateur et lecteur de carte</li>
  <li>Utilisation d'outil de gestion de projet (Jira)</li>
  <li>Etudier les différentes vulnérabilités des applications et apporter une solution adéquate pour les sécuriser</li>
  <li>Travailler en collaboration avec les membres de l'équipe</li>
</ul>


## II. Objectifs
Le projet Carotte Electronique consiste à configurer une carte à puce, où nous allons accorder des crédits supplémentaires (1€) aux élèves méritants en réalisant un système de porte-monnaie électronique à base de cartes à puce.

Ces crédits pourront ensuite être utilisés dans des distributeurs de boissons chaudes (café, thé, chocolat chaud) pour le prix de 20 centimes, cela signifie qu’un crédit accordé à un étudiant permet de lui offrir 5 boissons. 

Les étudiants devront se rendre dans le bureau administratif de l’IUT pour récupérer leurs cartes à puce et faire des réclamations en cas de problèmes de ces dernières. Quand un étudiant se présente pour la première fois afin de récupérer sa carte, l’agent administratif vérifie l’identité de l’étudiant (carte étudiant ou certificat de scolarité), puis personnalise une carte pour lui (numéro étudiant, nom, prénom, solde à 0€, code PIN, code PUK). L’étudiant récupère ensuite sa carte et est inscrit sur le logiciel de gestion de cartes à puces. 

Pour inciter les étudiants à venir récupérer leurs cartes, on leur attribue d’office un bonus d’un crédit (1€) qu’il faudra aller récupérer sur la borne de recharge. 

Voici ci-dessous le schéma relationnel des applications qui seront détaillées plus tard dans le compte rendu : 
![image](https://github.com/mathfern/SAE-Carotte/assets/150126396/7ecb9f2a-e2a4-4579-ab8a-a54898d8bd9b)



## III. Organisation et Gestion du projet

### 1 - Cahier des charges

### 2 - Répartition du temps

Pour organiser notre emploi du temps, nous avons entamé le processus en énumérant toutes les tâches à accomplir. Ensuite, nous avons répertorié les compétences de chacun afin de déterminer quelles tâches nous semblaient les plus simples à réaliser. Une fois cette liste établie, nous avons élaboré un diagramme de Gantt pour nous fournir une feuille de route dans le cadre de la SAE.

![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/835c5a10-a214-49d4-b519-9b8ced94e0a7)

En suivant notre planning prévisionnel, nous avons réussi à terminer la SAE dans les délais impartis. Cependant, certaines applications, telles que Rubrovitamin, Lubiana, Rodelika (et Web), nous ont demandé plus de temps que les autres, ce qui a entraîné des retards par rapport à notre diagramme prévisionnel. Voici un diagramme illustrant le temps réel que nous avons consacré à chaque application :

![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/3c466bbe-f4f7-4a76-bf1a-b7ad3a9d1f76)

### 3 - Mise en place du GitHub

### 4 - Gestion du Projet avec Jira

#### Présentation de Jira

Introduction :
Jira est un logiciel de gestion de projet développé par Atlassian, une entreprise spécialisée dans les outils de collaboration et de développement logiciel. Lancé initialement en 2002, Jira est devenu un choix populaire parmi les équipes de développement, les équipes informatiques et les équipes de gestion de projet pour sa flexibilité, sa personnalisation et sa puissance.

Caractéristiques clés :
- Gestion des tâches : Jira permet de créer, attribuer et suivre les tâches au sein d'un projet. Les utilisateurs peuvent définir des priorités, des échéances et des dépendances pour garantir une gestion efficace des activités.
- Tableaux : Jira prend en charge les méthodologies agiles, offrant des tableaux pour la gestion visuelle des projets. Les équipes peuvent suivre les progrès, gérer les sprints et ajuster les priorités de manière flexible.
- Personnalisation : Jira est hautement configurable pour s'adapter aux besoins spécifiques de chaque équipe. Les champs, les workflows et les tableaux de bord peuvent être adaptés pour répondre aux exigences uniques de chaque projet.
- Suivi du temps : Les fonctionnalités intégrées de suivi du temps permettent aux utilisateurs de mesurer précisément le temps passé sur chaque tâche, fournissant ainsi des données essentielles pour l'estimation des projets futurs.
  
Notre utilisations :<br>
Nous avons utilisé Jira pour le suivi de notre projet, attribuant des tâches spécifiques à chaque application. Chaque tâche a été divisée en plusieurs parties. Prenons l'exemple de la tâche "Rédaction des tâches + Planification":<br>
- Titre : <br>
Nom de la tâches
- Description : <br>
Dans la description, il est possible d'insérer un texte pour expliquer le travail à effectuer, ou, comme dans notre cas, une image. Dans cette instance, nous avons inclus le planning prévisionnel des tâches :
![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/835c5a10-a214-49d4-b519-9b8ced94e0a7)



## IV. Phase de Conception Initiale

### Application en C pour carte à puce (Rubrovitamin)


#### 1. Qu'est-ce qu'une carte à puce ?

##### Description générale d'une carte à puce
La carte à puce est un élément essentiel pour la vie quotidienne de millions de personnes, présente dans divers contextes tels que les cartes bancaires, les cartes d'identité et les cartes vitales. Elle stocke des données de manière sécurisée pour les protéger contre toute modification indésirable. Les cartes à puces sont des cartes munies d'un micro-processeur capable de stocker, traiter et sécuriser des informations.

##### Description technique d'une carte à puce

La composition technique d'une carte à puce est la suivante : 
- **Microprocesseur** qui est en quelques sorte le cerveau de la carte, c'est lui qui traite les données et exécute les instructions.
- **Mémoire Flash** qui est utilisée pour stocker les données non volatiles (ce qui signifie que ce sont les données qui restent présentent sur la carte même lorsqu'elle n'est pas alimentée). Elle est utilisée pour stocker des informations comme la version de la carte et le code contenant les fonctions, classes et instructions associées qui forment les APDUs. 
- **RAM (Random Access Memory)** qui est une mémoire volatile utilisée pour le stockage temporaire pendant l'exécution des programmes. Elle permet en règle générale de traiter des opérations plus rapidemment que les autres types de mémoires et est de ce fait utilisée pour des opérations temporaires et de traitement en cours.
- **EEPROM (Electrically Erasable Programmable Read-Only Memory)** est une mémoire non volatile également, elle stocke les données de manière permanente. Cette mémoire est flexible puisque comme son nom l'indique, c'est une mémoire qui peut être effacée, programmée et lue. Cette mémoire permet de stocker des informations et données sensibles de manière sécurisée.

##### Cycle de vie d'une carte à puce

- Le developpement, c'est dans cette partie que l'on test et que l'on imagine le programme (Rubrovitamin) en faisant des tests de programmation en mémoire flash. Le développement représente le code que l'on implémente en mémoire flash. 
- La programmation, c'est la partie dans laquelle on implémente le code Rubrovitamin dans la mémoire flash dans la carte à l'aide de la fonction progcarte (make progcarte)
- La personnalisation est la tâche réalisée par l'agent administratif qui a pour objectif d'écrire des informations personnelles sur la carte dans la mémoire EEPROM. On stockera des données telles que le nom, le prenom, le num etudiant, le solde, le code pin et le code puk.
- Vie, le moment ou l'étudiant pourra utiliser et profiter de sa carte
- Destruction, le moment ou la carte sera réinitialisée pour être attribuée à un autre étudiant.

##### Détails sur le type de cartes à puces utilisées pour le projet

Pour ce projet, le type de puce utilisé est une **ATMega328**. C'est un microcontrôleur 8 bits basé sur l'architecture Harvard. C'est un type de processeur qui sépare physiquement la mémoire de données et la mémoire programme. L’accès à chacune des deux mémoires s’effectue via deux bus distincts ce qui représente une amélioration des performances comparé à certaines technologies à un bus commun pour programme et données comme l'architecture Von Neumann par exemple. 

Pour en revenir au fonctionnement techniques des cartes utilisées pour le projet, voici un schéma qui détaille l'architecture utilisée par celles-ci : 
![Design sans titre](https://github.com/mathfern/SAE-Carotte/assets/134608345/f07992ab-d47c-4cd9-902b-f0a815595b79)



##### Normes utilisées

La norme que nous allons utiliser est la norme ISO 7816 et plus particulièrement la norme ISO 7816-4 qui définie les commandes de base de la carte permettant ainsi de comprendre le dialogue entre une carte et un lecteur. En effet, cette partie de la norme ISO 7816 traite et définie précisément de l'organisation, la sécurité et des commandes. Elle définit entre autre les messages APDU (Application Protocol Data Units), par lesquels les cartes à puce communiquent avec le lecteur.

https://www.iso.org/fr/standard/77180.html


##### Phase de communications entre la carte et le lecteur

Il existe trois principales étapes de communication entre la carte et l'ordinateur : 
- **Reset** : C'est la carte qui prend l'initiative de réaliser le RESET. Dès lors que la carte est insérée dans un lecteur de carte (connecté à un ordinateur), cette étape permet au lecteur d’identifier la carte qu’il est en train de lire et de vérifier la compatibilité de la carte et du lecteur. Si la carte s'avère compatible, on passe à la prochaine étape, sinon elle est rejetée.
  
- **ATR** : L'ATR ou Answer To Reset est la réponse du lecteur pour le RESET effectué par la carte. Dès lors que la carte est reset, elle envoie un "ATR" d'une taille maximale de 33 octets qui est une séquence binaire qui contient des informations cruciales sur les capacités et les caractéristiques de la carte à puce.
Par la suite, le lecteur analyse l'ATR pour déterminer comment communiquer avec la carte à puce. L'ATR contient des informations telles que le protocole de communication à utiliser, la taille des données, la vitesse de transmission, etc ..
La forme de l'ATR est :
L’ATR contient deux octets :
TS=0x3b, appelé octet initial
T0=0x0n où n désigne un nombre, appelé octet de format
Les quatre premiers bits de l’octet de format sont à 0 et le dernier correspond au
nombre d’octets d’historique limité à 15 (0 ≤ n ≤ F)
Dans notre cas, l'envoi de l'ATR est défini dans la fonction atr() du progcarte.c :
![atr](https://github.com/mathfern/SAE-Carotte/assets/134608345/4de4bd87-e515-494f-80ae-9a500f1885d2)


- **APDUs** :

Une fois l'ATR transmis, la carte se met en attente de commande. Les commandes se transmettent à partir d'APDU dans le domaine des cartes à puces. 
Ici, c'est nos logiciels Berlicum, Lubiana, Kuroda qui envoient des APDUs à la carte pour aller utiliser les fonctions associées dans le code en mémoire flash. 

La composition d'un APDU est la suivante : 
5 octets d'entête : 
| CLA | INS | P1 | P2 | P3 |
|-----|-----|----|----|----|

- Cla : correspond au numéro de classe qui contient les instructions (cf tableau ci dessus)
- Ins : correspond au numéro d'instruction associé
- P1 : désigne le paramètre 1 (défini à 0 si l'APDU ne nécessite pas de paramètre 1)
- P2 : désigne le paramètre 2 (défini à 0 si l'APDU ne nécessite pas de paramètre 2)
- P3 : désigne la taille des données à écrire dans l'EEPROM

Il existe deux types d'APDUs :
- Les APDUs entrantes : L'APDU de commande est envoyée par le terminal à la carte à puce pour demander une action particulière. Elle est composée de deux parties

Header (En-tête) : Les quatre premiers octets de l'APDU, qui spécifient l'instruction à exécuter (par exemple, lire des données, écrire des données, initialiser une opération, etc.) et d'autres informations telles que la classe et le canal.

Body (Corps) : Les octets restants de l'APDU, qui peuvent contenir des données spécifiques à l'instruction (par exemple, les données à écrire sur la carte).

![Capture d'écran 2023-11-22 110914](https://github.com/mathfern/SAE-Carotte/assets/134608345/c1c89fd1-5ec8-48d8-8f64-e339ee309893) <br>

schéma issu du cours de Mr.DJERROUD : Exemple d'échanges pour une commande entrante

- Les APDUs sortantes : L'APDU de réponse est renvoyée par la carte à puce en réponse à une APDU de commande. Elle est également composée de deux parties :

Données de Réponse : Les octets qui portent les données demandées par l'instruction de la commande. Par exemple, si la commande demandait la lecture de données, ces octets contiendront les données lues.

SW1-SW2 (Status Word) : Les deux derniers octets de l'APDU, appelés Status Word (SW1 et SW2). Ces octets indiquent l'état de la commande. Ils peuvent signaler si la commande s'est exécutée avec succès, si une erreur s'est produite, ou d'autres informations sur le statut de la transaction.

La carte peut répondre de deux manière : 
- Dans un premier temps, un acquittement qui atteste que l'appel de l'APDU s'est bien passé généralement SW1 = 0x90.
- Dans un second temps, un message d'erreur personnalisé conformément au tableau ci dessous : 

| Status Word | d’erreur                                 | Signification                                      |
|-------------|------------------------------------------|----------------------------------------------------|
| 6e 00       | CLA inconnue                             |                                                    |
| 6d 00       | CLA connue, INS inconnue                  |                                                    |
| 6b 00       | CLA, INS connues mais P1 et P2 incorrects |                                                    |
| 6c xx       | CLA, INS, P1 et P2 corrects mais P3 incorrect | xx désigne le P3 attendu                           |

![apdu sortante](https://github.com/mathfern/SAE-Carotte/assets/134608345/7793c6dd-3264-4765-8917-9d4ab8d3a2a1)

schéma issu du cours de Mr.DJERROUD : Exemple d'échanges pour une commande sortante

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
| 0x80   | 0x01        | Récupérer les données entrées dans l'input du mot de passe admin |
| 0x80   | 0x03        | Ajouter un nom, prenom, numéro d'étudiant sur la carte |
| 0x80   | 0x04        | Lire le nom, prenom, numéro d'étudiant sur la carte |
| 0x80   | 0x05        | Supprimer le nom, prenom, numéro d'étudiant et solde sur la carte |
| 0x80   | 0x06        | Ajouter le code PIN sur la carte |
| 0x80   | 0x07        | Lire le solde de la carte |
| 0x80   | 0x08        | Initialiser le solde à 0.00€ sur la carte |
| 0x80   | 0x09        | Ajouter le code PUK sur la carte |
| 0x81   | 0x00        | Lire le code PUK de la carte |
| 0x81   | 0x01        | Lire le code PIN de la carte |

#### 4. Nouvelles fonctionnalités pour Rubrovitamin

De base, Rubrovitamin est le logiciel qui prend en compte la lecture de la version, l'ecriture des données dans la carte, la lecture des données dans la carte, l'ecriture du solde dans la carte et la lecture. 

De notre propre initiative et pour rendre le logiciel plus complet et ergonomique, nous avons décidé de rajouter les fonctionnalités d'ajout et de lecture de codes PIN et PUK, la réinitialisation de la carte, la sécurisation de l'accès à l'ecriture sur l'EEPROM.

#### 5. Vulnérabilités

Il y a deux principaux types de vulnérabilités possibles liées aux cartes à puces directement : 

##### Vulnérabilité physique (matérielle)
La perte ou le vol physique de la carte peuvent être considérés comme une vulnérabilité. En cas de problème, les étudiants peuvent contacter l'agent administratif qui devrait être en mesure de bloquer les transactions depuis la carte pour cela, il suffit que l'utilisateur soit bloqué sur la base de données.

##### Vulnérabilité logicielle (Rubrovitamin)
Si les APDU ne sont pas sécurisées, n'importe quel individu en possession d'une carte à puce programmée avec le code de Rubrovitamin dans la mémoire flash peut utiliser un langage de programmation pour envoyer des APDU 

Une description des vulnérabilité plus détaillée de cette application est disponible plus bas dans le compte rendu. 

### Personnalisation (Lubiana)

#### Concept de personnalisation de carte à puce

La personnalisation de la carte à puce dans le logiciel Lubiana consiste à programmer des données spécifiques sur la puce, rendant chaque carte unique. L'objectif est d'initialiser chaque nouvelle carte attribuée à un étudiant avec les paramètres suivants :

- Le nom, prénom et numéro d'étudiant de chaque titulaire de carte.
- Le solde initial à 0.00€ lors de la création de la carte.
- Le code PIN et PUK de la carte

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

- La classe utilisée par Lubiana sera les classes 0x81 et 0x80 de l'API du projet.
- Chaque opération sera associée à une instruction de ces classes.

#### Instructions pour Lubiana :

| Classe | Instruction | Description |
| ------ | ----------- | ----------- |
| 0x80   | 0x00        | Consulter la version de l'application |
| 0x80   | 0x01        | Récupérer les données entrées dans l'input du mot de passe admin |
| 0x80   | 0x03        | Ajouter un nom, prenom, numéro d'étudiant sur la carte |
| 0x80   | 0x04        | Lire le nom, prenom, numéro d'étudiant sur la carte |
| 0x80   | 0x05        | Supprimer le nom, prenom, numéro d'étudiant et solde sur la carte |
| 0x80   | 0x06        | Ajouter le code PIN sur la carte |
| 0x80   | 0x07        | Lire le solde de la carte |
| 0x80   | 0x08        | Initialiser le solde à 0.00€ sur la carte |
| 0x80   | 0x09        | Ajouter le code PUK sur la carte |
| 0x81   | 0x00        | Lire le code PUK de la carte |
| 0x81   | 0x01        | Lire le code PIN de la carte |

#### Programmation :

Lubiana sera développé en utilisant Python 3.11. Les librairies utilisées par Lubiana sont : 
- pyscard
- random
- pyfiglet
- getpass

#### Gestion des erreurs : 

Lubiana est capable d'afficher et de gérer les erreurs de classes, d'instructions et de paramètre p3 lorsque l'APDU des données envoyées est de mauvaise taille.
En effet, elle utilise les variables sw1 et sw2 pour stocker les codes d'erreurs : 


### Purple Dragon (Base de données)

#### Concept de base de donnée carte à puce : 

Une base de données (purple dragon) implémenter en mysql pour les cartes à puce est une base de données utilisée pour stocker des informations liées aux cartes à puce :

- Les données des étudiants comme le numéro d’étudiant et contient uniquement les informations essentielles, à savoir le nom, le prénom, le solde et les bonus. 

- Les données du compte qui représente les opérations effectuées par les utilisateurs, elle est identifiée par la date de l’opération, et contient deux autres 
  champs, le montant de l’opération et sa description. Étant donné que plusieurs utilisateurs peuvent effectuer simultanément différentes opérations, nous avons 
  choisi d'associer le numéro d'étudiant à la clé primaire en utilisant une relation relative (R). Le montant de l'opération peut être positif en cas de bonus ou 
  de crédit, ou négatif en cas de débit.

- Les données du type de l’opération qui permet de catégoriser les types d'opérations : Bonus, Bonus transféré, Crédit et Débit.


Le schémas relationnel (MCD) proposé est donné ci-après : 

![image](https://github.com/mathfern/SAE-Carotte/assets/150126517/3a7f34bb-3c22-4650-a28d-bbfdfdd74d67)

Cette base de données devra être accessible par le logiciel de gestion Rodelika afin de permettre à l’agent administratif de gérer le suivi des cartes, des bonus, des débit etc. L’étudiant a chaque fois qu’il va insérer sa carte à puces les données de la carte à puces seront stockées dans la base de données.

#### Idées implémentées :

- Ajout d'une table admin avec les colonnes admin_id, nom et mot de passe en hash Bcrypt dans la base de données, ce qui permet d'avoir une authentification sur la version web de Rodelika. Cela fait en sorte que tout le monde ne puisse pas accéder à la base de donner et la modifier. 

- Ajout des colonnes etu_solde, etu_bonus dans la table étudiant pour permettre de stocker ces informations pour chaque étudiant.
  
#### Programmation

La base de données Purpledragon sera développée en sql. 

#### Vulnérabilités et solutions :

Les bases de données MySQL sont sujettes à plusieurs vulnérabilités potentielles qui peuvent mettre en danger la sécurité de vos données. Voici quelques-unes des vulnérabilités courantes et des mesures pour y remédier :

1. **Injection SQL :** Les attaques par injection SQL sont l'une des vulnérabilités les plus courantes. Les attaquants insèrent du code SQL malveillant dans les requêtes pour accéder, modifier ou supprimer des données. Pour y remédier :
   - Utilisez des requêtes préparées ou des procédures stockées pour éviter l'injection SQL.
   - Assurez-vous de filtrer et de valider toutes les données utilisateur avant de les utiliser dans des requêtes SQL.

2. **Authentification faible :** Une authentification faible, des mots de passe faibles ou l'utilisation de comptes par défaut peuvent faciliter l'accès non autorisé à la base de données. Pour y remédier :
   - Utilisez des mots de passe forts et encouragez une politique de gestion des mots de passe.
   - Limitez l'accès en fonction des principes du moindre privilège, en n'accordant que les autorisations nécessaires à chaque utilisateur.

### Logiciel de gestion (Rodelika)

#### Concept de gestion de l’administration :
Le logiciel de gestion (Rodelika) va permettre de gérer le suivi des cartes, des bonus, des débits. Dans notre cas, l’application permettra de rentrer en communication avec la base de données PurpleDragon ou on aura accès aux informations suivante :

- Liste des étudiants
- Solde des étudiants
- Saisir un nouvel étudiant
- Attribuer un bonus à un étudiant
- Supprimer un étudiant 

Le logiciel de gestion va permettre plusieurs actions :

- L’option 1 "liste des étudiants" nommée dans le code "get_list_student" permettra d’afficher la liste de l’ensemble des étudiants possédant une carte.

- L’option 2 "solde des étudiants" nommée dans le code "get_list_student_with_sold" permettra d’afficher le solde total de chaque étudiant.

- L’option 3 "saisir un nouvel étudiant" nommée dans le code "new_student" permettra d’attribuer une nouvelle carte à un étudiant. Elle ne permet pas la personnalisation de la carte. Elle se fait via le logiciel Lubiana.

- L’option 4 "attribuer un bonus à un étudiant" nommée dans le code "add_bonus" permettra à l’agent administratif lorsqu’il reçoit un email d’un enseignant d’attribuer un bonus. Le mail doit contenir le numéro de l’étudiant. Dans le cas contraire, l’agent administratif doit effectuer une recherche par nom et prénom avec l’option 1.

#### Fonction implémentées :

- L'option 5 "supprimer un étudiant" nommée dans le code "suppr_etudiant" permettra à l'agent administratif de supprimer un étudiant de la base de données.

#### Répartition classes et instructions :

La classe utilisée par Rodelika sera la classe 0x81, 0x82 et 0x83 de l’APU du projet (cf partie Carte à Puces)

Chaque opération réalisable par le logiciel sera associée à une instruction :

- Instruction pour l’affichage liste étudiante : 0x01 classe 0x81
- Instruction pour l’affichage solde étudiant : 0x01 classe 0x81
- Instruction pour l’attribution d’une nouvelle carte : 0x01 classe 0x81
- Instruction pour l’attribution d’un bonus : 0x02 classe 0x83
- Instruction pour la supression d'un étudiant : 0x04 classe 0x81

#### Programmation :

L’application Rodelika sera développée avec Python. En connexion avec la base de données PurpleDragon. Pour communiquer avec la base de données MySql nous allons installer les librairies Python suivantes :

- mysql-connector
- tabulate
- pyfiglet

### Application web de gestion (RodelikaWeb)

L’application web de gestion donne la possibilité à l’agent administratif d’avoir une interface graphique qui permet l’utilisation plus interactive du logiciel de gestion Rodelika.

Ce site sera codé en HTML/CSS, PHP et javascript et fera appel à la base de données PurpleDragon ainsi qu'à l'application Rodelika.


#### Fonctionnalités implémentées

On a ajouter une interface graphique pour chaque fonction pour l'agent administratif afin qu'ils puissent effectuer les manipulations plus facilement et interactive :
![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/96ac695c-26a5-4bf3-857e-296bb782ac22)
- liste des étudiants :<br>
Le programme Web utilise la fonctionnalité 1 du script Rodelika pour afficher les informations telles que le numéro étudiant, le nom et le prénom de l'étudiant.
![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/59ad1439-ad29-4385-95b3-4ae8e904335b)


- liste des étudiants avec le solde et bonus:<br>
De même que précédemment, nous allons utiliser l'option 2 de Rodelika pour afficher les informations incluant le numéro étudiant, le nom, le prénom, le solde et les bonus de l'étudiant.
![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/e344d96d-040c-4924-94e7-4c71337ff09b)

- ajouter un nouvel étudiant : 
![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/3b6b896a-3938-4670-bfd6-9f505d2145b1)

- attribuer un bonus :
![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/0e1be92b-c83e-4784-81d2-34ab7cbf210e)


- supprimer un étudiant :
![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/b4cca0a3-e16b-40d5-acee-99e61978565a)


- interface de connexion pour l’agent administratif pour sécuriser l’ajout de soldes dans la bdd :
![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/aca45aa2-4618-4722-aa89-667ac27c362a)



### Borne de recharge (Berlicum) : 

- La partie "Borne de Recharge (Berlicum)" se concentre sur le développement du logiciel embarqué pour une borne de recharge utilisée par des étudiants. Le but principal de cette borne est de permettre aux étudiants d'accéder à diverses fonctionnalités liées à leurs cartes à puce. Voici un aperçu des opérations principales que les étudiants peuvent effectuer à l'aide de cette borne :

- Afficher les Informations Personnelles nommée dans le code "affiche_info": Cette fonctionnalité permet aux étudiants d'afficher les informations personnelles stockées sur leur carte à puce. Cette fonction dans le code s'appelle "

- Consulter les Bonus nommée dans le code "affiche_bonus" : Les étudiants peuvent consulter les bonus qui leur ont été attribués, mais qui n'ont pas encore été transférés sur leur carte. Les informations sur ces bonus sont extraites de la base de données, et la colonne "type_operation" dans la table "compte" indique "Bonus" pour les bonus non transférés.

- Transférer les Bonus nommée dans le code "transfert_bonus": Les étudiants peuvent utiliser la borne pour transférer les bonus disponibles sur leur carte. Une fois que les bonus ont été transférés, la colonne "type_operation" dans la table "compte" est mise à jour pour indiquer "Bonus transféré". Il est essentiel que ces transactions respectent les propriétés ACID (Atomicité, Cohérence, Isolation et Durabilité) pour garantir l'intégrité des données.

- Consulter le crédit disponible nommée dans le code "consult_sold" : Les étudiants peuvent vérifier le solde disponible sur leur carte à puce, ce qui leur permet de suivre leurs ressources.

- Recharger le Crédit avec une Carte Bancaire nommée dans le code "recharger_carte" : Lorsqu'un étudiant a épuisé ses bonus, il a la possibilité de recharger son crédit à l'aide d'une carte bancaire. Il est important de noter que le processus de recharge avec une carte bancaire est fictif dans le cadre de ce projet, et la borne simule simplement une transaction réussie.

- Le développement du logiciel embarqué pour la borne de recharge (Berlicum) est essentiel pour offrir aux étudiants un accès facile à leurs informations, à leurs bonus et à leur crédit. Ce système contribue à la gestion efficace des ressources des étudiants, en garantissant l'intégrité des transactions et en facilitant la recharge en cas de besoin.


#### Fonctions implémentées : 

- La fonction "code pin" nommée dans le code "PINvalide" a été implémenter dans ce code pour permettre une meilleure sécurisation sur la carte à puce. Donc a chaque fois qu'un étudiant insert sa carte à puce dans la borne de recharge il devra mettre son code pin qui est défini au moment de la création de sa carte à puce.

- La fonction "Afficher l'historique des transactions" nommée dans le code "histo_transac" offre aux étudiants la possibilité de consulter un historique détaillé de toutes les transactions effectuées avec leur carte à puce. Cet historique est stocké dans une table "compte" de la base de données et peut être consulté à partir de la borne de recharge (Berlicum). Voici une description de cette fonctionnalité :

Afficher l'historique des transactions : Les étudiants peuvent accéder à un récapitulatif de toutes les transactions effectuées avec leur carte à puce. Chaque transaction est enregistrée dans la base de données avec des détails tels que la date, l'heure, le type de transaction (retrait, bonus, recharge, etc.), le montant impliqué, et d'autres informations pertinentes. L'affichage de cet historique se fait de manière claire et organisée, permettant aux étudiants de comprendre facilement leur utilisation de la carte.

#### Répartition classes et instructions :

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

### Application de simulateur de machine à café (Kuroda)

L'application Kuroda est un simulateur de machine à café implémenté en Python, utilisant une carte à puce comme moyen d'interaction. L'objectif principal est de permettre aux utilisateurs d'effectuer des transactions, telles que consulter le solde de leur compte, acheter une boisson et mettre à jour les données de leur carte à puce.

Kuroda est une application intéractive qui permet à l'utilisateur un choix de boisson variées. En effet, l'utilisateur peut acheter différentes boissons comme un café, un chocolat chaud ou un thé. 

Les principales fonctionnalités proposées par cette application sont les suivantes : 

- Consultation du Solde : L'utilisateur peut consulter le solde actuel de sa carte à puce en choisissant l'option correspondante dans le menu. L'application envoie une commande APDU à la carte pour récupérer cette information.

- Achat d'une Boisson : L'utilisateur peut acheter une boisson (café, chocolat, thé) au coût de 0.20 €. L'application vérifie d'abord si le solde de la carte est suffisant. Si oui, elle débite le montant de la carte et met à jour les données sur la carte et dans la base de données.

- Mise à Jour du Solde : Si le solde de la carte diffère de celui stocké dans la base de données, l'application met à jour le solde de la carte avec celui de la base de données. Cela garantit la cohérence des soldes entre la carte et la base de données.




## VI. Évaluation de la Sécurité et analyse des Vulnérabilités
Les logiciels de base n'étaient pas très sécurisés et comportaient plusieurs potentielles vulnérabilités. 

Une partie de sécurisation était nécessaire dans le cadre de ce projet. Nous avons pu trouver quelques vulnérabilités que nous avons résolues et d'autres vulnérabilités que l'on a recensé mais qui, par manque de temps n'ont pas étés traités. 

Dans cette partie, nous allons traiter les sécuritées supplémentaires implémentées pour chaque application pour patcher les différentes vulnérabilités : 

### Partie Vulnérabilités de Rubrovitamin :

Pour l'application Rubrovitamin, une faille principale a été détéctée concernant les fonctions d'écriture dans la mémoire EEPROM. En effet, on s'est rendu compte que l'écriture des informations personnelles nom, prénom, numéro étudiant, code PIN et PUK étaient des tâches réservées exclusivement à l'agent administratif. Par conséquent, un élève malveillant en connaissance de la table des classes et instructions aurait pu développer son propre code envoyant des APDUs pour modifier lui même ces informations. 
Pour patcher cette vulnérabilité, nous avons implémenté une fonctionnalité dans le code Rubrovitamin qui oblige l'utilisateur à rentrer le mot de passe administrateur pour pouvoir utiliser les fonctions d'écriture dans l'EEPROM utilisées pour écrire un nom, prenom, num étu, code PIN et PUK. De ce fait, sans connaître le mot de passe admin, il est impossible de personnaliser une carte sans connaître le mot de passe admin connu seulement par l'agent administratif.  

Toujours sur rubrovitamin, une étape de sécurisation contre **l'arrachement de carte** (lors d'une transaction) a été mise en place. En effet, dans le domaine des transactions sur carte à puce (opérations visant à modifier le solde) il existe un problème concernant l'arrachement de carte. Dans notre cas, imagineons que la carte soit arrachée à un moment précis pendant le processus de débit. Dans ce cas, il se peut que cet arrachement de carte ai compromis les données du solde d'arrivé et celui ci risque d'être érroné. Pour éviter ce problème, la **solution** consiste à rendre certaines opérations atomiques, indivisible : soit on arrive à tout transmettre, soit si il y a arrachement de carte au milieu d'une transaction, alors on ne transmet rien.
C'est l'implémentations des fonctions **engage()** et **valide()** dans le code qui permettent de gérer ce problème.

Toujours sur rubrovitamin, nous avons pensés à une faille supplémentaire que nous n'avons pas eu le temps de traiter. Cette faille concerne la **confidentialité** et **l'intégrité** des APDUs transmis. Les APDU peuvent contenir des informations sensibles telles que des identifiants personnels, des clés, des informations financières, etc. La confidentialité vise à empêcher que ces données ne soient compromises lors de leur transmission entre le lecteur et la carte à puce. Pour assurer la confidentialité, on peut utiliser des mécanismes de chiffrement pour rendre les données illisibles pour toute personne non autorisée qui pourrait intercepter les APDU pendant la transmission. L'intégrité quant à elle concerne la garantie que les données n'ont pas été altérées pendant la transmission. Les APDU peuvent être vulnérables à des attaques telles que la modification malveillante des données pendant leur transit. L'utilisation de mécanismes d'intégrité, tels que le hachage ou les codes d'authentification des messages, permet de détecter toute altération des données. Si les données ont été modifiées, le destinataire peut identifier cette altération et prendre des mesures appropriées.

### Partie Vulnérabilités du Logiciel de Gestion (Rodelika) :

Bien que le logiciel de gestion (Rodelika) ait été conçu pour gérer de manière efficace les cartes, les bonus, et les débits des étudiants, il est crucial de prendre en compte les possibles vulnérabilités qui pourraient compromettre la sécurité et l'intégrité des données. Voici quelques points à considérer :

Vulnérabilités liées à l'accès non autorisé :

- Si le logiciel n'implémente pas correctement les mécanismes d'authentification et d'autorisation, cela pourrait conduire à des accès non autorisés à des fonctionnalités sensibles, compromettant ainsi la confidentialité des données étudiantes.

Injection SQL :

- L'utilisation de requêtes SQL dynamiques sans les précautions nécessaires pourrait ouvrir la porte à des attaques par injection SQL. Cela pourrait permettre à un attaquant d'exécuter des commandes SQL malveillantes et d'altérer, supprimer ou récupérer des données non autorisées.

Défauts dans la validation des entrées utilisateur :

- Si le logiciel ne valide pas correctement les entrées utilisateur, cela pourrait conduire à des vulnérabilités telles que les attaques par injection, les attaques par débordement de tampon, ou d'autres formes d'attaques liées à la manipulation des données d'entrée.

### Partie Vulnérabilités de l'Application Web de Gestion (RodelikaWeb) :

Bien que l'application web de gestion (RodelikaWeb) offre une interface graphique conviviale pour les agents administratifs avec une interface de connexion pour cet admin avec un mot de passe hasher, il est essentiel de considérer les possibles vulnérabilités qui pourraient compromettre la sécurité de l'application. Voici quelques points à prendre en compte :

Injection de code SQL :

- L'utilisation de requêtes SQL dynamiques dans le code PHP sans les mesures de sécurité appropriées peut rendre l'application vulnérable aux attaques par injection SQL. Il est crucial de paramétrer et d'utiliser des requêtes préparées pour éviter ce type d'attaque.

Faiblesse dans la gestion des sessions :

- Si la gestion des sessions PHP n'est pas correctement implémentée, cela peut conduire à des vulnérabilités liées à la manipulation des sessions, telles que la fixation de session, la session hijacking ou la session poisoning. Assurez-vous d'utiliser des pratiques de gestion de session sécurisées.

Absence de chiffrement des données en transit :

- Si les données ne sont pas correctement chiffrées lors de leur transmission entre l'application web et la base de données ou entre le client et le serveur, cela peut exposer les informations sensibles à des interceptions.

Chiffrement faible des mots de passe :

- Si les mots de passe sont stockés dans la base de données sans être correctement hachés avec des algorithmes sécurisés, cela pourrait exposer les informations des utilisateurs en cas de violation de la base de données.
  
### Partie Vulnérabilités de la Borne de Recharge (Berlicum) :

Bien que le système de la borne de recharge (Berlicum) intègre des fonctionnalités de sécurité telles que l'utilisation d'un code PIN pour accéder à la borne, il reste important de noter quelques vulnérabilités potentielles qui pourraient compromettre la sécurité du système. Voici quelques points à considérer :

Attaques par force brute sur le code PIN :

- Les attaques par force brute sont possibles si les codes PIN sont relativement courts ou si la borne ne limite pas le nombre de tentatives incorrectes d'entrée du code PIN. Il est recommandé d'implémenter des mécanismes de verrouillage temporaire après un certain nombre de tentatives infructueuses.

Injection de code sur la carte à puce :

- Si la carte à puce n'est pas correctement sécurisée, un attaquant pourrait tenter d'injecter du code malveillant sur la carte, compromettant ainsi le système. Assurez-vous que la carte utilise des mécanismes de sécurité robustes pour empêcher toute altération non autorisée de son contenu.

Vulnérabilités dans les librairies utilisées :

- Les bibliothèques externes, telles que pyscard, mysql-connector, pyfiglet, et getpass, peuvent avoir des vulnérabilités connues. Il est important de maintenir ces bibliothèques à jour et de surveiller les annonces de sécurité pour s'assurer que toutes les vulnérabilités connues sont corrigées.

## VII. Conclusion


## VIII. Annexes
Tous les codes associés à chaque applications sont disponibles à la racine du github.
https://github.com/mathfern/SAE-Carotte/tree/main



