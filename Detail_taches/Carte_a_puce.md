## La carte à puce (Rubrovitamin)

### 1- Qu'est-ce qu'une carte à puce ? 
La carte à puce est un élément essentiel pour la vie quotidienne de millions de personnes. En effet, on la trouve partout autour de nous (carte bancaire, carte d’identité, carte vitale…). 
L’intérêt de la carte à puce est de contenir des données (stockées dans sa mémoire) et de les protéger contre toute modification indésirable. 

### 2- Projet carotte électronique
Dans le cas de notre SAE, nous allons configurer une carte à puce, nommée Rubrovitamin, dans le cadre du projet confidentiel nommé “La Carotte électronique”. Ce projet consiste à accorder des crédits supplémentaires (1€) aux élèves méritants en réalisant un système de porte-monnaie électronique à base de cartes à puce. 

Ces crédits pourront ensuite être utilisés dans des distributeurs de boissons chaudes (café, thé, chocolat chaud) pour le prix de 20 centimes, cela signifie qu’un crédit accordé à un étudiant permet de lui offrir 5 boissons. 

Les étudiants devront se rendre dans le bureau administratif de l’IUT pour récupérer leurs cartes à puce et faire des réclamations en cas de problèmes de ces dernières. Quand un étudiant se présente pour la première fois afin de récupérer sa carte, l’agent administratif vérifie l’identité de l’étudiant (carte étudiant ou certificat de scolarité), puis personnalise une carte pour lui (numéro étudiant, nom, prénom, solde à 0€). L’étudiant récupère ensuite sa carte et est inscrit sur le logiciel de gestion de cartes à puces. 

Pour inciter les étudiants à venir récupérer leurs cartes, on leur attribue d’office un bonus d’un crédit (1€) qu’il faudra aller récupérer sur la borne de recharge. 

### 3- Classes et instructions de Rubrovitamin
Voici, ci-dessous un tableau résumant les classes et instructions qui seront implémentées dans la carte à puce : 
![image](https://github.com/mathfern/SAE-Carotte/assets/150126396/57f30f96-5de8-4d6a-a788-e048a531f0ec)
La classe 0x81 est celle de la personnalisation, elle permet à l’agent administratif de : <ul>
<li>consulter la version de l’application (instruction 0x00)</li>
<li>Entrer les données d’un étudiant (instruction 0x01)</li>
<li>Consulter les étudiants ayant une carte à puce (instruction 0x02)</li>
</ul>
La classe 0x82 est celle de la gestion de paiement, elle permet à l’étudiant de : <ul>
<li>Lire le solde de la carte (instruction 0x01)</li>
<li>Ajouter un solde de 1.00€ (instruction 0x02)</li>
<li>Acheter une boisson à 20cts (instruction 0x03)</li>
</ul>
La classe 0x81 sera écrite dans l’EEPROM (car ces données ne bougent pas) et la 0x82 sera écrite dans la RAM. 

La carte à puce ne fait rien par elle-même mais il faut quand même y ajouter les classes et instructions pour que les logiciels puissent faire leur requêtes et que la carte réponde aux requêtes (en affichant la réponse). 

### 4- Idées de fonctionnalités à ajouter\modifier pour Rubrovitamin 
Nous avons pensé à séparer les bonus de l’argent provenant des cartes bancaires, pour cela nous avons créé une classe différente, la classe 0x83 qui gère les bonus. On peut donc: <ul>
<li>Lire le solde de bonus (instruction 0x01)</li>
<li>Ajouter un bonus à un élève (instruction 0x02 pour l’agent administratif)</li>
<li>Transférer les bonus obtenus sur la carte (instruction 0x03)</li>
</ul>
Nous avons aussi pensé à modifier l’instruction 0x02 de la classe 0x82 afin que l’étudiant puisse choisir la somme qu’il veut ajouter sur sa carte. Nous allons donc utiliser le paramètre P1 qui indiquera la valeur ajoutée par l’étudiant à partir de sa carte bancaire. 
Voici le tableau des classes et instructions mis à jour : 
![image](https://github.com/mathfern/SAE-Carotte/assets/150126396/811b870c-2d98-465c-8938-2f7a0fda1d69)

### 5- Vulnérabilités
La vulnérabilité qui peut se présenter au niveau des cartes à puce est physique : si l’élève perd ou se fait voler sa carte. Il suffira donc à l’étudiant d’aller voir l’agent administratif pour qu’il bloque la possibilité de faire des transactions à partir de cette carte. 
