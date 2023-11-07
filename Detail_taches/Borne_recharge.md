## Borne de recharge (Berlicum)
### 1 - Concept de la borne a recharge

La partie "Borne de Recharge (Berlicum)" se concentre sur le développement du logiciel embarqué pour une borne de recharge utilisée par des étudiants. Le but principal de cette borne est de permettre aux étudiants d'accéder à diverses fonctionnalités liées à leurs cartes à puce. Voici un aperçu des opérations principales que les étudiants peuvent effectuer à l'aide de cette borne :

- Afficher les Informations Personnelles : Cette fonctionnalité permet aux étudiants d'afficher les informations personnelles stockées sur leur carte à puce.

- Consulter les Bonus : Les étudiants peuvent consulter les bonus qui leur ont été attribués, mais qui n'ont pas encore été transférés sur leur carte. Les informations sur ces bonus sont extraites de la base de données, et la colonne "type_operation" dans la table "compte" indique "Bonus" pour les bonus non transférés.

- Transférer les Bonus : Les étudiants peuvent utiliser la borne pour transférer les bonus disponibles sur leur carte. Une fois que les bonus ont été transférés, la colonne "type_operation" dans la table "compte" est mise à jour pour indiquer "Bonus transféré". Il est essentiel que ces transactions respectent les propriétés ACID (Atomicité, Cohérence, Isolation et Durabilité) pour garantir l'intégrité des données.

- Consulter le crédit disponible : Les étudiants peuvent vérifier le solde disponible sur leur carte à puce, ce qui leur permet de suivre leurs ressources.

- Recharger le Crédit avec une Carte Bancaire : Lorsqu'un étudiant a épuisé ses bonus, il a la possibilité de recharger son crédit à l'aide d'une carte bancaire. Il est important de noter que le processus de recharge avec une carte bancaire est fictif dans le cadre de ce projet, et la borne simule simplement une transaction réussie.

Le développement du logiciel embarqué pour la borne de recharge (Berlicum) est essentiel pour offrir aux étudiants un accès facile à leurs informations, à leurs bonus et à leur crédit. Ce système contribue à la gestion efficace des ressources des étudiants, en garantissant l'intégrité des transactions et en facilitant la recharge en cas de besoin.

### 2 - Répartition classes et instructions

La classe utilisée par berlicum sera la classe 0x81, 0x82 et 0x83 de l’API du projet (cf partie Carte à Puces). 

Chaque opération réalisable par le logiciel sera associée à une instruction de la classe 0x81, 0x82 et 0x83 : . 

- Instruction pour l’*affichage des informations personnelles* : 0x81 0x02
- Instruction pour l’*affichage des bonus sur la carte* : 0x83 0x01
- Instruction pour l’*attribution des bonus sur la carte* : 0x83 0x02
- Instruction pour l’*affichage des crédits disponibles sur la carte* : 0x82 0x01
- Instruction pour l’*attribution d’argent sur la carte* : 0x82 0x02

### 3 - Idées de fonctions à rajouter pour Berlicum

- Une instruction qui contient une fonction qui permet de consulter l’historique de transaction. Cela peut les aider à suivre et à gérer les opérations passées.

