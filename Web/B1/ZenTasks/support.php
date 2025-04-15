<?php include("header.php");
if (!isConnected()) {
    header('Location: login.php');
    exit;
}
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (!empty($_POST["title"]) && !empty($_POST["content"])) {
        $idUser = $_SESSION["idUser"];
        $title = htmlspecialchars($_POST['title'], ENT_QUOTES, 'UTF-8');
        $content = htmlspecialchars($_POST['content'], ENT_QUOTES, 'UTF-8');
        $sql = "INSERT INTO support(idUser,title,content) VALUES (:idUser,:title,:content)";
        $statement = $pdo->prepare($sql);
        $statement->execute(
            array(
                ':idUser' => $idUser,
                ':title' => $title,
                ':content' => $content,
            )
        );
        header('Location: supportSucess.php');
        exit;
    }
}
?>

<section class="container">
    <form id="supportForm" method="POST">
        <h1>Support</h1>
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required><br><br>
        <label for="content">Content:</label><br>
        <textarea id="content" name="content" rows="4" cols="50" required></textarea><br><br>
        <input type="submit" value="Submit">
    </form>
</section>
<?php include("footer.php"); ?>