<?php

$dataset = $_POST['dataset'];

    if($dataset == "twitter"){
        //echo "llega";
        include("../html/mascotas_1_tweets.html");
    }elseif($dataset == "tableau"){
        include("../html/mascotas_2_tableau.html");
    }elseif($dataset == "data"){
        include("../html/mascotas_3_data_gov.html");
    }else{
        echo "Seleccione Dataset";
        //include("../../view_data/index.html");
    }


?>

