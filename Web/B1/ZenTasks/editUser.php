<?php include("header.php"); ?>
<?php
$idUser = $_SESSION["idUser"];
$sql = "SELECT * FROM users WHERE  idUser = :idUser";
$statement = $pdo->prepare($sql);
$statement->execute(array(

    ":idUser" => $idUser
));
$result = $statement->fetch(PDO::FETCH_ASSOC);
?>

<section class="container">

    <h2>Edit my User </h2>
    <form id="editUser" method="POST" action="updateUser.php">
        <input type="hidden" name="idUser" value="<?= $result['idUser'] ?>">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" value="<?= htmlspecialchars($result['username'], ENT_QUOTES, 'UTF-8') ?>" required><br><br>
        <label for="firstName">Firstname:</label>
        <input type="text" id="firstName" name="firstName" value="<?= htmlspecialchars($result['firstName'], ENT_QUOTES, 'UTF-8') ?>" required><br><br>
        <label for="lastName">Name:</label>
        <input type="text" id="lastName" name="lastName" value="<?= htmlspecialchars($result['lastName'], ENT_QUOTES, 'UTF-8') ?>" required><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" value="<?= htmlspecialchars($result['email'], ENT_QUOTES, 'UTF-8') ?>" required><br><br>
        <label for="phoneNumber">Phone Number:</label>
        <input type="tel" id="phoneNumber" name="phoneNumber" value="<?= htmlspecialchars($result['phoneNumber'], ENT_QUOTES, 'UTF-8') ?>" required><br><br>
        <input type="submit" value="Edit">

    </form>
</section>


















<?php include("footer.php"); ?>