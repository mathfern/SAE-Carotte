## Application web de gestion

L’application web de gestion donne la possibilité à l’agent administratif d’avoir une interface graphique qui permet l’utilisation plus interactive du logiciel de gestion Rodelika. 

Ce site sera codé en HTML/CSS et PHP et fera appel à la base de données PurpleDragon ainsi qu'à l'application Rodelika. 

### 1- Fonctionnalités à ajouter
On aimerait plus tard ajouter une interface graphique pour les élèves afin qu'ils puissent consulter leurs soldes. Et également une interface de connexion pour l’agent administratif pour sécuriser l’ajout de soldes dans la bdd. 

### 2- Vulnérabilités
Pour l'ajout futur de l'interface graphique de solde des élèves, sans informations de connexion un élève pourrait regarder le solde de n'importe quel autre élève inscrit. Pour remédier à cela, nous avons pensé à associer chaque carte à un identifiant (numéro étudiant) et un mot de passe sécurisé et chiffré. 

La création de mots de passe pourrait entraîner un autre problème : les attaques par force brute. Pour contrer cela, nous avons pensé à bloquer temporairement les tentatives de connexions au bout de 3 échecs et de geler le compte (mais pas la carte) au bout de 5 échecs. 

