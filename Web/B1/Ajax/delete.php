<?php

header("Content-Type: application/json");

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    if (isset($_POST["id"])) {
        $id = intval($_POST["id"]);

        try {
            $pdo = new PDO("mysql:host=localhost;dbname=test", "root", "");
            $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            $stmt = $pdo->prepare("DELETE FROM items WHERE id = ?");

            if ($stmt->execute([$id])) {
                echo json_encode(["success" => true]);
            } else {
                echo json_encode(["success" => false, "error" => "Échec de la suppression."]);
            }
        } catch (PDOException $e) {
            echo json_encode(["success" => false, "error" => $e->getMessage()]);
        }
    } else {
        echo json_encode(["success" => false, "error" => "ID manquant."]);
    }
}

