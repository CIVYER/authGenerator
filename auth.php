<?php
    header("Access-Control-Allow-Origin: *");  // Allow cross-origin requests

    // $email = "joshuavreyes111222@gmail.com";
    $email = $_POST['email'];

    $command = escapeshellcmd("python ./auth.py $email");
    $authCode = shell_exec($command);

    echo $authCode;

?>
