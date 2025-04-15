<?php
include("header.php");
$idTask = $_GET["idTask"];
$idUser = $_SESSION["idUser"];


$sql = 'UPDATE tasks SET completed = 1 WHERE idTask = :idTask and idUser = :idUser';
$statement = $pdo->prepare($sql);
$statement->execute(
    array(
        'idTask' => $idTask,
        'idUser' => $idUser
    )
);
$_SESSION["idTask"] = $idTask;
header('Location: sucessCompletedTask.php');
