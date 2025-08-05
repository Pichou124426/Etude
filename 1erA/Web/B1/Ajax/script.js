$(document).ready(function () {
    // Suppression d'un élément
    $(document).on("click", ".delete-btn", function () {
        let itemId = $(this).data("id");

        if (confirm("Voulez-vous vraiment supprimer cet élément ?")) {
            $.ajax({
                url: "delete.php",
                type: "POST",
                data: { id: itemId },
                dataType: "json",
                success: function (response) {
                    if (response.success) {
                        alert("Élément supprimé !");
                        $("#item-" + itemId).remove();
                    } else {
                        alert("Erreur : " + response.error);
                    }
                }
            });
        }
    });

    // Ajout d'un élément
    $("#add-form").submit(function (event) {
        event.preventDefault(); // Empêche le rechargement de la page

        let itemName = $("#item-name").val();

        if (itemName.trim() === "") {
            alert("Le nom ne peut pas être vide.");
            return;
        }

        $.ajax({
            url: "add.php",
            type: "POST",
            data: { name: itemName },
            dataType: "json",
            success: function (response) {
                if (response.success) {
                    let newItem = `<li id="item-${response.id}">
                        <span class="item-name">${response.name}</span> 
                        <button class="edit-btn" data-id="${response.id}">Modifier</button>
                        <button class="delete-btn" data-id="${response.id}">Supprimer</button>
                    </li>`;
                    $("#item-list").append(newItem);
                    $("#item-name").val(""); // Réinitialise le champ
                } else {
                    alert("Erreur : " + response.error);
                }
            }
        });
    });

    // Modification d'un élément
    $(document).on("click", ".edit-btn", function () {
        let itemId = $(this).data("id");
        let currentName = $("#item-" + itemId + " .item-name").text();
        let newName = prompt("Modifier l'élément :", currentName);

        if (newName !== null && newName.trim() !== "") {
            $.ajax({
                url: "update.php",
                type: "POST",
                data: { id: itemId, name: newName },
                dataType: "json",
                success: function (response) {
                    if (response.success) {
                        $("#item-" + itemId + " .item-name").text(newName);
                        alert("Élément mis à jour !");
                    } else {
                        alert("Erreur : " + response.error);
                    }
                }
            });
        }
    });
});
