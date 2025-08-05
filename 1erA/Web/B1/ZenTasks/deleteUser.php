<?php include("header.php"); ?>

<?php

$idUser = $_SESSION["idUser"];


if (is_numeric($idUser)) {
    $sql = 'DELETE FROM tasks WHERE  idUser = :idUser';
    $statement = $pdo->prepare($sql);
    $statement->execute([
        ':idUser' => $idUser
    ]);

    $sql = 'DELETE FROM users WHERE  idUser = :idUser';
    $statement = $pdo->prepare($sql);
    $statement->execute([
        ':idUser' => $idUser
    ]);


    disconnect();
    header('Location: myTasks.php');
    exit;
}

?>