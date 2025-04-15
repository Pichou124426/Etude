<?php
include("header.php");

if (isConnected()) {
    header("Location: index.php");
    exit;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST["email"]) && isset($_POST["password"])) {
        $email = trim($_POST["email"]); // Supprime les espaces inutiles
        $password = $_POST["password"];

        try {

            $sql = "SELECT * FROM users WHERE email = :email";
            $statement = $pdo->prepare($sql);
            $statement->execute([':email' => $email]);

            $result = $statement->fetch(PDO::FETCH_ASSOC);


            if (!$result) {
                $errorMessage = "Invalid email or password.";
            } else {

                if (password_verify($password, $result['password'])) {

                    $_SESSION["username"] = $result['username'];
                    $_SESSION["email"] = $result['email'];
                    $_SESSION["idUser"] = $result["idUser"];
                    header("Location: index.php");
                    exit;
                } else {
                    $errorMessage = "Invalid email or password.";
                }
            }
        } catch (PDOException $e) {
            $errorMessage = "Database error: " . htmlspecialchars($e->getMessage(), ENT_QUOTES, 'UTF-8');
        }
    } else {
        $errorMessage = "Please fill in all required fields.";
    }
}
?>
<div class="container">
    <form id="loginForm" method="POST">
        <h1>Login</h1>

        <p>Welcome back! Please enter your credentials to access your account.</p>
        <?php if (isset($errorMessage)) : ?>
            <p style="color: red;"><?= htmlspecialchars($errorMessage, ENT_QUOTES, 'UTF-8') ?></p>
        <?php endif; ?>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required placeholder="Enter your email"><br><br>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required placeholder="Enter your password"><br><br>

        <input type="submit" value="Login">
        <p>Don't have an account? <a href="register.php">Sign Up</a></p>
    </form>

</div>
<?php include("footer.php"); ?>