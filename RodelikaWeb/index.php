<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rodelika Web Interface</title>
    <link rel="stylesheet" href="style.css">
   <!-- <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script> -->
   <!-- <script src="scripts.js"></script> -->
</head>

<body>

    <header>
        <h1>Rodelika Web Interface</h1>
    </header>
    
     <?php
     $server = "localhost";
     $user = "root";
     $mdp = "root";
     $bdd = "purpledragon1";
     
     $connect = new mysqli($server, $user, $mdp, $bdd); //etablissement de la connexion

     if (!$connect) {
        die("Connexion échouée: " . mysqli_connect_error());
	}

	if ($_SERVER['REQUEST_METHOD'] == 'POST'){ //Méthode post
        $login = $_POST["login"];
        $password = $_POST["password"];

	//Requête préparée pour éviter les injections SQL
        $requete_prep = $connect->prepare("SELECT * FROM admin WHERE login = ?");
        $requete_prep->bind_param("s", $login); //lie les valeurs des variables "s" indique que ce sont des type strings

        //execute la requête
        $requete_prep->execute();

        //recupere le resultat
        $resultat = $requete_prep->get_result();
        //echo "Résultat de la requête : " . $resultat->num_rows;
        
        if ($resultat->num_rows > 0) {
        $recup_ligne = $resultat->fetch_assoc(); //Récupère la ligne du résultat sous forme de tableau avec le nom des colonnes de la table
        $mdp_hash_bdd = $recup_ligne['mot_de_passe']; //Recupere la valeur de la colonne mot_de_passe dans le tableau
        
        if (password_verify($password, $mdp_hash_bdd)) { //si le hash du mdp correspond au mdp de la bdd
            echo "Connexion réussie !";
            header("Location: accueil.html"); //Redirection
            exit();
            } else{ //Si on a le bon login mais le mauvais mot de passe 
            echo "Nom d'utilisateur ou mot de passe incorrect.";
            }
        }
        else { //Si on n'a ni le login ni le mot de passe, la même phrase d'erreur pour les 2 pour éviter les injections sql
           echo "Nom d'utilisateur ou mot de passe incorrect.";
         }
         
       //Ferme la connexion
       $connect->close();
	}
     ?>
     
    <form action ="index.php" method="post">
            <!-- Champs du formulaire -->
            <label for="login">Login : </label>
	    <input type="text" id="login" name="login" required></br>
	    
	    <label for="password"> Mot de passe :</label>
	    <input type="password" id="password" name="password" required></br>
	    
	    <!-- Bouton -->
	    <input type="submit" value="connexion">
    </form>

    <footer>
        <p>&copy; 2023 Rodelika Web Interface. Adrien Boucher, Mathias Fernandes, Antoine Machard, Djibril Namoune.</p>
    </footer>

</body>

</html>
