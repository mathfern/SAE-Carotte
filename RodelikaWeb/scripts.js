function hideResults() {
    $("#result").empty();
}

function getStudents() {
    hideResults();
    $("#newStudentForm").hide();
    $("#addBonusForm").hide();
    $.ajax({
    	
        type: "POST",
        url: "call_python_function.php",
        data: { choice: 1 },
        dataType: "json",
        success: function (response) {
            displayResultsEtudiant(response);
	    
        },
        error: function (error) {
            console.log("Error:", error);
        }
    });
}

function getSold() {
    hideResults();
    $("#newStudentForm").hide();
    $("#addBonusForm").hide();
    $.ajax({
        type: "POST",
        url: "call_python_function.php",
        data: { choice: 2 },
        dataType: "json",
        success: function (response) {
            displayResultsSolde(response);
	    
        },
        error: function (error) {
            console.log("Error:", error);
        }
    });
}


function displayResultsSolde(results) {
    hideResults();
    $("#newStudentForm").hide();
    $("#addBonusForm").hide();
    $("#result").empty();

    if (results.length > 0) {
        var table = "<table border='1'>";
        table += "<tr><th>Numéro Etudiant</th><th>Nom</th><th>Prénom</th><th>Solde</th><th>Bonus</th></tr>";

        for (var i = 0; i < results.length; i++) {
            table += "<tr>";
            table += "<td>" + results[i].etu_num + "</td>";
            table += "<td>" + results[i].etu_nom + "</td>";
            table += "<td>" + results[i].etu_prenom + "</td>";
            table += "<td>" + results[i].etu_solde + "</td>";
            table += "<td>" + results[i].etu_bonus + "</td>";
            table += "</tr>";
        }

        table += "</table>";
        $("#result").html(table);
    } else {
        $("#result").html("Aucun résultat trouvé.");
    }
}

function displayResultsEtudiant(results) {
    hideResults();
    $("#newStudentForm").hide();
    $("#addBonusForm").hide();
    $("#result").empty();

    if (results.length > 0) {
        var table = "<table border='1'>";
        table += "<tr><th>Numéro Etudiant</th><th>Nom</th><th>Prénom</th></tr>";

        for (var i = 0; i < results.length; i++) {
            table += "<tr>";
            table += "<td>" + results[i].etu_num + "</td>";
            table += "<td>" + results[i].etu_nom + "</td>";
            table += "<td>" + results[i].etu_prenom + "</td>";
            table += "</tr>";
        }

        table += "</table>";
        $("#result").html(table);
    } else {
        $("#result").html("Aucun résultat trouvé.");
    }
}
function newStudentForm() {
    $("#addBonusForm").hide();
    hideResults();
    $("#newStudentForm").toggle();
}

function newStudent() {
    $("#addBonusForm").hide();
    hideResults();
    var num_etudiant = $("#num_etudiant").val();
    var nom_etudiant = $("#nom_etudiant").val();
    var prenom_etudiant = $("#prenom_etudiant").val();

    $.ajax({
        type: "POST",
        url: "call_python_function.php",
        data: {
            choice: 3,
            num_etudiant: num_etudiant,
            nom_etudiant: nom_etudiant,
            prenom_etudiant: prenom_etudiant
        },
        success: function (response) {
            displayMessage(response);
	 
            
        },
        error: function (error) {
            console.log("Error:", error);
        }
    });
}

function addBonusForm() {
    $("#newStudentForm").hide();
    hideResults();
    $("#addBonusForm").toggle();
}
function addBonus() {
    $("#newStudentForm").hide();
    hideResults();
    var bonus_num_etudiant = $("#bonus_num_etudiant").val();

    $.ajax({
        type: "POST",
        url: "call_python_function.php",
        data: { choice: 4, bonus_num_etudiant: bonus_num_etudiant },
        success: function (response) {
            displayMessage(response);
	    
           
        },
        error: function (error) {
            console.log("Error:", error);
        }
    });
}


function goBack() {
    $("#result").empty();
    // Masque tous les formulaires
    $("#newStudentForm").hide();
    $("#addBonusForm").hide();
    // Efface les champs de formulaire
    $("#num_etudiant").val("");
    $("#nom_etudiant").val("");
    $("#prenom_etudiant").val("");
    $("#bonus_num_etudiant").val("");
}
