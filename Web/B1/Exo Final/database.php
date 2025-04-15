<?php
define("USER", 'root');
define("PASSWORD", '');
define("DNS", 'mysql:host=localhost;dbname=ExoFinal');

try {
    $pdo = new PDO(DNS, USER, PASSWORD);
} catch (PDOException $e) {
    die("Error ! : " . $e->getMessage());
}
?>
