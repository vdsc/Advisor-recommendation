<?php
$query = "networks";

// echo $query;
$query = str_replace(" ", "+", $query);

echo exec("curl 'http://localhost:8983/solr/job/select?indent=on&q=".$query."&rows=5000&wt=json' -o res.json");

$myfile = fopen("res.json", "r") or die("Unable to open file!");
$dis_res = fread($myfile,filesize("res.json"));
$dis_res = json_encode($dis_res);
$dis_res = str_replace('\n', '', $dis_res);
$dis_res = str_replace('\"', '', $dis_res); 
$dis_res = preg_replace('/responseHeader.*?}}/', '', $dis_res);
$dis_res = str_replace('title:[', '<table><tbody><tr><td>Title: ', $dis_res);
$dis_res = str_replace('company:[', '<tr><td>Company: ', $dis_res);
$dis_res = str_replace('location:[', '<tr><td>Location: ', $dis_res);
$dis_res = str_replace('summary:[', '<tr><td>Summary: ', $dis_res);
$dis_res = str_replace('],', '</td></tr>', $dis_res); 
$dis_res = preg_replace('/id:.*?},/', '},', $dis_res);
$dis_res = str_replace('},', '</tbody></table>', $dis_res);
$dis_res = str_replace('{','', $dis_res);
$dis_res = str_replace('response:numFound:', '<table><tbody><tr><td style="text-align:center;font-size:250%;" >Number Of Result: ', $dis_res); 
$dis_res = str_replace(',start:0,docs:[', '</td></tr></tbody></table>', $dis_res); 

?>