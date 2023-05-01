<?php

$GLOBALS["conexion"] = new PDO('mysql:host=localhost; dbname=test', 'root', '');
$GLOBALS["conexion"] -> exec("set names utf8");

 ?>