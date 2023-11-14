
function getStudents() {
<<<<<<< HEAD
=======
    goBack();
    
>>>>>>> 831b8ee24ac38cc174e293c59c2f73452fc8cc1d
    $.ajax({
        type: "POST",
        url: "call_python_function.php",
        data: { choice: 1 },
        dataType: "json",
        success: function (response) {
<<<<<<< HEAD
            displayResultsetu(response);
=======
            displayResults(response);
>>>>>>> 831b8ee24ac38cc174e293c59c2f73452fc8cc1d
        },
        error: function (error) {
            console.log("Error:", error);
        }
    });
}

function getSold() {
<<<<<<< HEAD
=======
    goBack();
    
>>>>>>> 831b8ee24ac38cc174e293c59c2f73452fc8cc1d
    $.ajax({
        type: "POST",
        url: "call_python_function.php",
        data: { choice: 2 },
        dataType: "json",
        success: function (response) {
<<<<<<< HEAD
            displayResultssolde(response);
=======
            displayResultsSolde(response);
>>>>>>> 831b8ee24ac38cc174e293c59c2f73452fc8cc1d
        },
        error: function (error) {
            console.log("Error:", error);
        }
    });
}

<<<<<<< HEAD

function displayResultssolde(results) {
=======
function displayResults(results) {
>>>>>>> 831b8ee24ac38cc174e293c59c2f73452fc8cc1d
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


function displayResultsSolde(results) {
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

function displayResultsetu(results) {
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
    $("#newStudentForm").toggle();
}

function newStudent() {
    goBack();
    
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
            // Recharge la liste des étudiants après l'ajout
            getStudents();
            // Masque le formulaire après l'ajout
            goBack();
        },
        error: function (error) {
            console.log("Error:", error);
        }
    });
}

function addBonusForm() {
    $("#addBonusForm").toggle();
}
function addBonus() {
    goBack();
    
    var bonus_num_etudiant = $("#bonus_num_etudiant").val();

    $.ajax({
        type: "POST",
        url: "call_python_function.php",
        data: { choice: 4, bonus_num_etudiant: bonus_num_etudiant },
        success: function (response) {
            displayMessage(response);
            // Recharge la liste des étudiants après l'ajout du bonus
            getStudents();
            // Masque le formulaire après l'ajout
            goBack();
        },
        error: function (error) {
            console.log("Error:", error);
        }
    });
}


function goBack() {
    $("#result").empty();
<<<<<<< HEAD
   
=======
    
>>>>>>> 831b8ee24ac38cc174e293c59c2f73452fc8cc1d
    // Masque tous les formulaires
    $("#newStudentForm").hide();
    $("#addBonusForm").hide();

    // Efface les champs de formulaire
    $("#num_etudiant").val("");
    $("#nom_etudiant").val("");
    $("#prenom_etudiant").val("");
    $("#bonus_num_etudiant").val("");
}
