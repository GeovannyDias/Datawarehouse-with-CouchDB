<?php

$dataset = $_POST['dataset'];

    if($dataset == "twitter"){
        //echo "llega";
        include("../html/entretenimineto_1_tweets.html");
    }elseif($dataset == "tableau"){
        include("../html/entretenimineto_2_tableau.html");
    }elseif($dataset == "data"){
        include("../html/entretenimineto_3_data_gov.html");
    }else{
        echo "Seleccione Dataset";
        //include("../../view_data/index.html");
    }


?>

