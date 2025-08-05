<?php include("header.php"); ?>


<?php
if ($_SERVER["REQUEST_METHOD"] == "POST" and (isset($_POST["email"]) and isset($_POST["password"]))) {
    $email = $_POST['email'];
    $password = $_POST['password'];
    $sql = "SELECT * FROM users WHERE email = :email";
    $statement = $pdo->prepare($sql);
    $statement->execute(
        array(
            ':email' => $email
        )
    );
    $user = $statement->fetch();
    if ($user) {
        if (password_verify($password, $user['password'])) {
            echo "Bienvenue " . $user['username'];
            $_SESSION["username"] =  $user['username'];
            $_SESSION["email"] =  $user['email'];
            $_SESSION["id_user"] = $user['id_user'];

            header("Location: index.php");
        } else {
            echo "Mot de passe incorrect";
        }
    } else {
        echo "Utilisateur non trouvé";
    }
};
?>

<h1>Connexion</h1>
<div id="Formulaire">
    <form action="login.php" method="post">
        <label for="email">Email</label>
        <input type="email" name="email" id="email" required>
        <label for="password">Mot de passe</label>
        <input type="password" name="password" id="password" required>
        <button type="submit">Connexion</button>
        <a href="register.php">Pas encore inscrit ?</a>
    </form>
</div>
<?php include("footer.php"); ?>