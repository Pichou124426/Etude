<?php
include("header.php");

$idUser = $_SESSION["idUser"];
$sql = "SELECT username FROM users WHERE idUser = :idUser";
$statement = $pdo->prepare($sql);
$statement->execute(
    array(
        'idUser' => $idUser
    )
);

$username = $statement->fetch(PDO::FETCH_ASSOC);

?>

<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task completed</title>
    <script>
        function redirectToIndex() {

            const username = "<?= htmlspecialchars($username['username'], ENT_QUOTES, 'UTF-8') ?>"; /* obtenir la valeur réelle */



            document.getElementById("message").innerText =
                ` Your changes for "${username}" are being processed, and you will be redirected to your profile page shortly. Thank you for your patience!`;
            setTimeout(() => {
                window.location.href = "myProfil.php";
            }, 4000);
        }
    </script>
</head>

<body onload="redirectToIndex()"> <!-- Exécute la fonction redirectToIndex() lors du chargement de la page -->
    <div class="container">
        <h1 style="text-align: center; margin-top: 20px;">Your changes are in progress.</h1>
        <div id="message" style="font-size: 24px; text-align: center; margin-top: 20px;"></div>
    </div>
</body>

</html>

<?php include("footer.php"); ?>