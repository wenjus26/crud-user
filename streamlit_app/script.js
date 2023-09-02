// script.js

function addUser() {
    const firstName = document.getElementById("first_name").value;
    const lastName = document.getElementById("last_name").value;
    const email = document.getElementById("email").value;

    // Envoyez une requête HTTP POST au backend pour ajouter l'utilisateur
    fetch('/add_user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            first_name: firstName,
            last_name: lastName,
            email: email
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message); // Affichez un message de succès
        refreshUserTable(); // Rafraîchissez la table des utilisateurs
    })
    .catch(error => {
        console.error('Erreur lors de l\'ajout de l\'utilisateur : ', error);
    });
}

function updateUser() {
    const userIdUpdate = document.getElementById("user_id_update").value;
    const updatedFirstName = document.getElementById("updated_first_name").value;
    const updatedLastName = document.getElementById("updated_last_name").value;
    const updatedEmail = document.getElementById("updated_email").value;

    // Envoyez une requête HTTP POST au backend pour mettre à jour l'utilisateur
    fetch('/update_user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            user_id: userIdUpdate,
            first_name: updatedFirstName,
            last_name: updatedLastName,
            email: updatedEmail
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message); // Affichez un message de succès
        refreshUserTable(); // Rafraîchissez la table des utilisateurs
    })
    .catch(error => {
        console.error('Erreur lors de la mise à jour de l\'utilisateur : ', error);
    });
}

function deleteUser() {
    const userIdDelete = document.getElementById("user_id_delete").value;

    // Envoyez une requête HTTP POST au backend pour supprimer l'utilisateur
    fetch('/delete_user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            user_id: userIdDelete
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message); // Affichez un message de succès
        refreshUserTable(); // Rafraîchissez la table des utilisateurs
    })
    .catch(error => {
        console.error('Erreur lors de la suppression de l\'utilisateur : ', error);
    });
}

function generateExcel() {
    // Envoyez une requête HTTP GET au backend pour obtenir les données des utilisateurs
    fetch('/list_users')
    .then(response => response.json())
    .then(data => {
        // Créez un tableau des données des utilisateurs au format JSON
        const userList = data.map(user => {
            return {
                "ID": user.id,
                "Prénom": user.first_name,
                "Nom de famille": user.last_name,
                "Email": user.email
            };
        });

        // Utilisez la bibliothèque xlsx pour générer le fichier Excel
        const XLSX = require('xlsx');
        const ws = XLSX.utils.json_to_sheet(userList);
        const wb = XLSX.utils.book_new();
        XLSX.utils.book_append_sheet(wb, ws, "Utilisateurs");
        const excelBlob = XLSX.write(wb, { bookType: "xlsx", type: "blob" });

        // Créez un objet Blob à partir du fichier Excel
        const blob = new Blob([excelBlob], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });

        // Créez une URL de téléchargement
        const url = URL.createObjectURL(blob);

        // Créez un lien de téléchargement pour le fichier Excel généré
        const a = document.createElement('a');
        a.href = url;
        a.download = 'utilisateurs.xlsx';
        a.style.display = 'none';

        // Ajoutez le lien au DOM et déclenchez le téléchargement
        document.body.appendChild(a);
        a.click();

        // Libérez l'URL de l'objet Blob après le téléchargement
        URL.revokeObjectURL(url);
    })
    .catch(error => {
        console.error('Erreur lors de la génération du fichier Excel : ', error);
    });
}

// Rafraîchir la table des utilisateurs (vous devrez implémenter cette fonction)
function refreshUserTable() {
    // Mettez à jour la table des utilisateurs avec les données actuelles depuis le backend
    // Vous devrez implémenter cette fonction en fonction de votre backend
}
