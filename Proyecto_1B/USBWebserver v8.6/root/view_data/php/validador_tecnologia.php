<?php

$dataset = $_POST['dataset'];

    if($dataset == "twitter"){
        //echo "llega";
        include("../html/tecnologia_1_tweets.html");
    }elseif($dataset == "tableau"){
        include("../html/tecnologia_2_tableau.html");
    }elseif($dataset == "data"){
        include("../html/tecnologia_3_data_gov.html");
    }else{
        echo "Seleccione Dataset";
        //include("../../view_data/index.html");
    }


?>

