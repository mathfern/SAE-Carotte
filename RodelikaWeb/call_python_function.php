<?php
$host = "localhost";
$user = "root";
$password = "root";
$database = "purpledragon1";

$cnx = mysqli_connect($host, $user, $password, $database);

if (!$cnx) {
    die("Connection failed: " . mysqli_connect_error());
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $choice = $_POST['choice'];

    switch ($choice) {
        case 1:
            getStudents();
            break;
        case 2:
            getSold();
            break;
        case 3:
            newStudent($_POST['num_etudiant'], $_POST['nom_etudiant'], $_POST['prenom_etudiant']);
            break;
        case 4:
            addBonus($_POST['bonus_num_etudiant']);
            break;
        case 5:
            supprEtudiant($_POST['num_etudiant_suppr']);
            break;
        default:
            echo "Invalid choice.";
    }
}

function getStudents() {
    global $cnx;
    $sql = "SELECT etu_num, etu_nom, etu_prenom FROM Etudiant";
    $result = mysqli_query($cnx, $sql);

    if ($result) {
        $rows = mysqli_fetch_all($result, MYSQLI_ASSOC);
        echo json_encode($rows);
    } else {
        echo "Error: " . $sql . "<br>" . mysqli_error($cnx);
    }
}

function getSold() {
    global $cnx;
    $sql = "SELECT etu_num, etu_nom, etu_prenom, etu_solde, etu_bonus FROM Etudiant";
    $result = mysqli_query($cnx, $sql);

    if ($result) {
        $rows = mysqli_fetch_all($result, MYSQLI_ASSOC);
        echo json_encode($rows);
    } else {
        echo "Error: " . $sql . "<br>" . mysqli_error($cnx);
    }
}



function newStudent($num_etudiant, $nom_etudiant, $prenom_etudiant) {
    global $cnx;
    // Vérifier d'abord si l'étudiant existe
    $checkSql = "SELECT * FROM Etudiant WHERE etu_num = '$num_etudiant'";
    $checkResult = mysqli_query($cnx, $checkSql);

    if ($checkResult && mysqli_num_rows($checkResult) == 0) {
        // L'étudiant n'existe pas, exécuter la requête
        $sql = "INSERT INTO Etudiant (etu_num, etu_nom, etu_prenom) VALUES ('$num_etudiant', '$nom_etudiant', '$prenom_etudiant')";
        $result = mysqli_query($cnx, $sql);

        if ($result) {
            echo "added successfully.";
        } else {
            echo "Error." . mysqli_error($cnx);
        }
    } else {
        // L'étudiant n'existe pas
        echo "Error.";
    }
}






function addBonus($bonus_num_etudiant) {
    global $cnx;

    // Vérifier d'abord si l'étudiant existe
    $checkSql = "SELECT * FROM Etudiant WHERE etu_num = '$bonus_num_etudiant'";
    $checkResult = mysqli_query($cnx, $checkSql);

    if ($checkResult && mysqli_num_rows($checkResult) > 0) {
        // L'étudiant existe, exécuter la requête de mise à jour
        $updateSql = "UPDATE Etudiant SET etu_bonus = etu_bonus + 1.00 WHERE etu_num = '$bonus_num_etudiant'";
        $updateResult = mysqli_query($cnx, $updateSql);

        if ($updateResult) {
            echo "Bonus added successfully.";
        } else {
            echo "Error." . mysqli_error($cnx);
        }
    } else {
        // L'étudiant n'existe pas
        echo "Error.";
    }
}


function supprEtudiant($num_etudiant) {
    global $cnx;
    $check_query = "SELECT COUNT(*) FROM Etudiant WHERE etu_num = '$num_etudiant';";
    $check_result = mysqli_query($cnx, $check_query);
    $result = mysqli_fetch_assoc($check_result);

    if ($result['COUNT(*)'] > 0) {
        $sql_delete_compte = "DELETE FROM Compte WHERE etu_num = '$num_etudiant';";
        $result_compte = mysqli_query($cnx, $sql_delete_compte);
        $sql_delete_etudiant = "DELETE FROM Etudiant WHERE etu_num = '$num_etudiant';";
        $result_etudiant = mysqli_query($cnx, $sql_delete_etudiant);

        if ($result_compte && $result_etudiant) {
            echo "L'étudiant a bien été supprimé.";
        	} else {
        	echo "Error." . mysqli_error($cnx);
        	}
    } else {
        echo "Error.";
    }
}

mysqli_close($cnx);
?>
