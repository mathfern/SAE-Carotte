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

Chaque logiciel est nommé par rapport à une variété de carotte, toujours en lien avec le nom du projet (Carotte électronique)


## III. Organisation et Gestion du projet

### 1 - Cahier des charges
L'objectif de notre projet au sein de cette SAE était de développer les logiciels suivants :
- Le programme embarqué dans la carte à puce (code nom : Rubrovitamina)
- L'application de personnalisation de carte utilisée par l'agent administratif (Lubiana)
- Le logiciel de gestion employé par l'agent administratif pour l'attribution des récompenses (Rodelika)
- Le logiciel de la borne de recharge (Berlicum)
- La base de données (Purple Dragon)

### 2 - Répartition du temps

Pour organiser notre emploi du temps, nous avons entamé le processus en énumérant toutes les tâches à accomplir. Ensuite, nous avons répertorié les compétences de chacun afin de déterminer quelles tâches nous semblaient les plus simples à réaliser. Une fois cette liste établie, nous avons élaboré un diagramme de Gantt pour nous fournir une feuille de route dans le cadre de la SAE.

![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/835c5a10-a214-49d4-b519-9b8ced94e0a7)

En suivant notre planning prévisionnel, nous avons réussi à terminer la SAE dans les délais impartis. Cependant, certaines applications, telles que Rubrovitamin, Lubiana, Rodelika (et Web), nous ont demandé plus de temps que les autres, ce qui a entraîné des retards par rapport à notre diagramme prévisionnel. Voici un diagramme illustrant le temps réel que nous avons consacré à chaque application :

![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/3c466bbe-f4f7-4a76-bf1a-b7ad3a9d1f76)

### 3 - Mise en place du GitHub

La mise en place de Git sur un système Debian 11, suivi de l'utilisation de GitHub, offre un moyen puissant de gérer les versions de code, de collaborer avec d'autres développeurs et de maintenir un historique clair des modifications apportées à un projet. Voici un résumé des étapes pour configurer Git, créer un référentiel sur GitHub, et travailler avec les commandes de base telles que git add, git commit, git push, et git pull.

Étapes :
1. Installation de Git sur Debian :

```sudo apt update``` <br>
```sudo apt upgrade``` <br>
```sudo apt install git``` <br>

2. Configuration de Git :

```git config --global user.name "Notre Nom"``` <br>
```git config --global user.email "Notre@email.com"``` <br>
```git config --list```

3. Création d'un nouveau référentiel sur GitHub :

Accédez à GitHub et créez un nouveau référentiel.

4. Configuration du Projet Local :

``` cd /chemin/vers/notre/projet ``` <br>
``` git init ``` <br>
``` git add . ``` <br>
``` git commit -m "Premier commit" ``` <br>

5. Travailler avec le Projet :
Pour récupérer les dernières modifications depuis le référentiel distant :

``` git pull origin master ```

Pour ajouter et valider les modifications locales :

``` git add . ``` <br>
``` git commit -m "Description des modifications" ``` 

Pour envoyer les modifications vers le référentiel distant :

``` git push origin master ```

Par ailleurs, le git étant en privé, il faut obligatoirement générer une clé ssh sur sa machine avec **ssh-keygen** de la manière suivante : 

``` ssh-keygen -t rsa -b 4096 -C "fernandes.mathias@gmail.com"```

S'assurer que la clé est en cours d'exécution :
``` eval "$(ssh-agent -s)"```

Ajouter la clé ssh à l'agent local SSH :
``` ssh-add -K /home/user/.ssh/id_rsa```

                                          
Conclusion :

La configuration de Git sur Debian 11 associée à GitHub offre un ensemble robuste d'outils pour la gestion des versions et la collaboration. Ces étapes, une fois suivies, nous permettent de travailler de manière efficace, de maintenir un historique précis des modifications, et de partager nos projets avec d'autres collaborateurs. L'utilisation des commandes git add, git commit, git push, et git pull facilite la gestion du cycle de vie du code. En veillant à respecter les meilleures pratiques de sécurité, ce processus garantit une expérience de développement collaborative et sécurisée.

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

- Sous tâches : <br>
Dans chaque tâche, nous avions la possibilité de créer des sous-tâches. Dans l'exemple donné, la tâche de rédaction est fragmentée en plusieurs parties, chacune correspondant à une application à rédiger.
![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/89557350-820a-4b6e-8182-0b9ad1ab87eb)

- Commentaires : <br>
En conclusion, chaque tâche dispose d'un espace commentaire qui nous a permis de suivre en temps réel l'évolution du projet. Jira a également facilité nos réunions en nous permettant de ne pas oublier les points déjà traités et d'ajouter des suggestions d'amélioration pour le futur.




## IV. Phase de Conception Initiale

### Gestion des Environnements Virtuels pour l'Installation de Modules Python

La mise en place d'environnements virtuels est une pratique essentielle dans le développement Python, permettant d'isoler les dépendances d'un projet et d'éviter les conflits entre différentes applications. Dans le cadre de notre projet, la création d'un environnement virtuel a été particulièrement utile pour installer et gérer les modules tels que pyscard et mysql-connector via pip.

Environnements Virtuels avec venv :

Création de l'Environnement Virtuel :

Utilisation de la bibliothèque standard venv pour créer un environnement virtuel.

``` python3 -m venv "dossier" ```

Activation de l'Environnement Virtuel :

``` source "dossier"/bin/activate ```

Installation de pyscard et mysql-connector via pip :

Une fois l'environnement virtuel activé, l'utilisation de pip pour installer les modules devient spécifique à cet environnement.

``` pip install pyscard mysql-connector ```

Utilisation dans le Contexte du Projet :

Dans le cadre de l'implémentation du logiciel embarqué comme pour la borne de recharge (Berlicum)et du logiciel de gestion (Rodelika), la création d'environnements virtuels a permis de garantir la disponibilité des modules requis (pyscard, swig, pyfiglet, tabulate et mysql-connector) dans des versions spécifiques, assurant ainsi la stabilité du système. 

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

#### 6. Utilisation de Rubrovitamin 

Comme expliqué précedemment, Rubrovitamin s'implémente dans la mémoire flash de la carte à puce à l'aide d'un programmateur. Il faut utiliser les commandes suivantes : 

``` make fuses ``` <br>
qui permet la configuration des fusibles lors de la 1ère programmation de la carte (à faire qu'une seule fois par carte). 

``` make progcarte ``` <br>
qui permet la programmation de la carte à puce (l'import du code Rubrovitamin en mémoire flash)

Ces deux commandes s'appuient sur le logiciel open sources AVRDUDE qui permet de programmer des microcontrôleurs de la famille AVR (comme notre carte à puce dans ce projet). 

Les principales fonctions d'AVRDUDE sont les suivantes :

- Programmation du Microcontrôleur : AVRDUDE est utilisé pour écrire le code compilé dans la mémoire flash de la carte à puce. 

- Lecture du Microcontrôleur : AVRDUDE permet de lire le contenu de la mémoire de la carte à puce

- Configuration des Fusibles : Les microcontrôleurs AVR ont des fusibles qui déterminent divers paramètres de configuration, tels que la fréquence d'horloge, l'activation de la protection en écriture, etc. AVRDUDE permet de configurer ces fusibles.

Ici voici un exemple de l'utilisation de rubrovitamin :

![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/15dc35fc-8d2e-4fa0-bd03-f1945691036e)

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
     fonction print_version()

     ![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/f4e907c9-a12b-45be-bb9a-2923aa1a4052)


2. **Affichage des données de la carte à puce :**
   - Vérifie et affiche les données telles que le nom, le prénom et le numéro d'étudiant sur la carte. Si aucune donnée n'est présente, indique que la carte est vierge.
     fonction print_data()

![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/9ce47349-255f-43a1-8da9-eb3430ccf51a)


3. **Attribuer la carte à un étudiant :**
   - Permet d'ajouter le nom, le prénom et le numéro d'étudiant sur la carte.
     fonction assign_card()

     ![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/3c7566e0-2e4a-49dc-abfa-34c0b296eff0)


4. **Mettre le solde initial de 0.00€ :**
   - Initialise le solde de la carte à 0.00€.
     fonction init_sold()

![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/4f802174-6ae3-42e0-9c10-f86c6bcc0164)

5. **Consulter le solde :**
   - Affiche le solde actuel sur la carte.
     fonction consult_sold()

    ![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/c9ff52e9-e7b2-4e92-afa6-709375928781)


6. **Réinitialiser les données de la carte :**
   - Supprime les données de la carte, nécessaire en cas de réattribution.
     fonction delete_data()

     ![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/f279b706-ba92-4685-9218-89779867a2c0)


7. **Attribuer code PIN/PUK :**
   - Permet de définir un nouveau code PIN et génère un code PUK aléatoire.
     fonctions codePIN() et codePUK()
![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/62f3ccb0-7c78-480c-9cdb-7515694b8ff3)

8. **Consulter le code PUK :**
   - Affiche le code PUK actuel.
     fonction consult_PUK()
![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/71f33c31-38e2-4410-b780-553de9c23677)

9. **Modifier le code PIN :**
   - En cas d'oubli, permet de modifier le code PIN en utilisant le code PUK.
     fonction modifPIN()
![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/56a2ec2b-6a2d-4f01-8a13-69918a047a01)


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
En effet, elle utilise les variables sw1 et sw2 pour stocker les codes d'erreurs 0x90 pour sw1 et 0x6X pour sw2


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

- Ajout d'une table admin avec les colonnes admin_id, nom et mot de passe en hash Bcrypt dans la base de données, ce qui permet d'avoir une authentification sur la version web de Rodelika. Cela fait en sorte que tout le monde ne puisse pas accéder à la base de données et la modifier. 

- Ajout des colonnes etu_solde, etu_bonus dans la table étudiant pour permettre de stocker ces informations pour chaque étudiant.
  
#### Programmation

La base de données Purpledragon a été développée à l'aide du langage sql. 

#### Vulnérabilités et solutions :

Les bases de données MySQL sont sujettes à plusieurs vulnérabilités potentielles qui peuvent mettre en danger la sécurité de vos données. Voici quelques-unes des vulnérabilités courantes et des mesures pour y remédier :

1. **Injection SQL :** Les attaques par injection SQL sont l'une des vulnérabilités les plus courantes. Les attaquants insèrent du code SQL malveillant dans les requêtes pour accéder, modifier ou supprimer des données. Pour y remédier :
   - Utilisez des requêtes préparées ou des procédures stockées pour éviter l'injection SQL.
   - Assurez-vous de filtrer et de valider toutes les données utilisateur avant de les utiliser dans des requêtes SQL.

2. **Authentification faible :** Une authentification faible, des mots de passe faibles ou l'utilisation de comptes par défaut peuvent faciliter l'accès non autorisé à la base de données. Pour y remédier :
   - Utilisez des mots de passe forts et encouragez une politique de gestion des mots de passe.
   - Limitez l'accès en fonction des principes du moindre privilège, en n'accordant que les autorisations nécessaires à chaque utilisateur.
  
   Et voici la base de données qu'on a utilisé :

    On a ici la table Etudiant avec notamment le solde et les bonus ainsi que les étudiants :
   
   ![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/2748e9a6-ec5e-4390-b02c-e2c74063dadc)

   Puis on a la table Compte qui va stockées les transactions de chaque étudiant :

   ![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/435cbd90-3066-4cad-8e76-f035148917e4)

   On aura ici la table Admin avec le nom d'utilisateur et le mot de passe hashé pour acceder à RodelikaWeb :

   ![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/c5f386d5-a5c8-4872-a695-e30855afb9ef)

   Et puis on a la table Type avec les différents types d'opérations :

   ![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/03d68a7b-ca50-4897-9a0c-bd148e35e39a)


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
  
  ![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/3788ae15-565a-4617-b0d1-2071145250b2)

- L’option 2 "solde des étudiants" nommée dans le code "get_list_student_with_sold" permettra d’afficher le solde total de chaque étudiant.
  
  ![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/0706857f-2e1a-4251-85cd-51c6242a1937)

- L’option 3 "saisir un nouvel étudiant" nommée dans le code "new_student" permettra d’attribuer une nouvelle carte à un étudiant. Elle ne permet pas la personnalisation de la carte. Elle se fait via le logiciel Lubiana.
  
![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/c85a498c-8808-44dc-a8c8-b620ef3e7e7c)

- L’option 4 "attribuer un bonus à un étudiant" nommée dans le code "add_bonus" permettra à l’agent administratif lorsqu’il reçoit un email d’un enseignant d’attribuer un bonus. Le mail doit contenir le numéro de l’étudiant. Dans le cas contraire, l’agent administratif doit effectuer une recherche par nom et prénom avec l’option 1.
  
  ![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/913fc5dd-dafa-4831-b982-e51f8835ffb4)


#### Fonction implémentées :

- L'option 5 "supprimer un étudiant" nommée dans le code "suppr_etudiant" permettra à l'agent administratif de supprimer un étudiant de la base de données.
  
![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/82066ab0-29af-4b6b-b7b2-c1298f8b094d)

#### Programmation :

L’application Rodelika sera développée avec Python. En connexion avec la base de données PurpleDragon. Pour communiquer avec la base de données MySql nous allons installer les librairies Python suivantes :

- mysql-connector
- tabulate
- pyfiglet

### Application web de gestion (RodelikaWeb)

L’application web de gestion donne la possibilité à l’agent administratif d’avoir une interface graphique qui permet l’utilisation plus interactive du logiciel de gestion Rodelika.

Ce site sera codé en HTML/CSS, PHP et javascript et fera appel à la base de données PurpleDragon ainsi qu'à l'application Rodelika.


#### Fonctionnalités implémentées <br>
Pour démarrer RodelikaWeb, il vous suffit de vous rendre dans le répertoire SAE-Carotte/RodelikaWeb/ et d'exécuter la commande "php -S localhost:8000". Cette commande lance un serveur web local utilisant PHP sur le port 8000. Ensuite, ouvrez simplement un navigateur web et accédez à "http://localhost:8000". Vous serez dirigé vers l'interface de connexion où vous devrez saisir votre identifiant et votre mot de passe.<br>

- Nous avons ajouté une interface graphique pour chaque fonction afin que l'agent administratif puisse effectuer les manipulations plus facilement et de manière plus interactive :
![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/96ac695c-26a5-4bf3-857e-296bb782ac22)
- liste des étudiants :<br>
Le programme Web utilise la fonctionnalité 1 du script Rodelika pour afficher les informations telles que le numéro étudiant, le nom et le prénom de l'étudiant.
![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/3327e21c-cb03-4e29-b3be-eff83bfcba6e)


- liste des étudiants avec le solde et bonus:<br>
De même que précédemment, nous allons utiliser l'option 2 de Rodelika pour afficher les informations incluant le numéro étudiant, le nom, le prénom, le solde et les bonus de l'étudiant.
![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/83a7baa0-55cf-4547-befb-7c2451592d5a)


- ajouter un nouvel étudiant : <br>
Dans cette instance, nous utiliserons l'option 3 de Rodelika. En saisissant un numéro étudiant, un nom et un prénom, nous pourrons ajouter un nouvel étudiant. Une vérification sera effectuée pour s'assurer que le numéro étudiant comporte bien 8 chiffres et qu'il n'existe pas déjà dans la base de données.
![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/3b6b896a-3938-4670-bfd6-9f505d2145b1)

- attribuer un bonus :<br>
Pour attribuer un bonus, il vous suffira d'entrer un numéro étudiant existant dans la base de données (une vérification sera effectuée). Ensuite, le compte étudiant associé à ce numéro se verra ajouter un bonus (le bonus de base étant de +1,00€). Cette opération s'effectue en utilisant la fonction 4 de Rodelika.
![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/0e1be92b-c83e-4784-81d2-34ab7cbf210e)


- supprimer un étudiant :<br>
Enfin, la dernière fonctionnalité de notre site consiste à supprimer un étudiant existant dans la base de données. Pour ce faire, il vous suffit d'entrer un numéro étudiant. Une fois la vérification effectuée, l'étudiant associé à ce numéro sera supprimé. Cette opération utilise la fonctionnalité ajoutée à Rodelika, à savoir l'option 5.
![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/b4cca0a3-e16b-40d5-acee-99e61978565a)


- interface de connexion pour l’agent administratif pour sécuriser l’ajout de soldes dans la bdd :
![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/aca45aa2-4618-4722-aa89-667ac27c362a)


- Chaque formulaire ou tableau est accompagné de son propre message d'erreur et de succès. Voici un exemple de message qui s'affiche lors de l'ajout d'un bonus.
![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/42b570e4-3a98-4338-9de8-c7d560144eb1) <br>

- Un exemple de message qui s'affiche lors d'une erreur d'ajout de bonus :
![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/b2e48e1d-0da4-49d5-bc1a-9be5856bcb77)


### Borne de recharge (Berlicum) : 

- La partie "Borne de Recharge (Berlicum)" se concentre sur le développement du logiciel embarqué pour une borne de recharge utilisée par des étudiants. Le but principal de cette borne est de permettre aux étudiants d'accéder à diverses fonctionnalités liées à leurs cartes à puce. Voici un aperçu des opérations principales que les étudiants peuvent effectuer à l'aide de cette borne :

- Afficher les Informations Personnelles nommée dans le code "affiche_info": Cette fonctionnalité permet aux étudiants d'afficher les informations personnelles stockées sur leur carte à puce.

  ![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/e319c039-d4c6-4d63-ae98-d944bbe8507e)


- Consulter les Bonus nommée dans le code "affiche_bonus" : Les étudiants peuvent consulter les bonus qui leur ont été attribués, mais qui n'ont pas encore été transférés sur leur carte. Les informations sur ces bonus sont extraites de la base de données, et la colonne "type_operation" dans la table "compte" indique "Bonus" pour les bonus non transférés.

  ![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/e8134883-9795-4243-9747-7fe8233b0624)

- Transférer les Bonus nommée dans le code "transfert_bonus": Les étudiants peuvent utiliser la borne pour transférer les bonus disponibles sur leur carte. Une fois que les bonus ont été transférés, la colonne "type_operation" dans la table "compte" est mise à jour pour indiquer "Bonus transféré". Il est essentiel que ces transactions respectent les propriétés ACID (Atomicité, Cohérence, Isolation et Durabilité) pour garantir l'intégrité des données.

![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/1d3e10aa-6252-49a6-a5e8-763b29b71b3e)

- Consulter le crédit disponible nommée dans le code "consult_sold" : Les étudiants peuvent vérifier le solde disponible sur leur carte à puce, ce qui leur permet de suivre leurs ressources.

  ![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/79307f37-0f1d-4155-b8f3-0e29d0eb97f5)

- Recharger le Crédit avec une Carte Bancaire nommée dans le code "recharger_carte" : Lorsqu'un étudiant a épuisé ses bonus, il a la possibilité de recharger son crédit à l'aide d'une carte bancaire. Il est important de noter que le processus de recharge avec une carte bancaire est fictif dans le cadre de ce projet, et la borne simule simplement une transaction réussie.

  ![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/6aa1a588-6c65-45e3-9e13-1a6f43083554)


- Le développement du logiciel embarqué pour la borne de recharge (Berlicum) est essentiel pour offrir aux étudiants un accès facile à leurs informations, à leurs bonus et à leur crédit. Ce système contribue à la gestion efficace des ressources des étudiants, en garantissant l'intégrité des transactions et en facilitant la recharge en cas de besoin.


#### Fonctions implémentées : 

- La fonction "code pin" nommée dans le code "PINvalide" a été implémenter dans ce code pour permettre une meilleure sécurisation sur la carte à puce. Donc a chaque fois qu'un étudiant insert sa carte à puce dans la borne de recharge il devra mettre son code pin qui est défini au moment de la création de sa carte à puce.

- La fonction "Afficher l'historique des transactions" nommée dans le code "histo_transac" offre aux étudiants la possibilité de consulter un historique détaillé de toutes les transactions effectuées avec leur carte à puce. Cet historique est stocké dans une table "compte" de la base de données et peut être consulté à partir de la borne de recharge (Berlicum). Voici une description de cette fonctionnalité :

  ![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/2af2c990-b136-4ed0-84b7-e6ccf88a7187)

Afficher l'historique des transactions : Les étudiants peuvent accéder à un récapitulatif de toutes les transactions effectuées avec leur carte à puce. Chaque transaction est enregistrée dans la base de données avec des détails tels que la date, l'heure, le type de transaction (retrait, bonus, recharge, etc.), le montant impliqué, et d'autres informations pertinentes. L'affichage de cet historique se fait de manière claire et organisée, permettant aux étudiants de comprendre facilement leur utilisation de la carte.


#### Répartition classes et instructions :

La classe utilisée par berlicum sera la classe 0x80, 0x81 de l’API du projet (cf partie Carte à Puces). 

Chaque opération réalisable par le logiciel sera associée à une instruction de la classe 0x81, 0x80 : . 

- Instruction pour l’*affichage des informations personnelles* : instruction 0x01 et classe 0x80 + Requete BDD
- Instruction pour l’*attribution des bonus sur la carte* :  Requete BDD
- Instruction pour l’*affichage des crédits disponibles sur la carte* : instruction 0x07 et classe 0x80
- Instruction pour l’*attribution d’argent sur la carte* : | classe 0x80 instruction 0x08
- Instruction pour l'affichage de l'historique de transaction* : Requete BDD

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

![image](https://github.com/mathfern/SAE-Carotte/assets/150122701/3469a959-4266-4399-bd53-09bcd6be3c26)

- Mise à Jour du Solde : Si le solde de la carte diffère de celui stocké dans la base de données, l'application met à jour le solde de la carte avec celui de la base de données. Cela garantit la cohérence des soldes entre la carte et la base de données.

#### Répartition classes et instructions :

La classe utilisée par kuroda sera la classe 0x80, 0x81 de l’API du projet (cf partie Carte à Puces). 

Chaque opération réalisable par le logiciel sera associée à une instruction de la classe 0x81, 0x80 : . 

- Instruction pour l’*affichage du solde* : instruction 0x07 et classe 0x80
- Instruction pour l’*débiter le solde* :  Requete BDD + instructions 0x07, 0x08, 0x04 de la classe 0x80
- Instruction pour *mettre le solde de la BDD sur celui de la carte* : instruction 0x08 et classe 0x80

#### Programmation : 

Berlicum sera développé en utilisant Python 3.11. Les librairies utilisées par Berlicum sont : 
- pyscard
- mysql-connector
- pyfiglet
- getpass


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

### Partie Vulnérabilités pour la Base de Données PurpleDragon :

Injection SQL :

- Vulnérabilité : Les attaques par injection SQL peuvent se produire si des requêtes SQL dynamiques ne sont pas correctement sécurisées.

- Solution : Utilisez des requêtes préparées ou des procédures stockées pour éviter l'injection SQL. Validez et filtrez toutes les données utilisateur avant de les incorporer dans des requêtes SQL.

Authentification faible :

- Vulnérabilité : L'utilisation de mots de passe faibles ou d'identifiants par défaut peut rendre l'accès à la base de données plus facile.

- Solution : Utilisez des mots de passe forts, encouragez la rotation régulière des mots de passe, et limitez l'accès en fonction du principe du moindre privilège. Évitez l'utilisation d'identifiants par défaut.

Accès non autorisé :

- Vulnérabilité : Les comptes avec des autorisations excessives peuvent permettre un accès non autorisé ou des modifications indésirables.

- Solution : Appliquez le principe du moindre privilège en accordant à chaque utilisateur uniquement les autorisations nécessaires pour effectuer ses tâches. Révisez régulièrement les autorisations.

Chiffrement faible des mots de passe :

- Vulnérabilité : Le stockage de mots de passe sans cryptage adéquat peut compromettre la sécurité des utilisateurs.

- Solution : Utilisez des algorithmes de hachage sécurisés (comme Bcrypt) pour stocker les mots de passe. Encouragez également l'utilisation de mots de passe forts.

### Partie Vulnérabilités du Logiciel de Gestion (Rodelika) :

Le logiciel de gestion (Rodelika) ait été conçu pour gérer de manière efficace les cartes, les bonus, et les débits des étudiants, il est crucial de prendre en compte les possibles vulnérabilités qui pourraient compromettre la sécurité et l'intégrité des données. Voici quelques points à considérer :

Vulnérabilités liées à l'accès non autorisé :

- Si le logiciel n'implémente pas correctement les mécanismes d'authentification et d'autorisation, cela pourrait conduire à des accès non autorisés à des fonctionnalités sensibles, compromettant ainsi la confidentialité des données étudiantes.

Injection SQL :

- L'utilisation de requêtes SQL dynamiques sans les précautions nécessaires pourrait ouvrir la porte à des attaques par injection SQL. Cela pourrait permettre à un attaquant d'exécuter des commandes SQL malveillantes et d'altérer, supprimer ou récupérer des données non autorisées.

Défauts dans la validation des entrées utilisateur :

- Si le logiciel ne valide pas correctement les entrées utilisateur, cela pourrait conduire à des vulnérabilités telles que les attaques par injection, les attaques par débordement de tampon, ou d'autres formes d'attaques liées à la manipulation des données d'entrée.

### Partie Vulnérabilités de l'Application Web de Gestion (RodelikaWeb) :

L'application web de gestion (RodelikaWeb) offre une interface graphique conviviale pour les agents administratifs avec une interface de connexion pour cet admin avec un mot de passe hasher, il est essentiel de considérer les possibles vulnérabilités qui pourraient compromettre la sécurité de l'application. Voici quelques points à prendre en compte :

Injection de code SQL :

- L'utilisation de requêtes SQL dynamiques dans le code PHP sans les mesures de sécurité appropriées peut rendre l'application vulnérable aux attaques par injection SQL. Il est crucial de paramétrer et d'utiliser des requêtes préparées pour éviter ce type d'attaque.

Faiblesse dans la gestion des sessions :

- Si la gestion des sessions PHP n'est pas correctement implémentée, cela peut conduire à des vulnérabilités liées à la manipulation des sessions, telles que la fixation de session, la session hijacking ou la session poisoning. Assurez-vous d'utiliser des pratiques de gestion de session sécurisées.

Absence de chiffrement des données en transit :

- Si les données ne sont pas correctement chiffrées lors de leur transmission entre l'application web et la base de données ou entre le client et le serveur, cela peut exposer les informations sensibles à des interceptions.

Chiffrement faible des mots de passe :

- Si les mots de passe sont stockés dans la base de données sans être correctement hachés avec des algorithmes sécurisés, cela pourrait exposer les informations des utilisateurs en cas de violation de la base de données.
  
### Partie Vulnérabilités pour les applications Berlicum et Kuroda:

La borne de recharge (Berlicum) intègre des fonctionnalités de sécurité telles que l'utilisation d'un code PIN pour accéder à la borne, il reste important de noter quelques vulnérabilités potentielles qui pourraient compromettre la sécurité du système. Voici quelques points à considérer :

Attaques par force brute sur le code PIN :

- Les attaques par force brute sont possibles si les codes PIN sont relativement courts ou si la borne ne limite pas le nombre de tentatives incorrectes d'entrée du code PIN. Il est recommandé d'implémenter des mécanismes de verrouillage temporaire après un certain nombre de tentatives infructueuses.

Injection de code sur la carte à puce :

- Si la carte à puce n'est pas correctement sécurisée, un attaquant pourrait tenter d'injecter du code malveillant sur la carte, compromettant ainsi le système. Assurez-vous que la carte utilise des mécanismes de sécurité robustes pour empêcher toute altération non autorisée de son contenu.

Vulnérabilités dans les librairies utilisées :

- Les bibliothèques externes, telles que pyscard, mysql-connector, pyfiglet, et getpass, peuvent avoir des vulnérabilités connues. Il est important de maintenir ces bibliothèques à jour et de surveiller les annonces de sécurité pour s'assurer que toutes les vulnérabilités connues sont corrigées.

## VII. Partie infrastructure

Une partie supplémentaire a été effectuée, il s'agit de la mise en place d'une infrastructure réseaux mettant en lien 5 machines virtuelles. 

Chaque membre du groupe heberge une machine virtuelle sur le même réseau. Chaque machine possède une IP fixe et chaque machine héberge une application du projet. 

Plan d'adressage IP : 

| Nom               | Adresse IP     | Service                     |
|-------------------|----------------|-----------------------------|
| PurpleDragon/RodelikaWeb      | 192.168.240.10   | MySQL, Apache               |
| Lubiana           | 192.168.240.14   |                             |
| Berlicum          | 192.168.240.11  |                             |
| Kuroda            | 192.168.240.13   |                             |
| Rodelika          | 192.168.240.12   |                |

Schéma de l'infrastructure globale du projet : 

![infra](https://github.com/mathfern/SAE-Carotte/assets/134608345/2ffacef0-7346-4650-ab88-544d2aaa6891)


Certaines de ces machines virtuelles auront des fonctionnalités particulières : 

La machine qui héberge purple dragon et rodelika web devra héberger un service web apache pour pouvoir héberger Rodelika Web à l'adresse 192.168.240.10
PurpleDragon devra héberger un service mysql pour pouvoir héberger la base de données purpledragon1 à l'adresse 192.168.240.10.

Un serveur de supervision est aussi implémenté sur la machine PurpleDragon/Rodelika Web. En effet, on a hebergé une instance de zabbix qui permet de superviser notre infrastructure.  

Les hôtes supervisés par le serveur de supervision sont : 
- Lubiana, le serveur de supervision devrait pouvoir vérifier que cette machine répond bien au ping
- Berlicum, le serveur de supervision devrait pouvoir vérifier que cette machine répond bien au ping
- Kuroda, le serveur de supervision devrait pouvoir vérifier que cette machine répond bien au ping
- PurpleDragon/Rodelika Web, le serveur de supervision devrait pouvoir vérifier que cette machine répond bien au ping et que les services de MySql et Apache fonctionnent correctement sur la machine.
- Rodelika, le serveur de supervision devrait pouvoir vérifier que cette machine répond bien au ping

### Mise en place du serveur de supervision : 

Pour mettre en place le serveur Zabbix de supervision, voici la procédure que nous avons suivi : 
Procédure sur le site officiel de zabbix : 
https://www.zabbix.com/fr/download?zabbix=6.0&os_distribution=debian&os_version=12&components=server_frontend_agent&db=mysql&ws=apache

Installation du repository Zabbix : <br>
``` wget https://repo.zabbix.com/zabbix/6.0/debian/pool/main/z/zabbix-release/zabbix-release_6.0-5+debian12_all.deb ``` <br>
``` dpkg -i zabbix-release_6.0-5+debian12_all.deb ``` <br>
``` apt update ``` <br>

Installation des packages Zabbix Server (mysql), frontend php, configuration apache pour zabbix, et zabbix agent : <br>
``` apt install zabbix-server-mysql zabbix-frontend-php zabbix-apache-conf zabbix-sql-scripts zabbix-agent ``` <br>

Création de la base de données initiale Zabbix : <br>
``` mysql -u root -p ``` <br>
``` mysql> create database zabbix character set utf8mb4 collate utf8mb4_bin; ``` <br>
```  create user zabbix@localhost identified by 'password'; ``` <br>
``` grant all privileges on zabbix.* to zabbix@localhost; ``` <br> 
``` set global log_bin_trust_function_creators = 1; ```

Importation du schéma de la BDD et les données initiales (fournies par zabbix directement) sur l'hôte du Zabbix serveur : <br>
``` zcat /usr/share/zabbix-sql-scripts/mysql/server.sql.gz | mysql --default-character-set=utf8mb4 -uzabbix -p zabbix ```

Désactivation de l'option log_bin_trust_function_creators : <br>
```  set global log_bin_trust_function_creators = 0; ```

Dans le fichier : /etc/zabbix/zabbix_server.conf définir le mot de passe de la base de données : <br>
``` DBPassword=password ```


restart le serveur apache

### Installation des agents Zabbix sur tous les hôtes que l'on souhaite superviser :

Comme expliqué précedemment, les machines qui devront être supervisées par notre serveur zabbix sont les machines qui contient les applications : Lubiana, Kuroda, Berlicum, Rodelika. 

Le type de supervision que l'on a choisi pour notre infrastructure est une supervision par agent (on utilisera l'agent zabbix).

Les agents Zabbix doivent par conséquent être installés sur toutes ces machines. Voici la procédure officielle de Zabbix pour cette installe : 
https://www.zabbix.com/fr/download?zabbix=6.0&os_distribution=debian&os_version=12&components=agent&db=&ws=

Installation du repository Zabbix : <br>
``` wget https://repo.zabbix.com/zabbix/6.0/debian/pool/main/z/zabbix-release/zabbix-release_6.0-5+debian12_all.deb ``` <br>
``` dpkg -i zabbix-release_6.0-5+debian12_all.deb ``` <br>
``` apt update ```

Installation du paquet zabbix-agent : <br>
``` apt install zabbix-agent ```

Restart du service zabbix agent : <br>
``` systemctl restart zabbix-agent ```

Activation de l'option de démarrage du service au démarrage de la machine : <br>
``` systemctl enable zabbix-agent ```


### Configuration des bases de données PurpleDragon et Zabbix :

Etant donné que les bases de données PurpleDragon et Zabbix sont hebergées sur une machine qui doit être accessible à distance, il ne faut pas oublier de configurer les bases de données de manière à créer un compte qui est autorisé a communiquer avec cette base de donnée locale depuis les IP des machines virtuelles Lubiana, Rodelika, Berlicum et Kuroda. Pour ce faire, voici comment on peut procéder : 

Depuis la machine qui heberge la base de données :

Création d'un utilisateur : 
``` CREATE USER 'user'@'IP_MACHINE_A_SUPERVISER' IDENTIFIED BY 'mot_de_passe'; ```

Donner les privilèges pour accéder à la base de données Zabbix et PurpleDragon à distance : 
``` GRANT ALL PRIVILEGES ON zabbix.* TO 'user'@'adresse_IP_machine'; ``` <br>
``` GRANT ALL PRIVILEGES ON purpledragon1.* TO 'user'@'IP_MACHINE_A_SUPERVISER'; ```

Conformément à notre infrastructure, on doit faire en sorte que Kuroda, Berlicum et Rodelika puissent communiquer avec la base de données PurpleDragon. 
Pour ce qui est de zabbix, toutes les machines doivent accéder à la base de données pour pouvoir être référencées dans les machines supervisées. 
Il faudra donc gérer les droits des utilisateurs en conséquence.


### Supervision Zabbix :

![supervision](https://github.com/mathfern/SAE-Carotte/assets/134608345/296d39f7-5084-41a9-bcaf-1124c9c313a3)
Screenshot des machines supervisées par Zabbix

On a rencontré un problème lors de la mise en place de l'outil de supervision Zabbix, on s'est rendu compte que la seule machine supervisée par Zabbix était la machine host qui héberge la base de données Zabbix et PurpleDragon. Après avoir effectué des recherches, on s'est rendu compte que c'était un problème de flux, en effet, les machines distantes n'arrivaient pas à communiquer avec la base de données Zabbix, probablement à cause d'une règle de firewall sur les machines distantes. Nous n'avons pas réussi à régler ce problème dans le temps imparti mais on peut noter qu'il s'agit d'une amélioration à développer dans notre infrastructure. 


### Axes de sécurisation de l'infrastructure : 

Il serait intéressant de sécuriser la partie infrastructure de notre projet en installant un pare-feu sur la machine PurpleDragon qui aurait des règles acceptant seulement les requêtes des machines Berlicum, Rodelika et Kuroda sur le port mysql : 3306. 

Il serait également intéressant de répliquer certaines machines virtuelles comme la machine de base de données et le serveur web (PurpleDragon et Rodelika) pour augmenter la disponibilité de l'infrastructure et renforcer la résilience. De ce fait, si une de ces deux machines tombe en panne, une bascule automatique vers l'instance répliquée devrait se faire pour réduire les délais de panne temporairement.

## VIII. Conclusion
Cette SAE et les cours qui allaient avec nous ont permis d'avoir une première approche de la carte à puce et de nous familiariser avec l'utilisation de celle-ci. Nous avons pu comprendre comment implémenter des programmes et les lire sur une carte à puce, à l'aide du programmeur et du lecteur, et la sécuriser.

Du côté gestion de projet, nous avons pu utiliser des logiciels nous permettant de nous faciliter la gestion de projet et aussi de communiquer entre nous par le biais de réunions tous les mercredi et vendredi. 

Cette SAE nous a permis de refaire de la programmation et de l'algorithmique et aussi de collaborer en équipe avec chacun des membres du groupe. 

## IX. Annexes
Tous les codes associés à chaque applications sont disponibles à la racine du github.
https://github.com/mathfern/SAE-Carotte/tree/main

Installation de zabbix :
https://www.zabbix.com/fr/download?zabbix=6.0&os_distribution=debian&os_version=12&components=agent&db=&ws=
https://www.zabbix.com/fr/download?zabbix=6.0&os_distribution=debian&os_version=12&components=server_frontend_agent&db=mysql&ws=apache

Répertoire de la SAE : 
https://perso.halim.info/iut/RT/SAE/SAE_3_12/

Répertoire des cours associés à la SAE :
https://perso.halim.info/iut/RT/SAE/SAE_3_12/carte_ap/

Sujet en pdf :
https://perso.halim.info/iut/RT/SAE/SAE_3_12/SAE_concevoir_realiser_carte_a_puce.pdf




