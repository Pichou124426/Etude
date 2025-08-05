<?php include("header.php"); ?>
<?php
if (!isConnected()) {
    header('Location: login.php');
    exit;
}
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (!empty($_POST["titleTask"]) && !empty($_POST["contentTask"])) {
        $idUser = $_SESSION["idUser"];
        $titleTask = htmlspecialchars($_POST['titleTask'], ENT_QUOTES, 'UTF-8');
        $contentTask = htmlspecialchars($_POST['contentTask'], ENT_QUOTES, 'UTF-8');
        $sql = "INSERT INTO tasks(idUser,titleTask,contentTask) VALUES (:idUser,:titleTask,:contentTask)";
        $statement = $pdo->prepare($sql);
        $statement->execute(
            array(
                ':idUser' => $idUser,
                ':titleTask' => $titleTask,
                ':contentTask' => $contentTask,
            )
        );
        header('Location: myTasks.php');
        exit;
    }
}
?>


<?php if (isConnected()) : ?>
    <section class="container">
        <h2> My Tasks </h2>
        <div class="myTasks">
            <?php
            $idUser = $_SESSION["idUser"];
            $sql = "SELECT * FROM tasks WHERE idUser = :idUser AND completed = 0 "; // Filtre sur les tâches non complétées
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
                        <a href="deleteTask.php?idTask=<?= htmlspecialchars($task["idTask"], ENT_QUOTES, 'UTF-8') ?>">Delete</a>
                        <a href="editTask.php?idTask=<?= htmlspecialchars($task["idTask"], ENT_QUOTES, 'UTF-8') ?>">Edit</a>
                        <a href="taskCompleted.php?idTask=<?= htmlspecialchars($task["idTask"], ENT_QUOTES, 'UTF-8') ?>">Completed</a>
                    </div>
            <?php endforeach;
            } else {
                echo "<p>No tasks found.</p>";
            }
            ?>

        </div>
    </section>
    <section class="container">
        <div class=addTask>
            <h2> Add a Task </h2>
            <form id="taskForm" method="POST">
                <label for="titleTask">Title:</label>
                <input type="text" id="titleTask" name="titleTask" required><br><br>
                <label for="contentTask">Content:</label><br>
                <textarea id="contentTask" name="contentTask" rows="4" cols="50" required></textarea><br><br>
                <input type="submit" value="Add">
            </form>
        <?php endif; ?>
        </div>
    </section>
    <section class="container">
        <div=quotes>
            <h2> Quote of the day </h2>
            <p> " Success is not final, failure is not fatal: It is the courage to continue that counts." </p>
            </div>
    </section>


    <?php include("footer.php"); ?>