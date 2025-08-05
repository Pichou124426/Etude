<?php include("header.php");
if (!isConnected()) {
    header('Location: login.php');
    exit;
}
?>
<section class="container">
    <h2>Task Status</h2>
    <div class="taskStatus">
        <h3> Completed Tasks </h3>
        <div class="taskCompleted">
            <?php
            $idUser = $_SESSION["idUser"];
            $sql = "SELECT * FROM tasks WHERE idUser = :idUser AND completed = 1 ";
            $statement = $pdo->prepare($sql);
            $statement->execute(array(':idUser' => $idUser));
            $result = $statement->fetchAll(PDO::FETCH_ASSOC);
            ?>
            <?php
            if (!empty($result)) { 
                foreach ($result as $task) : ?>
                    <div class="task">
                        <h4> <?= htmlspecialchars($task["titleTask"], ENT_QUOTES, 'UTF-8') ?> </h4>
                        <p> <?= htmlspecialchars($task["contentTask"], ENT_QUOTES, 'UTF-8') ?> </p>
                    </div>
            <?php endforeach;
            } else {
                echo "<p>No tasks found.</p>"; 
            }
            ?>

        </div>
        <h3> Uncompleted Tasks </h3>
        <div class="taskUncompleted">
            <?php
            $idUser = $_SESSION["idUser"];
            $sql = "SELECT * FROM tasks WHERE idUser = :idUser AND completed = 0 ";
            $statement = $pdo->prepare($sql);
            $statement->execute(array(':idUser' => $idUser));
            $result = $statement->fetchAll(PDO::FETCH_ASSOC);
            ?>
            <?php
            if (!empty($result)) { 
                foreach ($result as $task) : ?>
                    <div class="task">
                        <h4> <?= htmlspecialchars($task["titleTask"], ENT_QUOTES, 'UTF-8') ?> </h4>
                        <p> <?= htmlspecialchars($task["contentTask"], ENT_QUOTES, 'UTF-8') ?> </p>
                    </div>
            <?php endforeach;
            } else {
                echo "<p>No tasks found.</p>"; 
            }
            ?>
</section>


<?php
$idUser = $_SESSION["idUser"];


$sqlTotal = "SELECT COUNT(*) AS total FROM tasks WHERE idUser = :idUser";
$stmtTotal = $pdo->prepare($sqlTotal);
$stmtTotal->execute([':idUser' => (int)$idUser]);
$totalTasks = $stmtTotal->fetchColumn();


$sqlCompleted = "SELECT COUNT(*) AS completed FROM tasks WHERE idUser = :idUser AND completed = 1";
$stmtCompleted = $pdo->prepare($sqlCompleted);
$stmtCompleted->execute([':idUser' => (int)$idUser]);
$completedTasks = $stmtCompleted->fetchColumn();


$sqlUncompleted = "SELECT COUNT(*) AS uncompleted FROM tasks WHERE idUser = :idUser AND completed = 0";
$stmtUncompleted = $pdo->prepare($sqlUncompleted);
$stmtUncompleted->execute([':idUser' => (int)$idUser]);
$uncompletedTasks = $stmtUncompleted->fetchColumn();


$percentageCompleted = $totalTasks > 0 ? round(($completedTasks / $totalTasks) * 100, 2) : 0;
?>
<section class="container">

    <div class="static">
        <h3> Static </h3>
        <p>Total Tasks: <?= htmlspecialchars($totalTasks, ENT_QUOTES, 'UTF-8') ?></p>
        <p>Completed Tasks: <?= htmlspecialchars($completedTasks, ENT_QUOTES, 'UTF-8') ?></p>
        <p>Uncompleted Tasks: <?= htmlspecialchars($uncompletedTasks, ENT_QUOTES, 'UTF-8') ?></p>
        <p>Percentage of Completed Tasks: <?= htmlspecialchars($percentageCompleted, ENT_QUOTES, 'UTF-8') ?>%</p>
    </div>
</section>







<?php include("footer.php"); ?>