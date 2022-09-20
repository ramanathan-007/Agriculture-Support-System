<?php
    $command = escapeshellcmd('python CropPrediction/app.py');
    $output = shell_exec($command);
    echo $output;
?>