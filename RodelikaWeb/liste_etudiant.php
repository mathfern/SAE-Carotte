<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <title>Rodelika Web Interface</title>
    <link rel="stylesheet" href="style.css">
    <script src="scripts.js"></script>
</head>

<body>

    <header>
        <h1>Rodelika Web Interface</h1>
    </header>

    <nav>
        <ul>
            <li><a href="liste_etudiant.php">Liste des étudiants</a></li>
            <li><a href="solde_etudiant.html">Solde des étudiants</a></li>
            <li><a href="nv_etudiant.html">Nouvel étudiant</a></li>
            <li><a href="bonus.html">Attribuer un bonus</a></li>
            <li><a href="index.html">Accueil</a></li>
        </ul>
    </nav>

    <?php
$output = shell_exec("python Rodelika.py 1");
echo "<pre>$output</pre>";
?>
    
    <footer>
        <p>&copy; 2023 Rodelika Web Interface. Adrien Boucher, Mathias Fernandes, Antoine Machard, Djibril Namoune.</p>
    </footer>

</body>

</html>
