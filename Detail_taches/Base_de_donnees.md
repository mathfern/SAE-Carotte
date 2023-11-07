## Purple Dragon (Base de données)

### 1 - Concept de base de donnée carte à puce

Une base de données (purple dragon) implémenter en mysql pour les cartes à puce est une base de données utilisée pour stocker des informations liées aux cartes à puce :

- Les données des étudiants comme le numéro d’étudiant et contient uniquement les informations essentielles, à savoir le nom et le prénom. 

- Les données du compte qui  représente les opérations effectuées par les utilisateurs, elle est identifiée par la date de l’opération, et contient deux autres 
  champs, le montant de l’opération et sa description. Étant donné que plusieurs utilisateurs peuvent effectuer simultanément différentes opérations, nous avons 
  choisi d'associer le numéro d'étudiant à la clé primaire en utilisant une relation relative (R). Le montant de l'opération peut être positif en cas de bonus ou de 
  crédit, ou négatif en cas de débit.

- Les données du type de l’opération qui permet de catégoriser les types d'opérations : Bonus, Bonus transféré, Crédit et Débit.


Le schémas relationnel (MCD) proposé est donné ci-après : 

![image](https://github.com/mathfern/SAE-Carotte/assets/150126517/3a7f34bb-3c22-4650-a28d-bbfdfdd74d67)

Cette base de données devra être accessible par le logiciel lubiana pour permettre à la personnalisation de la carte à puces et aussi par le logiciel de gestion Rodelika afin de permettre à l’agent administratif de gérer le suivi des cartes, des bonus, des débit etc.

Chaque étudiant partira de base avec 1 euro qu'il devra récuperer sur la borne de recharge pour en profiter.
