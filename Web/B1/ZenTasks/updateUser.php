<?php
include("header.php");
$idUser = $_POST["idUser"];
$username = $_POST["username"];
$firstName = $_POST["firstName"];
$lastName = $_POST["lastName"];
$email = $_POST["email"];
$phoneNumber = $_POST["phoneNumber"];

$sql = 'UPDATE users SET username = :username, firstName = :firstName, lastName = :lastName, email = :email, phoneNumber = :phoneNumber WHERE idUser = :idUser';
$statement = $pdo->prepare($sql);
$statement->execute(
    array(
        'idUser' => $idUser,
        'username' => $username,
        'firstName' => $firstName,
        'lastName' => $lastName,
        'email' => $email,
        'phoneNumber' => $phoneNumber
    )
);

header('Location: sucessUpdateUser.php');
