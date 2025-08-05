<?php
define("USER", 'root');
define("PASSWORD", 'userpw');
define("DNS", 'mysql:host=localhost;dbname=hexagone');

try {
    $pdo = new PDO(DNS, USER, PASSWORD);
    echo "Connexion reussie";
} catch (PDOException $e) {
    die("Error ! : " . $e->getMessage());
}
