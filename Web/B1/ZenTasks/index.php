<?php include("header.php"); ?>
<div class="container">
    <h1>ZenTasks</h1>
    <p>ZenTasks is a simple task management application that allows you to create, view, and delete tasks. It is designed to help you stay organized and focused on your work.</p>
    <p>To get started, you can create a new task by clicking the "My task" button below. You can also view your existing tasks and delete them if needed.</p>
    <p>ZenTasks is built using PHP and MySQL, and it is designed to be lightweight and easy to use. It is perfect for individuals or small teams who need a simple task management solution.</p>
    <p>We hope you enjoy using ZenTasks!</p>
    <div class="button-container">
        <?php
        if (isset($_SESSION['username'])) {
            echo '<p>Welcome, <span class="username-highlight">' . htmlspecialchars($_SESSION['username']) . '</span>!</p>';
        } else {
            echo '<p>Please <a href="login.php">login</a> to access your tasks.</p>';
        }
        ?>


    </div>
</div>





















<?php include("footer.php"); ?>