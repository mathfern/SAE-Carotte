function hideResults() {
    $("#result").empty();
}


// fonction pour affihcer la liste des étudiants 
function getStudents() {
    hideResults();									// On cache les résultats des autres fonctions pour éviter le chevauchement
    $("#supprimerEtudiantForm").hide();
    $("#newStudentForm").hide();
    $("#addBonusForm").hide();
    $.ajax({
    	
        type: "POST",
        url: "call_python_function.php",						// Appelle le script PHP pour récupérer la liste des étudiants
        data: { choice: 1 },								// Envoie le choix 1 pour la liste des étudiants
        dataType: "json",
        success: function (response) {							// Affiche les résultats des étudiants
            displayResultsEtudiant(response);
	    
        },
        error: function (error) { 							// En cas d'erreur, affiche un message dans la console
            console.log("Error:", error); 
        }
    });
}


function displayResultsEtudiant(results) {						//construit un tableau HTML pour afficher les résultats des étudiants 
    hideResults();									// On cache les résultats des autres fonctions pour éviter le chevauchement
    $("#supprimerEtudiantForm").hide();
    $("#newStudentForm").hide();
    $("#addBonusForm").hide();
    $("#result").empty();

    if (results.length > 0) {								//Vérifie si la variable results contient au moins un élément
        var table = "<table border='1'>";						//initialise une variable table en créant le début d'un élément de tableau HTML avec une bordure.
        table += "<tr><th>Numéro Etudiant</th><th>Nom</th><th>Prénom</th></tr>";	//Ajoute une ligne d'en-tête au tableau avec les titres des colonnes (Numéro Etudiant, Nom, Prénom).

        for (var i = 0; i < results.length; i++) {					//Démarre une boucle for pour itérer à travers tous les résultats (étudiants) dans le tableau results.
            table += "<tr>";
            table += "<td>" + results[i].etu_num + "</td>";				//Ajoute une cellule de données (colonne) au tableau avec le numéro de l'étudiant 
            table += "<td>" + results[i].etu_nom + "</td>";				//Ajoute une cellule de données avec le nom de l'étudiant.
            table += "<td>" + results[i].etu_prenom + "</td>";				//Ajoute une cellule de données avec le prénom de l'étudiant.
            table += "</tr>";
        }

        table += "</table>";
        $("#result").html(table);							//affiche le tableau HTML
    } else {
        $("#result").html("Aucun résultat trouvé.");					// En cas d'erreur, affiche un message 
    }
}


// Fonction pour récupérer les soldes des étudiants depuis le serveur
function getSold() {
    hideResults();									// On cache les résultats des autres fonctions pour éviter le chevauchement
    $("#supprimerEtudiantForm").hide();
    $("#newStudentForm").hide();
    $("#addBonusForm").hide();
    $.ajax({
        type: "POST",
        url: "call_python_function.php",						// Appelle le script PHP pour récupérer la liste des étudiants + solde
        data: { choice: 2 },								// Envoie le choix 2 pour la liste des étudiants + solde 
        dataType: "json",
        success: function (response) {							// si succès alors : 
            displayResultsSolde(response);						// Appel la fonction displayResultsSolde
	    
        },
        error: function (error) {							// En cas d'erreur, affiche un message dans la console
            console.log("Error:", error);
        }
    });
}


function displayResultsSolde(results) {
    hideResults();									// On cache les résultats des autres fonctions pour éviter le chevauchement
    $("#supprimerEtudiantForm").hide();
    $("#newStudentForm").hide();
    $("#addBonusForm").hide();
    $("#result").empty();

    if (results.length > 0) {								//Vérifie si la variable results contient au moins un élément
   									 		// Construit un tableau HTML avec les résultats des soldes
        var table = "<table border='1'>";						//initialise une variable table en créant le début d'un élément de tableau HTML avec une bordure.
        table += "<tr><th>Numéro Etudiant</th><th>Nom</th><th>Prénom</th><th>Solde</th><th>Bonus</th></tr>";		//Ajoute une ligne d'en-tête au tableau avec les titres des colonnes.

        for (var i = 0; i < results.length; i++) {
          										// Remplit le tableau avec les données des étudiants
            table += "<tr>";
            table += "<td>" + results[i].etu_num + "</td>";				//Ajoute une cellule de données avec le numéro de l'étudiant.
            table += "<td>" + results[i].etu_nom + "</td>";				//Ajoute une cellule de données avec le nom de l'étudiant.
            table += "<td>" + results[i].etu_prenom + "</td>";				//Ajoute une cellule de données avec le prénom de l'étudiant.
            table += "<td>" + results[i].etu_solde + "</td>";				//Ajoute une cellule de données avec le solde de l'étudiant.
            table += "<td>" + results[i].etu_bonus + "</td>";				//Ajoute une cellule de données avec les bonus de l'étudiant.
            table += "</tr>";
        }

        table += "</table>";
        $("#result").html(table);				 			// Affiche le tableau
    } else {
        $("#result").html("Aucun résultat trouvé.");		 			// Affiche un message si aucun résultat n'est trouver
    }
}


// Fonction pour afficher le formulaire d'ajout d'un nouvel étudiant
function newStudentForm() {
    $("#addBonusForm").hide();
    $("#supprimerEtudiantForm").hide();
    hideResults();
    
    $("#newStudentForm").toggle();							// Affiche ou cache le formulaire en fonction de son état actuel
}


// Fonction pour ajouter un nouvel étudiant
function newStudent() {
    $("#addBonusForm").hide();								// On cache les résultats des autres fonctions pour éviter le chevauchement
    $("#supprimerEtudiantForm").hide();
    hideResults();
    
    var num_etudiant = $("#num_etudiant").val();					// récupère la valeur du champ de saisie avec l'ID "num_etudiant" et l'assigne à la variable num_etudiant.
    var nom_etudiant = $("#nom_etudiant").val();					// récupère la valeur du champ de saisie avec l'ID "nom_etudiant" et l'assigne à la variable nom_etudiant.
    var prenom_etudiant = $("#prenom_etudiant").val();					// récupère la valeur du champ de saisie avec l'ID "prenom_etudiant" et l'assigne à la variable prenom_etudiant.

    $.ajax({
        type: "POST",
        url: "call_python_function.php",						// Appelle le script PHP
        data: {
            choice: 3,									// Envoie le choix 3 pour ajouter un étudiants
            num_etudiant: num_etudiant,							// permet au script PHP côté serveur de récupérer ces valeurs pour ajouter un nouvel étudiant à la bdd
            nom_etudiant: nom_etudiant,
            prenom_etudiant: prenom_etudiant
        },
	success: function (response) {
	    console.log(response);
            if (response === "Error.") {
		displayErrorMessage("L'étudiant avec ce numéro existe déja.");		// En cas d'erreur, affiche un message
            } else {
                displayOkMessage("L'étudiant a été ajouté avec succès !");		// En cas d'ajout, affiche un message
            }
        },	
    });
}


// Fonction ajouter un bonus 
function addBonusForm() {
    $("#newStudentForm").hide();
    $("#supprimerEtudiantForm").hide();
    hideResults();
    $("#addBonusForm").toggle();							// Affiche ou cache le formulaire en fonction de son état actuel
}


function addBonus() {
    $("#newStudentForm").hide();
    $("#supprimerEtudiantForm").hide();							// On cache les résultats des autres fonctions pour éviter le chevauchement
    hideResults();
    
    
    var bonus_num_etudiant = $("#bonus_num_etudiant").val();				// sélectionne l'élément de formulaire avec l'ID "bonus_num_etudiant

    $.ajax({
        type: "POST",
        url: "call_python_function.php",						// Appelle le script PHP
        data: { choice: 4, bonus_num_etudiant: bonus_num_etudiant },			// Envoie le choix 4 pour ajouter un bonus
        										// permet au script PHP côté serveur de récupérer ces valeurs pour ajouter un nouveau bonus à un étudiant
	success: function (response) {
	    console.log(response);
            if (response === "Error.") {						// Si le message dans les log est Error. alors afficher displayErrorMessage
		displayErrorMessage("L'étudiant avec ce numéro n'existe pas.");
            } else {									// Sinon afficher displayOkMessage
                displayOkMessage("Le Bonus a été ajouté avec succès !");
            }
        },

    });
}


// Fonction supprimer un étudiant 
function supprimerEtudiantForm() {
    hideResults();
    $("#newStudentForm").hide();
    $("#addBonusForm").hide();

    $("#supprimerEtudiantForm").toggle();						// Affiche ou cache le formulaire en fonction de son état actuel
}

function supprimerEtudiant() {
    hideResults();
    $("#newStudentForm").hide();							// On cache les résultats des autres fonctions pour éviter le chevauchement
    $("#addBonusForm").hide();

    var num_etudiant_suppr = $("#num_etudiant_suppr").val();				// sélectionne l'élément de formulaire avec l'ID "num_etudiant_suppr"

    $.ajax({
        type: "POST",
        url: "call_python_function.php",						// Appelle le script PHP
        data: { choice: 5, num_etudiant_suppr: num_etudiant_suppr },			// Envoie le choix 4 pour ajouter un bonus
        										// permet au script PHP côté serveur de récupérer ces valeurs pour supprimer un étudiant de la bdd
	success: function (response) {
	    console.log(response);
            if (response === "Error.") {						// Si le message dans les log est Error. alors afficher displayErrorMessage
		displayErrorMessage("L'étudiant avec ce numéro n'existe pas.");
            } else {
                displayOkMessage("L'étudiant à bien été supprimé !");			// Sinon afficher displayOkMessage
            }
        },
    });
}


// Fonction Acceuil
function goBack() {
    
    $("#result").empty();								// vide le contenu de l'élément HTML qui a l'ID "result".

    $("#newStudentForm").hide();
    $("#addBonusForm").hide();								// Masque tous les formulaires
    $("#supprimerEtudiantForm").hide();
    
    $("#num_etudiant").val("");
    $("#nom_etudiant").val("");								// Efface les champs de formulaire
    $("#prenom_etudiant").val("");
    $("#bonus_num_etudiant").val("");
}


// Fonction message OK
function displayOkMessage(message) {
    $("#result").empty();								// vide le contenu de l'élément HTML qui a l'ID "result".
    $("#result").html("<p style='color: green;'>" + message + "</p>").css;		// dans la variable result on met en couleur vert le message qui sera défini dans les fonctions 
}


// Fonction message erreur
function displayErrorMessage(message) {
    $("#result").empty();								// vide le contenu de l'élément HTML qui a l'ID "result".
    $("#result").html("<p style='color: red;'>" + message + "</p>").css;		// dans la variable result on met en couleur rouge le message qui sera défini dans les fonctions 
}
