<?php
header("Content-Type: application/json");

if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST["id"]) && isset($_POST["name"])) {
    try {
        $pdo = new PDO("mysql:host=localhost;dbname=test", "root", "");
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        $id = intval($_POST["id"]);
        $name = trim($_POST["name"]);

        if ($name === "") {
            echo json_encode(["success" => false, "error" => "Le nom ne peut pas être vide."]);
            exit;
        }

        $stmt = $pdo->prepare("UPDATE items SET name = ? WHERE id = ?");
        if ($stmt->execute([$name, $id])) {
            echo json_encode(["success" => true]);
        } else {
            echo json_encode(["success" => false, "error" => "Échec de la mise à jour."]);
        }
    } catch (PDOException $e) {
        echo json_encode(["success" => false, "error" => $e->getMessage()]);
    }
}
?>
