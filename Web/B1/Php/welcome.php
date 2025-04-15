<?php  
    session_start();
    echo "Bienvenue, " . $_SESSION["nom"];
    if (isset($_POST['logout'])) {
    
        session_unset(); 
        session_destroy(); 
        header("Location: login.php");
    }
?>

<form method="post">
    <button type="submit" name="logout">Déconnexion</button>
</form>