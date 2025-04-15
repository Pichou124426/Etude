<?php
include("header.php");
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Page d'accueil</title>
</head>

<body>
    <?php if (!$connected) : ?>
        <h1>Bienvenue</h1>
        <a href="register.php">S'inscrire</a>
        <a href="login.php">Se connecter</a>
    <?php else : ?>
        <h1>Bienvenue <?php echo $_SESSION["firstname"]?></h1>
        <a href="disconnect.php">Se déconnecter</a>
        <a href="read.php">Tableau administrateur</a>
    <?php endif; ?>
</body>

</html>