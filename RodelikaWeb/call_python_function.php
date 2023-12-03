<?php
$host = "localhost";
$user = "root";                                        // Connexion BDD
$password = "root";
$database = "purpledragon1";

$cnx = mysqli_connect($host, $user, $password, $database);

if (!$cnx) {
    die("Connection failed: " . mysqli_connect_error());
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $choice = $_POST['choice'];

    switch ($choice) {                                // En fonction du choix appeler la fonction 
        case 1:
            getStudents();
            break;
        case 2:
            getSold();
            break;
        case 3:                                        //Appelle la fonction en passant les paramêtre suivant :
            newStudent($_POST['num_etudiant'], $_POST['nom_etudiant'], $_POST['prenom_etudiant']);
            break;
        case 4:                                        //Appelle la fonction en passant les paramêtre suivant :
            addBonus($_POST['bonus_num_etudiant']);
            break;
        case 5:                                        //Appelle la fonction en passant les paramêtre suivant :
            supprEtudiant($_POST['num_etudiant_suppr']);
            break;
        default:                                        // Si la valeur de choice ne correspond à aucun des cas le code affiche Invalid Choice 
            echo "Invalid choice.";
    }
}

function getStudents() {
    global $cnx;
    // Construit la requête SQL pour sélectionner les numéros, noms et prénoms des étudiants
    $sql = "SELECT etu_num, etu_nom, etu_prenom FROM Etudiant";
    // Exécute la requête SQL en utilisant la connexion à la base de données
    $result = mysqli_query($cnx, $sql);
    // Vérifie si la requête SQL a réussi
    if ($result) {
        // Récupère toutes les lignes de résultat sous forme associative
        $rows = mysqli_fetch_all($result, MYSQLI_ASSOC);
        // Convertit les résultats en format JSON et les affiche
        echo json_encode($rows);
    } else {
        // En cas d'erreur, affiche un message d'erreur avec les détails de la requête SQL
        echo "Error: " . $sql . "<br>" . mysqli_error($cnx);
    }
}

function getSold() {
    global $cnx;
    // Construit la requête SQL pour sélectionner les numéros, noms, prénoms, solde et bonus des étudiants
    $sql = "SELECT etu_num, etu_nom, etu_prenom, etu_solde, etu_bonus FROM Etudiant";

    // Exécute la requête SQL en utilisant la connexion à la base de données
    $result = mysqli_query($cnx, $sql);

    // Vérifie si la requête SQL a réussi
    if ($result) {
        // Récupère toutes les lignes de résultat
        $rows = mysqli_fetch_all($result, MYSQLI_ASSOC);
        // Convertit les résultats en format JSON et les affiche
        echo json_encode($rows);
    } else {
        // En cas d'erreur, affiche un message d'erreur avec les détails de la requête SQL
        echo "Error: " . $sql . "<br>" . mysqli_error($cnx);
    }
}



function newStudent($num_etudiant, $nom_etudiant, $prenom_etudiant) {
    global $cnx;
    // Vérifie d'abord si l'étudiant existe en recherchant son numéro d'étudiant dans la base de données
    $checkSql = "SELECT * FROM Etudiant WHERE etu_num = '$num_etudiant'";
    $checkResult = mysqli_query($cnx, $checkSql);

    // Vérifie si la requête de vérification a réussi et si l'étudiant n'existe pas déjà
    if ($checkResult && mysqli_num_rows($checkResult) == 0) {
        // L'étudiant n'existe pas, donc exécute la requête d'insertion
        $sql = "INSERT INTO Etudiant (etu_num, etu_nom, etu_prenom) VALUES ('$num_etudiant', '$nom_etudiant', '$prenom_etudiant')";
        $result = mysqli_query($cnx, $sql);

        // Vérifie si la requête d'insertion a réussi
        if ($result) {
            // Affiche un message indiquant que l'ajout a été effectué avec succès
            echo "added successfully.";
        } else {
            // En cas d'échec de la requête d'insertion, affiche un message d'erreur avec les détails de l'erreur SQL
            echo "Error." . mysqli_error($cnx);
        }
    } else {
         // L'étudiant existe déjà, affiche un message d'erreur
        echo "Error.";
    }
}






function addBonus($bonus_num_etudiant) {
    global $cnx;

    // Vérifie d'abord si l'étudiant existe en recherchant son numéro d'étudiant dans la base de données
    $checkSql = "SELECT * FROM Etudiant WHERE etu_num = '$bonus_num_etudiant'";
    $checkResult = mysqli_query($cnx, $checkSql);

    // Vérifie si la requête de vérification a réussi et si l'étudiant existe
    if ($checkResult && mysqli_num_rows($checkResult) > 0) {
        // L'étudiant existe, donc exécute la requête de mise à jour pour ajouter un bonus
        $updateSql = "UPDATE Etudiant SET etu_bonus = etu_bonus + 1.00 WHERE etu_num = '$bonus_num_etudiant'";
        $updateResult = mysqli_query($cnx, $updateSql);


        
        // Vérifie si la requête de mise à jour a réussi
        if ($updateResult) {
            // Affiche un message indiquant que le bonus a été ajouté avec succès
            echo "Bonus added successfully.";
        } else {
            // En cas d'échec de la requête de mise à jour, affiche un message d'erreur avec les détails de l'erreur SQL
            echo "Error." . mysqli_error($cnx);
        }
    } else {
        // L'étudiant n'existe pas, affiche un message d'erreur
        echo "Error.";
    }
}



// Définit la fonction supprEtudiant avec un paramètre $num_etudiant
function supprEtudiant($num_etudiant) {
    global $cnx;

    // Construit la requête SQL pour compter le nombre de fois que l'étudiant apparait avec le numéro spécifié
    $check_query = "SELECT COUNT(*) FROM Etudiant WHERE etu_num = '$num_etudiant';";
    $check_result = mysqli_query($cnx, $check_query);
    $result = mysqli_fetch_assoc($check_result);


    // Vérifie si l'étudiant existe (le nombre de fois ou il apparait est supérieur à 0)
    if ($result['COUNT(*)'] > 0) {
        // Construit la requête SQL pour supprimer l'étudiant de la table Compte
        $sql_delete_compte = "DELETE FROM Compte WHERE etu_num = '$num_etudiant';";
        $result_compte = mysqli_query($cnx, $sql_delete_compte);

        // Construit la requête SQL pour supprimer l'étudiant de la table Etudiant
        $sql_delete_etudiant = "DELETE FROM Etudiant WHERE etu_num = '$num_etudiant';";
        $result_etudiant = mysqli_query($cnx, $sql_delete_etudiant);

        // Vérifie si les deux requêtes de suppression ont réussi
        if ($result_compte && $result_etudiant) {
            // Affiche un message indiquant que l'étudiant a été supprimé avec succès
            echo "L'étudiant a bien été supprimé.";
        	} else {
            // En cas d'échec de l'une des requêtes de suppression, affiche un message d'erreur avec les détails de l'erreur SQL
        	echo "Error." . mysqli_error($cnx);
        	}
    } else {
        // L'étudiant n'existe pas, affiche un message d'erreur
        echo "Error.";
    }
}

mysqli_close($cnx);
?>
