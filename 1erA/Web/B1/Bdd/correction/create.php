<?php
include("header.php");

//insertion des données reçues depuis un formulaire dans la table
$mot_de_passe = password_hash($_POST["password"], PASSWORD_DEFAULT);
$email = $_POST['email'];
$nom = $_POST['nom'];
$prenom = $_POST['prenom'];
$email = $_POST['email'];
$sql = "INSERT INTO users (firstname,lastname,email,password) VALUES (:prenom, :nom,  :email, :mot_de_passe)";

$statement = $pdo->prepare($sql);
$statement->execute(array(":mot_de_passe" => $mot_de_passe, ":email" => $email, ":nom" => $nom, ":prenom" => $prenom));
session_start();
//insertion des données dans les variables de session
$lastid = $pdo->lastInsertId();
$_SESSION["firstname"] =  $prenom;
$_SESSION["lastname"] =  $nom;
$_SESSION["email"] =  $email;
$_SESSION["id_user"] = $lastid;
header("Location: index.php");
?>