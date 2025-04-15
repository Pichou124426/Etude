<?php
include 'connexionBdd.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $firstname = $_POST['firstName'];
    $lastname = $_POST['lastName'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    $password = password_hash($password, PASSWORD_DEFAULT);

    if ($firstname != null and $lastname != null and $email != null and $password != null) {
        echo " Bienvenue $firstname, <br>";
        $sql = "INSERT INTO users(firstname,lastname,email,password) VALUES (:firstname,:lastname,:email,:password)";
        $statement = $pdo->prepare($sql);

        $statement->execute(
            array(
                ':firstname' => $firstname,
                ':lastname' => $lastname,
                ':email' => $email,
                ':password' => $password
            )
        );
    } else {
        echo "Veuillez saisir toute les informations avant d'envoyer svp";
    };
}
