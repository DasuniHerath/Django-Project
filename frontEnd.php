<?php
// MySQL connection parameters
$db_config = array(
    'host' => 'localhost',
    'database' => 'world',
    'user' => 'root',
    'password' => 'root'
);

try {
    // Connect to MySQL
    $connection = new PDO("mysql:host={$db_config['host']};dbname={$db_config['database']}", $db_config['user'], $db_config['password']);
    $connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Function to fetch table structure for a given table
    function visualizeTableStructure($connection, $tableName) {
        $query = "DESCRIBE $tableName";
        $stmt = $connection->prepare($query);
        $stmt->execute();
        $tableStructure = $stmt->fetchAll(PDO::FETCH_ASSOC);

        // Render table structure
        echo "<h2>Table Structure for $tableName</h2>";
        echo "<table border='1'><tr><th>Field</th><th>Type</th><th>Null</th><th>Key</th><th>Default</th><th>Extra</th></tr>";
        foreach ($tableStructure as $row) {
            echo "<tr>";
            foreach ($row as $value) {
                echo "<td>$value</td>";
            }
            echo "</tr>";
        }
        echo "</table>";
    }

    // Function to fetch all data points for a given table
    function visualizeAllDataPoints($connection, $tableName) {
        $query = "SELECT * FROM $tableName";
        $stmt = $connection->prepare($query);
        $stmt->execute();
        $dataPoints = $stmt->fetchAll(PDO::FETCH_ASSOC);

        // Render all data points
        echo "<h2>All Data Points for the '$tableName' Table</h2>";
        echo "<table border='1'><tr>";
        foreach ($dataPoints[0] as $key => $value) {
            echo "<th>$key</th>";
        }
        echo "</tr>";
        foreach ($dataPoints as $row) {
            echo "<tr>";
            foreach ($row as $value) {
                echo "<td>$value</td>";
            }
            echo "</tr>";
        }
        echo "</table>";
    }

    // Check if user submitted a table name
    if (isset($_POST['table_name'])) {
        $table_name = $_POST['table_name'];
        visualizeTableStructure($connection, $table_name);
        visualizeAllDataPoints($connection, $table_name);
    } else {
        // If no table name is provided, display a form to input the table name
        echo "<form method='post'>";
        echo "Enter Table Name: <input type='text' name='table_name'>";
        echo "<input type='submit' value='Show Details'>";
        echo "</form>";
    }

} catch(PDOException $e) {
    echo "Error: " . $e->getMessage();
}
?>
