<?php
header("Content-Type: application/json");

if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST["name"])) {
    try {
        $pdo = new PDO("mysql:host=localhost;dbname=test", "root", "");
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        $name = trim($_POST["name"]);
        if ($name === "") {
            echo json_encode(["success" => false, "error" => "Le nom est vide."]);
            exit;
        }

        $stmt = $pdo->prepare("INSERT INTO items (name) VALUES (?)");
        $stmt->execute([$name]);
        $id = $pdo->lastInsertId();

        echo json_encode(["success" => true, "id" => $id, "name" => htmlspecialchars($name)]);
    } catch (PDOException $e) {
        echo json_encode(["success" => false, "error" => $e->getMessage()]);
    }
}
?>
