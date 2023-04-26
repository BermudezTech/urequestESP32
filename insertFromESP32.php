<?php

$GLOBALS["conexion"] = new PDO('mysql:host=localhost; dbname=test', 'root', '');
$GLOBALS["conexion"] -> exec("set names utf8");

header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST');
header("Access-Control-Allow-Headers: X-Requested-With");

$json = file_get_contents('php://input');
$data = json_decode($json);
//$led1on = $data->led1on;

$sq = $conexion -> prepare("");
$sq -> execute();

echo json_encode("ok");

?>
