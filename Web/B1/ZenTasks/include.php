<?php
function isConnected()
{
    if (isset($_SESSION["idUser"])) {
        return true;
    }
    return false;
}

function getOut()
{
    if (!isConnected()) {
        header("location: index.php");
    }
}


function disconnect()
{
    session_start();
    session_destroy();
    header("Location: index.php");
}
