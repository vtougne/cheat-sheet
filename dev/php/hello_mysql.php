<?php
$host = 'localhost';
$db   = 'testdb';
$user = 'root';
$pass = '';
$charset = 'utf8mb4';

// DSN = Data Source Name
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";

// Options PDO
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,  // Exceptions en cas d'erreur
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,        // Résultat sous forme de tableau associatif
    PDO::ATTR_EMULATE_PREPARES   => false,                   // Préparation réelle (sécurité)
];

try {
    $pdo = new PDO($dsn, $user, $pass, $options);

    $stmt = $pdo->query("SELECT id, name, email FROM users");

    echo "<h1>Liste des utilisateurs :</h1>";
    echo "<ul>";
    while ($row = $stmt->fetch()) {
        echo "<li>{$row['id']} - {$row['name']} ({$row['email']})</li>";
    }
    echo "</ul>";

} catch (\PDOException $e) {
    echo "Erreur de connexion : " . $e->getMessage();
}
?>
