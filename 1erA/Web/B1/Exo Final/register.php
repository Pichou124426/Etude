<?php include("header.php"); ?>
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST" and (isset($_POST["username"]) and isset($_POST["email"]) and isset($_POST["password"])) and isset($_POST["password2"])) {
    $username = $_POST['username'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    $password2 = $_POST['password2'];
    if ($password == $password2) {
        $password = password_hash($password, PASSWORD_DEFAULT);
        $sql = "INSERT INTO users(username,email,password) VALUES (:username,:email,:password)";
        $statement = $pdo->prepare($sql);
        $statement->execute(
            array(
                ':username' => $username,
                ':email' => $email,
                ':password' => $password
            )
        );
        echo "Bienvenue $username, <br>";


        $lastid = $pdo->lastInsertId();
        $_SESSION["username"] =  $username;
        $_SESSION["email"] =  $email;
        $_SESSION["id_user"] = $lastid;

        header("Location: index.php");
    } else {
        echo "Les mots de passe ne correspondent pas";
    }
}
?>

<h1>Inscription</h1>
<p>Vous avez déjà un compte ? <a href="login.php">Connectez-vous</a></p>
<form action="register.php" method="post">

    <label for="username">Username</label>
    <input type="text" name="username" id="username" required>
    <label for="email">Email</label>
    <input type="email" name="email" id="email" required>
    <label for="password">Mot de passe</label>
    <input type="password" name="password" id="password" required>
    <label for="password2">Confirmer le mot de passe</label>
    <input type="password" name="password2" id="password2" required>
    <button type="submit">Inscription</button>
</form>

<?php include("footer.php"); ?>