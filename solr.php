<?php
$query = 'network';
//$query = $_POST["x"];
//echo ($query);
// echo $query;
//$query = $_POST["query"];
// echo $query;
//Associative array for the http query
$http_query = array(
    'indent' => 'on',
    'q' => $query,
    'rows' => '500',
    'wt' => 'json'
);
//BASE_URL for the select request
$base_url = "http://localhost:8983/solr/advisor/select?";

$full_query = $base_url.http_build_query($http_query);
//require_once('rest.inc.php');

// CALL

//$results = [];

//echo exec("curl 'http://localhost:8983/solr/test/select?indent=on&q=".$query."&rows=500&wt=json' -o res2.json");
$curl = curl_init($full_query);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
// $output = curl_exec($curl);


curl_setopt($curl, CURLOPT_URL, $full_query);
curl_setopt($curl, CURLOPT_HEADER, false);
$output = curl_exec($curl);
// curl_close($ch);


$data = json_decode($output, true);

echo "<pre>";
//echo $data[0]["response"];

//var_dump($data["response"]["docs"]);

foreach($data as $v) {
    $data[key($v)] = current($v);
}
//$data = str_replace("[","", $data);


echo json_encode($data["response"]["docs"], 128);

curl_close($curl);

// echo "Ping Status : ".$data["status"].PHP_EOL;
// $output = json_encode($output);
// echo gettype($output);
//echo exec("curl 'http://localhost:8983/solr/test/select?indent=on&q=".$query."&rows=500&wt=json' ");
//$res = RestCurl::get("curl 'http://localhost:8983/solr/test/select?indent=on&q=".$query."&rows=500&wt=json' ");

?>