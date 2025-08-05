<form id="login" method="POST">
    Nom d'utillisateur :<input type="text" name="nom" placeholder="Inserer votre nom " required />
    <br>
    Mots de passe :<input type="password" name="password" placeholder="Saisir votre mot de passe" required>
    <button type="submit" name="connexion">Connexion </button>
</form>

<?php 
session_start();

    if ($_SERVER["REQUEST_METHOD"]=="POST") {
        $_SESSION["nom"] = $_POST['nom'];
        $password = $_POST['password'];
        $password = password_hash($password,PASSWORD_DEFAULT);
       
        
        if (($_SESSION["nom"]!=null)) {
            if (!headers_sent()) {
                header("Location: welcome.php");
            } else {
                echo "Impossible de rediriger, les en-têtes HTTP ont déjà été envoyés.";
            }
    };};

?>

