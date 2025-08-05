<?php include("header.php"); ?>

<?php
if (isset($_GET["idTask"])) {
    $idTask = $_GET["idTask"];
    $idUser = $_SESSION["idUser"];

    // Vérifie que 'idTask' est un entier valide
    if (is_numeric($idTask)) {
        $sql = 'DELETE FROM tasks WHERE idTask = :idTask AND idUser = :idUser';
        $statement = $pdo->prepare($sql);
        $statement->execute([
            ':idTask' => $idTask,
            ':idUser' => $idUser
        ]);


        header('Location: myTasks.php');
        exit;
    }
}
?>