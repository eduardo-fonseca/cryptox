<?php

	function cpxMercadoBitcoin() {
		$db_con = new PDO('mysql:host=localhost;dbname=CryptoX', 'root', '123');

		$statement = $db_con->prepare("select * from mercadobitcoin order by id desc limit 1");
		if($statement->execute()) {
			$mercadobitcoin = $statement->fetch();
			return $mercadobitcoin;
		}
	}

	function cpxWalltime() {
		$db_con = new PDO('mysql:host=localhost;dbname=CryptoX', 'root', '123');

		$statement = $db_con->prepare("select * from walltime order by id desc limit 1");
		if($statement->execute()) {
			$walltime = $statement->fetch();
			return $walltime;
		}
	}

	function cpxBitCambio() {
		$db_con = new PDO('mysql:host=localhost;dbname=CryptoX', 'root', '123');

		$statement = $db_con->prepare("select * from bitcambio order by id desc limit 1");
		if($statement->execute()) {
			$bitcambio = $statement->fetch();
			return $bitcambio;
		}
	}

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

	function cpxBTCBolsa() {
		$db_con = new PDO('mysql:host=localhost;dbname=CryptoX', 'root', '123');

		$statement = $db_con->prepare("select * from btcbolsa order by id desc limit 1");
		if($statement->execute()) {
			$btcbolsa = $statement->fetch();
			return $btcbolsa;
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
