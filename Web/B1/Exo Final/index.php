<?php
include("header.php");

?>



<section>
    <h2> Bienvenue sur le site </h2>
    <p> Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptates. </p>
    <p> Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptates. </p>
    <?php
    if (isConnected()): ?>
        <div class="mesPosts">
            <h3> Mes Posts </h3>
            <?php
            $id_user = $_SESSION["id_user"];
            $sql = "SELECT title,content FROM blog WHERE id_user = :id_user";
            $statement = $pdo->prepare($sql);
            $statement->execute(array(':id_user' => $id_user));
            $result = $statement->fetchAll(PDO::FETCH_ASSOC);
            ?>
            <?php foreach ($result as $post): ?>
                <div class="post">
                    <h4> <?= $post["title"] ?> </h4>
                    <p> <?= $post["content"] ?> </p>
                </div>
            <?php endforeach; ?>
        </div>
    <?php endif; ?>





</section>

<?php include("footer.php"); ?>