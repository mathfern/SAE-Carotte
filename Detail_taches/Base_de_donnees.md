## Purple Dragon (Base de données)

### 1 - Concept de base de donnée carte à puce

Une base de données (purple dragon) implémenter en mysql pour les cartes à puce est une base de données utilisée pour stocker des informations liées aux cartes à puce :

- Les données des étudiants comme le numéro d’étudiant et contient uniquement les informations essentielles, à savoir le nom et le prénom. 

- Les données du compte qui  représente les opérations effectuées par les utilisateurs, elle est identifiée par la date de l’opération, et contient deux autres 
  champs, le montant de l’opération et sa description. Étant donné que plusieurs utilisateurs peuvent effectuer simultanément différentes opérations, nous avons 
  choisi d'associer le numéro d'étudiant à la clé primaire en utilisant une relation relative (R). Le montant de l'opération peut être positif en cas de bonus ou 
  de crédit, ou négatif en cas de débit.

- Les données du type de l’opération qui permet de catégoriser les types d'opérations : Bonus, Bonus transféré, Crédit et Débit.


Le schémas relationnel (MCD) proposé est donné ci-après : 

![image](https://github.com/mathfern/SAE-Carotte/assets/150126517/3a7f34bb-3c22-4650-a28d-bbfdfdd74d67)

Cette base de données devra être accessible par le logiciel de gestion Rodelika afin de permettre à l’agent administratif de gérer le suivi des cartes, des bonus, des débit etc. L’étudiant a chaque fois qu’il va insérer sa carte à puces les données de la carte à puces seront stockées dans la base de données.

Chaque étudiant partira de base avec 1 euro qu'il devra récuperer sur la borne de recharge pour en profiter.

### 2 - Idéé de données a rajouter pour la base de données

- Dans la table étudiant on a décider de rajouter un champ date de naissance.
  
### 3 - Vulnérabilités et solutions

Les bases de données MySQL sont sujettes à plusieurs vulnérabilités potentielles qui peuvent mettre en danger la sécurité de vos données. Voici quelques-unes des vulnérabilités courantes et des mesures pour y remédier :

1. **Injection SQL :** Les attaques par injection SQL sont l'une des vulnérabilités les plus courantes. Les attaquants insèrent du code SQL malveillant dans les requêtes pour accéder, modifier ou supprimer des données. Pour y remédier :
   - Utilisez des requêtes préparées ou des procédures stockées pour éviter l'injection SQL.
   - Assurez-vous de filtrer et de valider toutes les données utilisateur avant de les utiliser dans des requêtes SQL.

2. **Authentification faible :** Une authentification faible, des mots de passe faibles ou l'utilisation de comptes par défaut peuvent faciliter l'accès non autorisé à la base de données. Pour y remédier :
   - Utilisez des mots de passe forts et encouragez une politique de gestion des mots de passe.
   - Limitez l'accès en fonction des principes du moindre privilège, en n'accordant que les autorisations nécessaires à chaque utilisateur.




