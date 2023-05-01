<?php

include 'conexion.php';

header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST');
header("Access-Control-Allow-Headers: X-Requested-With");

function insertData($led1on, $led2on, $led3on, $temperatura, $bombilloOn){
    $conexion = $GLOBALS["conexion"];
    $led1on = $led1on == "true" ? 1:0;
    $led2on = $led2on == "true" ? 1:0;
    $led3on = $led3on == "true" ? 1:0;
    $bombilloOn = $bombilloOn == "true" ? 1:0;
    $sq = $conexion -> prepare("INSERT INTO botesp32 (led1on, led2on, led3on, temperatura, bombilloOn) VALUES ('$led1on', '$led2on', '$led3on', '$temperatura', '$bombilloOn')");
    $sq -> execute();
}

function deleteData($id){
    $conexion = $GLOBALS["conexion"];
    $sq = $conexion -> prepare("DELETE FROM botesp32 WHERE id='$id'");
    $sq -> execute();
}

function editData($id, $led1on, $led2on, $led3on, $temperatura, $bombilloOn){
    $conexion = $GLOBALS["conexion"];
    $led1on = $led1on == "true" ? 1:0;
    $led2on = $led2on == "true" ? 1:0;
    $led3on = $led3on == "true" ? 1:0;
    $bombilloOn = $bombilloOn == "true" ? 1:0;
    $sq = $conexion -> prepare("UPDATE botesp32 SET led1on = '$led1on',led2on = '$led2on',led3on = '$led3on',temperatura='$temperatura', bombilloOn='$bombilloOn' WHERE id='$id'");
    $sq -> execute();
}

function getAllData(){
    $conexion = $GLOBALS["conexion"];
    $sq = $conexion -> prepare("SELECT * FROM botesp32");
    $sq -> execute();
    $array = array();

    while($res = $sq -> fetch()){
        array_push($array, [
            "id" => $res["id"],
            "led1on" => $res["led1on"],
            "led2on" => $res["led2on"],
            "led3on" => $res["led3on"],
            "temperatura" => $res["temperatura"],
            "bombilloOn" => $res["bombilloOn"],
            "dateAndTime" => $res["dateAndTime"],
        ]);
    }
    return $array;
}

?>