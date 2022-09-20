<?php 

session_start();

if (!isset($_SESSION['username'])) {
    header("Location: index.php");
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome</title>
</head>
<body>
    <?php echo "<h1 style=color: hotpink;>Welcome " . $_SESSION['username'] . "</h1>"; ?>
    <a href="logout.php">Logout</a>
    <br>
    <br>
    <br>
    <a href="./call.php"> Crop Prediction</a>
    <br>
    <br>
    <br>
    <a href="PlantDisease_Deployment/app.py"> Plant Disease Prediction </a>
</body>
</html>