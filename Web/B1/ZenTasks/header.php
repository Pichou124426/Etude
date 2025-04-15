<?php
session_start();
include("database.php");
include("include.php");

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ZenTask : The task manager that relaxes you!</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>


    <nav>
        <div style="display:flex;margin-left:10px; size: 25%;">
            <img src="logo.png" alt="ZenTask Logo" class="logo">
            <h1> ZenTasks</h1>
        </div>
        <div style="margin: auto;size: 50%;align-content:center;">
            <a href="index.php">Home</a>
            <a href="myTasks.php">My Tasks</a>
            <a href="taskStatus.php">Task Status</a>
            <a href="about.php">About</a>
            <a href="support.php">Support</a>
        </div>
        <div class="login" style="size: 25%;">
            <?php if (isConnected()) : ?>
                <a href="myProfil.php">My Profil</a>
            <?php else : ?>
                <a href="login.php">Login</a>
                <a href="register.php">Sign Up</a>
            <?php endif; ?>
        </div>
    </nav>