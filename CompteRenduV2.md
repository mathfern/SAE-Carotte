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
Dans le description il est possible d'insérer un texte pour expliquer le travail à effectuer, ou, comme dans notre cas, une image. Dans cette instance, nous avons inclus le planning prévisionnel des tâches :
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
##### Détails sur le type de cartes à puces utilisées pour le projet
Pour ce projet, le type de puce utilisé est une **ATMega328**. C'est un microcontrôleur 8 bits basé sur l'architecture Harvard. C'est un type de processeur qui sépare physiquement la mémoire de données et la mémoire programme. L’accès à chacune des deux mémoires s’effectue via deux bus distincts ce qui représente une amélioration des performances comparé à certaines technologies à un bus commun pour programme et données comme l'architecture Von Neumann par exemple. 

Pour en revenir au fonctionnement techniques des cartes utilisées pour le projet, voici un schéma qui détaille l'architecture utilisée par celles-ci : 
 ![schema_smartcard](https://github.com/mathfern/SAE-Carotte/assets/134608345/8d98304a-ad0b-4f05-939a-6808c7d36c3d)
![Design sans titre](https://github.com/mathfern/SAE-Carotte/assets/134608345/f07992ab-d47c-4cd9-902b-f0a815595b79)
