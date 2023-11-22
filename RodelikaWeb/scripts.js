function hideResults() {
    $("#result").empty();
}

function getStudents() {
    hideResults();										// On cache les résultats des autres fonctions pour éviter le chevauchement
    $("#supprimerEtudiantForm").hide();
    $("#newStudentForm").hide();
    $("#addBonusForm").hide();
    $.ajax({
    	
        type: "POST",
        url: "call_python_function.php",							// Appelle le script PHP pour récupérer la liste des étudiants
        data: { choice: 1 },									// Envoie le choix 1 pour la liste des étudiants
        dataType: "json",
        success: function (response) {								// Affiche les résultats des étudiants
            displayResultsEtudiant(response);
	    
        },
        error: function (error) { 								// En cas d'erreur, affiche un message dans la console
            console.log("Error:", error); 
        }
    });
}

// Fonction pour afficher les résultats des étudiants
function displayResultsEtudiant(results) {							//construit un tableau HTML pour afficher les résultats des étudiants 
    hideResults();										// On cache les résultats des autres fonctions pour éviter le chevauchement
    $("#supprimerEtudiantForm").hide();
    $("#newStudentForm").hide();
    $("#addBonusForm").hide();
    $("#result").empty();

    if (results.length > 0) {									//Vérifie si la variable results contient au moins un élément
        var table = "<table border='1'>";							//initialise une variable table en créant le début d'un élément de tableau HTML avec une bordure.
        table += "<tr><th>Numéro Etudiant</th><th>Nom</th><th>Prénom</th></tr>";		//Ajoute une ligne d'en-tête au tableau avec les titres des colonnes (Numéro Etudiant, Nom, Prénom).

        for (var i = 0; i < results.length; i++) {						//Démarre une boucle for pour itérer à travers tous les résultats (étudiants) dans le tableau results.
            table += "<tr>";
            table += "<td>" + results[i].etu_num + "</td>";					//Ajoute une cellule de données (colonne) au tableau avec le numéro de l'étudiant 
            table += "<td>" + results[i].etu_nom + "</td>";					//Ajoute une cellule de données avec le nom de l'étudiant.
            table += "<td>" + results[i].etu_prenom + "</td>";					//Ajoute une cellule de données avec le prénom de l'étudiant.
            table += "</tr>";
        }

        table += "</table>";
        $("#result").html(table);								//affiche le tableau HTML
    } else {
        $("#result").html("Aucun résultat trouvé.");						// En cas d'erreur, affiche un message 
    }
}



// Fonction pour récupérer les soldes des étudiants depuis le serveur
function getSold() {
    hideResults();										// On cache les résultats des autres fonctions pour éviter le chevauchement
    $("#supprimerEtudiantForm").hide();
    $("#newStudentForm").hide();
    $("#addBonusForm").hide();
    $.ajax({
        type: "POST",
        url: "call_python_function.php",							// Appelle le script PHP pour récupérer la liste des étudiants + solde
        data: { choice: 2 },									// Envoie le choix 2 pour la liste des étudiants + solde 
        dataType: "json",
        success: function (response) {								// si succès alors : 
            displayResultsSolde(response);							// Appel la fonction displayResultsSolde
	    
        },
        error: function (error) {								// En cas d'erreur, affiche un message dans la console
            console.log("Error:", error);
        }
    });
}


function displayResultsSolde(results) {
    hideResults();										// On cache les résultats des autres fonctions pour éviter le chevauchement
    $("#supprimerEtudiantForm").hide();
    $("#newStudentForm").hide();
    $("#addBonusForm").hide();
    $("#result").empty();

    if (results.length > 0) {
    // Construit un tableau HTML avec les résultats des soldes
        var table = "<table border='1'>";
        table += "<tr><th>Numéro Etudiant</th><th>Nom</th><th>Prénom</th><th>Solde</th><th>Bonus</th></tr>";

        for (var i = 0; i < results.length; i++) {
          // Remplit le tableau avec les données des étudiants
            table += "<tr>";
            table += "<td>" + results[i].etu_num + "</td>";
            table += "<td>" + results[i].etu_nom + "</td>";
            table += "<td>" + results[i].etu_prenom + "</td>";
            table += "<td>" + results[i].etu_solde + "</td>";
            table += "<td>" + results[i].etu_bonus + "</td>";
            table += "</tr>";
        }

        table += "</table>";
        $("#result").html(table);				 				// Affiche le tableau
    } else {
        $("#result").html("Aucun résultat trouvé.");		 				// Affiche un message si aucun résultat n'est trouver
    }
}

// Fonction pour afficher le formulaire d'ajout d'un nouvel étudiant
function newStudentForm() {
    $("#addBonusForm").hide();
    $("#supprimerEtudiantForm").hide();
    hideResults();
    
    $("#newStudentForm").toggle();				// Affiche ou cache le formulaire en fonction de son état actuel
}


// Fonction pour ajouter un nouvel étudiant
function newStudent() {
    $("#addBonusForm").hide();					// On cache les résultats des autres fonctions pour éviter le chevauchement
    $("#supprimerEtudiantForm").hide();
    hideResults();
    
    var num_etudiant = $("#num_etudiant").val();		// récupère la valeur du champ de saisie avec l'ID "num_etudiant" et l'assigne à la variable num_etudiant.
    var nom_etudiant = $("#nom_etudiant").val();		// récupère la valeur du champ de saisie avec l'ID "nom_etudiant" et l'assigne à la variable nom_etudiant.
    var prenom_etudiant = $("#prenom_etudiant").val();		// récupère la valeur du champ de saisie avec l'ID "prenom_etudiant" et l'assigne à la variable prenom_etudiant.

    $.ajax({
        type: "POST",
        url: "call_python_function.php",			// Appelle le script PHP
        data: {
            choice: 3,						// Envoie le choix 3 pour ajouter un étudiants
            num_etudiant: num_etudiant,
            nom_etudiant: nom_etudiant,
            prenom_etudiant: prenom_etudiant
        },
	success: function (response) {
	    console.log(response);
            if (response === "Error.") {
		displayErrorMessage("L'étudiant avec ce numéro existe déja.");				// En cas d'erreur, affiche un message
            } else {
                displayOkMessage("L'étudiant a été ajouté avec succès !");				// En cas d'ajout, affiche un message
            }
        },	
    });
}

function addBonusForm() {
    $("#newStudentForm").hide();
    $("#supprimerEtudiantForm").hide();
    hideResults();
    $("#addBonusForm").toggle();
}
function addBonus() {
    $("#newStudentForm").hide();
    $("#supprimerEtudiantForm").hide();
    hideResults();
    var bonus_num_etudiant = $("#bonus_num_etudiant").val();

    $.ajax({
        type: "POST",
        url: "call_python_function.php",
        data: { choice: 4, bonus_num_etudiant: bonus_num_etudiant },
	success: function (response) {
	    console.log(response);
            if (response === "Error.") {
		displayErrorMessage("L'étudiant avec ce numéro n'existe pas.");
            } else {
                displayOkMessage("Le Bonus a été ajouté avec succès !");
            }
        },

    });
}

function supprimerEtudiantForm() {
    hideResults();
    $("#newStudentForm").hide();
    $("#addBonusForm").hide();

    $("#supprimerEtudiantForm").toggle();
}

function supprimerEtudiant() {
    hideResults();
    $("#newStudentForm").hide();
    $("#addBonusForm").hide();

    var num_etudiant_suppr = $("#num_etudiant_suppr").val();

    $.ajax({
        type: "POST",
        url: "call_python_function.php",
        data: { choice: 5, num_etudiant_suppr: num_etudiant_suppr },
	success: function (response) {
	    console.log(response);
            if (response === "Error.") {
		displayErrorMessage("L'étudiant avec ce numéro n'existe pas.");
            } else {
                displayOkMessage("L'étudiant à bien été supprimé !");
            }
        },
    });
}






function goBack() {
    
    $("#result").empty();
    // Masque tous les formulaires
    $("#newStudentForm").hide();
    $("#addBonusForm").hide();
    $("#supprimerEtudiantForm").hide();
    // Efface les champs de formulaire
    $("#num_etudiant").val("");
    $("#nom_etudiant").val("");
    $("#prenom_etudiant").val("");
    $("#bonus_num_etudiant").val("");
}


function displayOkMessage(message) {
    $("#result").empty();
    $("#result").html("<p style='color: green;'>" + message + "</p>").css;
}

function displayErrorMessage(message) {
    $("#result").empty();
    $("#result").html("<p style='color: red;'>" + message + "</p>").css;
}
