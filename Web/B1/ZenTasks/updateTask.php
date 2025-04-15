<?php
include("header.php");
$idTask = $_POST["idTask"];
$titleTask = $_POST["titleTask"];
$contentTask = $_POST["contentTask"];

$sql = 'UPDATE tasks SET titleTask = :titleTask, contentTask = :contentTask WHERE idTask = :idTask';
$statement = $pdo->prepare($sql);
$statement->execute(
    array(
        'titleTask' => $titleTask,
        'contentTask' => $contentTask,
        'idTask' => $idTask
    )
);
header('Location: myTasks.php');
