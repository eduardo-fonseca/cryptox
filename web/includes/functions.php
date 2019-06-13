<?php

	function cpxBitStamp() {
		$db_con = new PDO('mysql:host=localhost;dbname=CryptoX', 'root', '123');

		$statement = $db_con->prepare("select * from bitstamp order by id desc limit 1");
		if($statement->execute()) {
			$bitstamp = $statement->fetch();
			return $bitstamp;
		}
	}

	function cpxGemini() {
		$db_con = new PDO('mysql:host=localhost;dbname=CryptoX', 'root', '123');

		$statement = $db_con->prepare("select * from gemini order by id desc limit 1");
		if($statement->execute()) {
			$gemini = $statement->fetch();
			return $gemini;
		}
	}

	function cpxCexio() {
		$db_con = new PDO('mysql:host=localhost;dbname=CryptoX', 'root', '123');

		$statement = $db_con->prepare("select * from cexio order by id desc limit 1");
		if($statement->execute()) {
			$cexio = $statement->fetch();
			return $cexio;
		}
	}

	function cpxOKCoin() {
		$db_con = new PDO('mysql:host=localhost;dbname=CryptoX', 'root', '123');

		$statement = $db_con->prepare("select * from okcoin order by id desc limit 1");
		if($statement->execute()) {
			$okcoin = $statement->fetch();
			return $okcoin;
		}
	}

	function cpxHitBTC() {
		$db_con = new PDO('mysql:host=localhost;dbname=CryptoX', 'root', '123');

		$statement = $db_con->prepare("select * from hitbtc order by id desc limit 1");
		if($statement->execute()) {
			$hitbtc = $statement->fetch();
			return $hitbtc;
		}
	}


	function cpxPoloniex() {
		$db_con = new PDO('mysql:host=localhost;dbname=CryptoX', 'root', '123');

		$statement = $db_con->prepare("select * from poloniex order by id desc limit 1");
		if($statement->execute()) {
			$poloniex = $statement->fetch();
			return $poloniex;
		}
	}

	function cpxBitfinex() {
		$db_con = new PDO('mysql:host=localhost;dbname=CryptoX', 'root', '123');

		$statement = $db_con->prepare("select * from bitfinex order by id desc limit 1");
		if($statement->execute()) {
			$bitfinex = $statement->fetch();
			return $bitfinex;
		}
	}


?>
