<?php
include("header.php");

try {
    $idUser = $_SESSION["idUser"];

    // Requête SQL pour récupérer l'utilisateur connecté
    $sql = "SELECT * FROM users WHERE idUser = :idUser";
    $statement = $pdo->prepare($sql); // Préparation de la requête
    $statement->execute([':idUser' => $idUser]); // Exécution avec les paramètres

    // Récupérer une seule ligne
    $result = $statement->fetch(PDO::FETCH_ASSOC);

    // Vérifiez si un utilisateur est trouvé
    if (!$result) {
        echo "<p>No user found.</p>";
        exit; // Arrête le script si aucun utilisateur trouvé
    }
} catch (PDOException $e) {
    die("Erreur PDO : " . htmlspecialchars($e->getMessage(), ENT_QUOTES, 'UTF-8'));
}
?>

<!DOCTYPE html>
<html>

<head>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }

        table,
        th,
        td {
            border: 1px solid black;
        }

        th {
            background-color: #f2f2f2;
        }

        td {
            text-align: left;
            padding: 8px;
        }
    </style>
</head>

<body>
    <div class="container">
        <table border="3">
            <tr>
                <th>Username</th>
                <th>FirstName</th>
                <th>Lastname</th>
                <th>Email</th>
                <th>Phone Number</th>
                <th colspan="2">Action</th>
            </tr>
            <tr>
                <td><?= htmlspecialchars($result['username'] ?? 'N/A', ENT_QUOTES, 'UTF-8') ?></td> <!-- Si null, affiche N/A -->
                <td><?= htmlspecialchars($result['firstName'] ?? 'N/A', ENT_QUOTES, 'UTF-8') ?></td>
                <td><?= htmlspecialchars($result['lastName'] ?? 'N/A', ENT_QUOTES, 'UTF-8') ?></td>
                <td><?= htmlspecialchars($result['email'] ?? 'N/A', ENT_QUOTES, 'UTF-8') ?></td>
                <td><?= htmlspecialchars($result['phoneNumber'] ?? 'N/A', ENT_QUOTES, 'UTF-8') ?></td>
                <td><a href="editUser.php?id=<?= htmlspecialchars($result['idUser'] ?? '', ENT_QUOTES, 'UTF-8') ?>">Edit</a></td>
                <td><a href="deleteUser.php?id=<?= htmlspecialchars($result['idUser'] ?? '', ENT_QUOTES, 'UTF-8') ?>">Delete</a></td>
            </tr>
        </table>
    </div>
    <form action="logout.php" method="POST">
        <button type="submit" class="logout-btn">Logout</button>
    </form>



<?php include('footer.php');?>