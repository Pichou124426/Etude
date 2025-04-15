<?php include("header.php"); ?>
<?php
$idUser = $_SESSION["idUser"];
$idTask = $_GET["idTask"];
$sql = "SELECT * FROM tasks WHERE idTask = :idTask AND idUser = :idUser";
$statement = $pdo->prepare($sql);
$statement->execute(array(
    ":idTask" => $idTask,
    ":idUser" => $idUser
));
$result = $statement->fetch(PDO::FETCH_ASSOC);
?>

<section class="container">
    <h2>Modifier une tâche</h2>
    <form id="editTaskForm" method="POST" action="updateTask.php">
        <input type="hidden" name="idTask" value="<?= $result['idTask'] ?>">
        <label for="titleTask">Title:</label>
        <input type="text" id="titleTask" name="titleTask" value="<?= htmlspecialchars($result['titleTask'], ENT_QUOTES, 'UTF-8') ?>" required><br><br>
        <label for="contentTask">Content:</label><br>
        <textarea id="contentTask" name="contentTask" rows="4" cols="50" required><?= htmlspecialchars($result['contentTask'], ENT_QUOTES, 'UTF-8') ?></textarea><br><br>
        <input type="submit" value="Edit">
    </form>
</section>


















<?php include("footer.php"); ?>