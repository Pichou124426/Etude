<?php include("header.php"); ?>

<?php


if (isset($_SESSION["username"])) {
    header("Location: index.php");
    exit();
}

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["username"], $_POST["firstName"], $_POST["lastName"], $_POST["email"], $_POST["password"], $_POST["password2"], $_POST["phoneNumber"])) {
    $username = trim($_POST["username"]);
    $firstName = trim($_POST["firstName"]);
    $lastName = trim($_POST["lastName"]);
    $email = trim($_POST["email"]);
    $phoneNumber = trim($_POST["phoneNumber"]);
    $password = $_POST["password"];
    $password2 = $_POST["password2"];


    $sqlCheck = "SELECT * FROM users WHERE email = :email OR phoneNumber = :phoneNumber";
    $stmtCheck = $pdo->prepare($sqlCheck);
    $stmtCheck->execute([
        ':email' => $email,
        ':phoneNumber' => $phoneNumber
    ]);
    $existingUser = $stmtCheck->fetch(PDO::FETCH_ASSOC);

    if ($existingUser) {
        if ($existingUser["email"] === $email) {
            echo "<p style='color:red;'>This email address is already in use.</p>";
        } elseif ($existingUser["phoneNumber"] === $phoneNumber) {
            echo "<p style='color:red;'>This phone number is already in use.</p>";
        }
    } elseif ($password === $password2) {

        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);


        $sqlInsert = "INSERT INTO users(username, firstName, lastName, email, phoneNumber, password) VALUES (:username, :firstName, :lastName, :email, :phoneNumber, :password)";
        $stmtInsert = $pdo->prepare($sqlInsert);
        $stmtInsert->execute([
            ':username' => $username,
            ':firstName' => $firstName,
            ':lastName' => $lastName,
            ':email' => $email,
            ':phoneNumber' => $phoneNumber,
            ':password' => $hashedPassword
        ]);


        $_SESSION["username"] = $username;
        $_SESSION["email"] = $email;
        $_SESSION["idUser"] = $pdo->lastInsertId();

        header("Location: index.php");
        exit();
    } else {
        echo "<p style='color:red;'>Passwords do not match.</p>";
    }
}
?>
<div class="container">
    <form id="registerForm" method="POST">
        <h1>Register</h1>

        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required placeholder="Enter your username" pattern="[A-Za-z0-9_]{3,20}" title="Username must be 3-20 characters long and can include letters, numbers, and underscores."><br><br>

        <label for="firstName">First Name:</label>
        <input type="text" id="firstName" name="firstName" required placeholder="Enter your first name" pattern="[A-Za-zÀ-ÿ]+" title="Please enter a valid first name."><br><br>

        <label for="lastName">Last Name:</label>
        <input type="text" id="lastName" name="lastName" required placeholder="Enter your last name" pattern="[A-Za-zÀ-ÿ]+" title="Please enter a valid last name."><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required placeholder="Enter your email"><br><br>

        <label for="phoneNumber">Phone Number:</label>
        <input type="tel" id="phoneNumber" name="phoneNumber" required placeholder="Enter your phone number" pattern="[0-9]{10}" title="Please enter a valid phone number."><br><br>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required placeholder="Enter your password"><br><br>

        <label for="password2">Confirm Password:</label>
        <input type="password" id="password2" name="password2" required placeholder="Confirm your password"><br><br>

        <input type="submit" value="Sign Up">

        <p>Already registered? <a href="login.php">Log in here</a></p>
        <p>By signing up, you agree to our <a href="terms.php">Terms of Use</a>.</p>
    </form>
</div>
<?php include("footer.php"); ?>