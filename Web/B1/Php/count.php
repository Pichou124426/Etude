<?php
    function compterCaracteres($nomFichier){
        if (file_exists($nomFichier)) {
            $contenu = file_get_contents($nomFichier);
            return strlen($contenu);
    }   else {
        return "Le fichier n'existe pas";
    } 
    }
    $nomFichier="login.php";
    echo compterCaracteres($nomFichier);
?>