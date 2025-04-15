<?php
include("header.php");

if ($_SERVER["REQUEST_METHOD"] == "POST" and (isset($_POST["title"]) and isset($_POST["content"]))) {
    $id_user = $_SESSION["id_user"];
    $title = htmlspecialchars($_POST['title'], ENT_QUOTES, 'UTF-8');
    $content = htmlspecialchars($_POST['content'], ENT_QUOTES, 'UTF-8');;
    $sql = "INSERT INTO blog(id_user,title,content) VALUES (:id_user,:title,:content)";
    $statement = $pdo->prepare($sql);
    $statement->execute(
        array(
            ':id_user' => $id_user,
            ':title' => $title,
            ':content' => $content,
        )
    );
    echo "Le post: $title a été créé <br>";
}
?>

<form action="createPost.php" method="post">
    <input type="text" name="title" placeholder="Title">
    <input type="text" name="content" placeholder="Content">
    <input type="submit" value="Create Post">
</form>

<?php include("footer.php"); ?>