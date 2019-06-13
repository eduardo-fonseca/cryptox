<?php

include_once("includes/functions.php");

echo "Bitstamp:<br>";
print_r(json_encode(cpxBitStamp()));
echo "<br>";

echo "Gemini:<br>";
print_r(json_encode(cpxGemini()));
echo "<br>";

echo "CexIO:<br>";
print_r(json_encode(cpxCexIO()));
echo "<br>";

echo "HitBTC:<br>";
print_r(json_encode(cpxHitBTC()));
echo "<br>";

echo "Poloniex:<br>";
print_r(json_encode(cpxPoloniex()));
echo "<br>";

echo "Poloniex:<br>";
print_r(json_encode(cpxBitfinex()));
echo "<br>";


?>