<?php
include("header.php");

$idTask = $_SESSION["idTask"];
$idUser = $_SESSION["idUser"];

$sql = "SELECT titleTask FROM tasks WHERE idTask = :idTask AND idUser = :idUser";
$statement = $pdo->prepare($sql);
$statement->execute(
    array(
        'idTask' => $idTask,
        'idUser' => $idUser
    )
);

$task = $statement->fetch(PDO::FETCH_ASSOC);

if ($task) {
    $titleTask = htmlspecialchars($task['titleTask'], ENT_QUOTES, 'UTF-8');
} else {
    $titleTask = "Unknown Task";
}
?>

<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task completed</title>
    <script>
        function redirectToIndex() {
            const titleTask = "<?= $titleTask ?>";

            document.getElementById("message").innerText =
                `Congratulations on successfully completing the task: "${titleTask}"! Your hard work and determination have truly paid off. This achievement reflects your dedication and skills, and you should be very proud of yourself. Well done!`;

            setTimeout(() => {
                window.location.href = "index.php";
            }, 4000);
        }
    </script>
</head>

<body onload="redirectToIndex()"> <!-- Exécute la fonction redirectToIndex() lors du chargement de la page -->
    <div class="container">
        <h1 style="text-align: center; margin-top: 20px;">Congratulations task completed!</h1>
        <div id="message" style="font-size: 24px; text-align: center; margin-top: 20px;"></div>
    </div>

    <!-- Inclure le footer -->
    <?php include("footer.php"); ?>

</body>

</html>