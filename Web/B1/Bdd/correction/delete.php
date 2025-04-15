<?php
include("header.php");
//On récupère l'ID depuis l'URL
$id = $_GET['id'];
$sql = ' DELETE FROM users WHERE id_user = :id';
$statement = $pdo->prepare($sql);
$statement->execute(
    array('id' => $id)
);
header('Location: read.php');
?>