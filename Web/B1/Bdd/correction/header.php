<?php
include("db.php");
session_start();
//Vérifier si un utilisateur est connecté (bool)
function isConnected()
{
    if (isset($_SESSION["id_user"])) {
        return true;
    }
    return false;
}
//Redirige à la page index si un utilisateur n'est pas connecté
function getOut()
{
    if (!isConnected()) {
        header("location: index.php");
    }
}
?>