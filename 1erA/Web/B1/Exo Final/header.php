<?php
include("database.php");
session_start();
function isConnected()
{
    if (isset($_SESSION["id_user"])) {
        return true;
    }
    return false;
}
?>


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercice Final</title>
    <link rel="stylesheet" href="index.css">
</head>

<body>
    <nav>
        <h1> Le nom du site </h1>
        <ul>
            <li><a href="index.php">Accueil</a></li>
            <li><a href="about.php">A propos</a></li>
            <li><a href="contact.php">Contact</a></li>
        </ul>
        <div class="login">
            <?php
            if (isConnected()) : ?>

                <a href="logout.php">Déconnexion</a>
                <a href="createPost.php">Créer un post</a>
            <?php else : ?>
                <a href="login.php">Connexion</a>
                <a href="register.php">Inscription</a>
            <?php endif; ?>
        </div>
    </nav>