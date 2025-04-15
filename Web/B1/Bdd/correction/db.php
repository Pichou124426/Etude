<?php
//lien du php à la base de donnée
define("USER", "root");
define("PASSWORD", "root");
define("DSN", "mysql:host=localhost;dbname=hexagone");
//Pour Zhou : création d'un objet de la classe PDO pour se connecter à la BDD
try {
    $pdo = new PDO(DSN, USER, PASSWORD);
    echo "connexion à la bdd reussie";
} catch (PDOException $e) {
    die("Error: " . $e->getMessage());
}
?>