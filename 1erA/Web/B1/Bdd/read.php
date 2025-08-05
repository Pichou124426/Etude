<?php
$host = "localhost";
$user = "root";
$password = "";
$database = "hexagone";

$conn = new mysqli($host, $user, $password, $database);

if ($conn->connect_error) {
    die("Erreur de connexion à la base de donnée." . $conn->connect_error);
}

$sql = "SELECT * FROM users";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
    echo "<table border='1'>
        <tr>
            <th>ID</th>    
            <th>firstname</th>    
            <th>lastname</th>    
            <th>email</th>
        </tr>";
    while ($row = $result->fetch_assoc()) {
        echo "<table border='1'>
        <tr>
                <td>" . $row["id_user"] . " </td>
                <td>" . $row["firstname"] . " </td>
                <td>" . $row["lastname"] . " </td>
                <td>" . $row["email"] . " </td>
            </tr>";
    }
    echo "</table>";
} else {
    echo "Aucun utilisateur trouvé. ";
}

$conn->close();
