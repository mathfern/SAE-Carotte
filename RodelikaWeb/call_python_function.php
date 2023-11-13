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
    $sql = "INSERT INTO Etudiant (etu_num, etu_nom, etu_prenom) VALUES ('$num_etudiant', '$nom_etudiant', '$prenom_etudiant')";
    $result = mysqli_query($cnx, $sql);

    if ($result) {
        echo "Nouvel étudiant ajouté avec succès.";
    } else {
        echo "Error: " . $sql . "<br>" . mysqli_error($cnx);
    }
}
function addBonus($bonus_num_etudiant) {
    global $cnx;
    $sql = "UPDATE Etudiant SET etu_bonus = etu_bonus + 1.00 WHERE etu_num = '$bonus_num_etudiant'";
    $result = mysqli_query($cnx, $sql);

    if ($result) {
        echo "Bonus added successfully.";
    } else {
        echo "Error: " . $sql . "<br>" . mysqli_error($cnx);
    }
}

mysqli_close($cnx);
?>
