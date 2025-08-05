<?php
include("header.php");
//redirection à la page index si l'utilisateur est déjà connecté
if (isConnected()) {
    header("Location: index.php");
}
//vérification d'un formulaire envoyé
//récupération de l'email et du mot de passe 
if (isset($_POST["email"]) && isset($_POST["password"])) {
    $email = $_POST["email"];
    $password = $_POST["password"];

//récupération d'un utilisateur à partir de l'adresse mail envoyé
//dans le but de pouvoir comparer le mot de passe à celui enregistré en BDD
    $sql = "SELECT  * FROM users WHERE email = :toto";
    $statement = $pdo->prepare($sql);
    $statement->execute(array(':toto' => $email));
    $result = $statement->fetchAll(PDO::FETCH_ASSOC);

//Si le mot de passe correspond, création de la session avec toutes les données de l'utilisateur
//fetchAll est un tableau de résultats, [0] sélectionne le premier résultat
//pour éviter de devoir sélectionner le résultat, on pourrait utiliser 'fetch' : $result['firstname']
    if (password_verify($password, $result[0]['password'])) {
        $_SESSION["firstname"] =  $result[0]['firstname'];
        $_SESSION["lastname"] =  $result[0]['lastname'];
        $_SESSION["email"] =  $result[0]['email'];
        $_SESSION["id_user"] = $result[0]["id_user"];
        header("Location: index.php");
    }
}
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <form method="POST">
        <input type="email" name="email" placeholder=" votre email">
        <input type="password" name="password" placeholder="votre mot de passe">
        <input type="submit" value="Envoyer">
    </form>
</body>

</html>