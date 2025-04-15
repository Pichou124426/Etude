<?php
$pdo = new PDO("mysql:host=localhost;dbname=test", "root", "", [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, //  PDO::ERRMODE_EXCEPTION	Lève une exception (PDOException) en cas d'erreur SQL, facilitant le débogage et améliorant la sécurité.
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC // Permet de mettre le mode de fetch par défaut à PDO::FETCH_ASSOC => Evite la redondance
]);

$stmt = $pdo->prepare("SELECT * FROM items ORDER BY id DESC");
$stmt->execute();
$items = $stmt->fetchAll();
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestion des éléments</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script defer src="script.js"></script>
</head>
<body>
<h1>Gestion des éléments</h1>

<!-- Formulaire d'ajout -->
<form id="add-form">
    <input type="text" id="item-name" placeholder="Nom de l'élément">
    <button type="submit">Ajouter</button>
</form>

<h2>Liste des éléments</h2>
<ul id="item-list">
    <?php foreach ($items as $item): ?>
        <li id="item-<?= $item['id'] ?>">
            <span class="item-name"><?= htmlspecialchars($item['name']) ?></span>
            <button class="edit-btn" data-id="<?= $item['id'] ?>">Modifier</button>
            <button class="delete-btn" data-id="<?= $item['id'] ?>">Supprimer</button>
        </li>
    <?php endforeach; ?>
</ul>
</body>
</html>
