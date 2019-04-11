import cpxFunctions

'''
Exchanges Adicionadas
---------------------

	Nacionais
	---------
	- MercadoBitcoin (https://www.mercadobitcoin.com.br/)
	- WallTime (https://walltime.info/)
	- BitCambio (https://bitcambio.com.br/)
	- Braziliex (https://braziliex.com/)
	- BitcoinTrade (https://bitcointrade.com.br/)
	- BTCBolsa (https://btcbolsa.com/)

	Internacionais
	--------------
	- BitFinex (https://www.bitfinex.com/)
	- BitStamp (https://www.bitstamp.net/)
	- Gemini (https://gemini.com/)
	- Cex.io (http://cex.io/)
	- OKCoin (https://www.okcoin.com/)
	- HitBtc (https://hitbtc.com/)
	- Poloniex (https://poloniex.com/)

'''


def api_bitvalor(exchange, arg1):
	"""
	Receive the content of BitValor API, parse it as JSON and return the value of selected argument.

	Parameters
	----------
	exchange : str
	arg1 : str

	Options
	-------
	exchange (MBT, WAL, CAM, BZX, BTD)
	arg1 (last, open, high, low, vol, vwap, money, trades)

	"""
	json_bitvalor = cpxFunctions.get_jsonparsed_data('https://api.bitvalor.com/v1/ticker.json')

	return {
		'MBT' : json_bitvalor['ticker_1h']['exchanges']['MBT'][arg1],
		'CAM' : json_bitvalor['ticker_1h']['exchanges']['CAM'][arg1],
		'BZX' : json_bitvalor['ticker_1h']['exchanges']['BZX'][arg1],
		'BTD' : json_bitvalor['ticker_1h']['exchanges']['BTD'][arg1],
		'B2U' : json_bitvalor['ticker_1h']['exchanges']['B2U'][arg1]

	}[exchange]


def api_bitvalorAll(exchange):
	"""
	Parameters
	----------
	exchange : str

	Options
	-------
	exchange (MBT, CAM, BZX, BTD)

	"""
	json_bitvalor = cpxFunctions.get_jsonparsed_data('https://api.bitvalor.com/v1/ticker.json')

	return json_bitvalor['ticker_1h']['exchanges'][exchange]


def api_bitfinex(arg1):
	"""
	Receive the content of BitFinex API, parse it as JSON and return the value of selected argument.

	Parameters
	----------
	arg1 : str

	Options
	-------
	arg1 (volume, timestamp, bid, last_price, mid, high, low, ask)

	Limits
	------
	20 requests/min

	"""
	json_bitfinex = cpxFunctions.get_jsonparsed_data('https://api.bitfinex.com/v1/pubticker/btcusd')
	
	return {
		'volume' : json_bitfinex[arg1],
		'timestamp' : json_bitfinex[arg1],
		'bid' : json_bitfinex[arg1],
		'last_price' : json_bitfinex[arg1],
		'mid' : json_bitfinex[arg1],
		'high' : json_bitfinex[arg1],
		'low' : json_bitfinex[arg1],
		'ask' : json_bitfinex[arg1]

	}[arg1]


def api_bitfinexAll():
	"""
	Receive the content of BitFinex API.
	Limits
	------
	20 requests/min

	"""
	json_bitfinex = cpxFunctions.get_jsonparsed_data('https://api.bitfinex.com/v1/pubticker/btcusd')
	
	return json_bitfinex


def api_bitstamp(arg1):
	"""
	Receive the content of BitStamp API, parse it as JSON and return the value of selected argument.

	Parameters
	----------
	arg1 : str

	Options
	-------
	arg1 (volume, last, timestamp, bid, vwap, high, low, ask, open)

	"""
	json_bitstamp = cpxFunctions.get_jsonparsed_data('https://www.bitstamp.net/api/ticker/')

	return {
		'volume' : json_bitstamp[arg1],
		'last' : json_bitstamp[arg1],
		'timestamp' : json_bitstamp[arg1],
		'bid' : json_bitstamp[arg1],
		'vwap' : json_bitstamp[arg1],
		'high' : json_bitstamp[arg1],
		'low' : json_bitstamp[arg1],
		'ask' : json_bitstamp[arg1],
		'open' : json_bitstamp[arg1]

	}[arg1]


def api_bitstampAll():
	"""
	Receive the content of BitStamp API.

	"""
	json_bitstamp = cpxFunctions.get_jsonparsed_data('https://www.bitstamp.net/api/ticker/')

	return json_bitstamp


def api_gemini(arg1):
	"""
	Receive the content of Gemini API, parse it as JSON and return the value of selected argument.

	Parameters
	----------
	arg1 : str

	Options
	-------
	arg1 (ask, bid, last)

	"""
	json_gemini = cpxFunctions.get_jsonparsed_data('https://api.gemini.com/v1/pubticker/btcusd')

	return {
		'ask' : json_gemini[arg1],
		'bid' : json_gemini[arg1],
		'last' : json_gemini[arg1],

	}[arg1]


def api_geminiAll():
	"""
	Receive the content of Gemini API.

	"""
	json_gemini = cpxFunctions.get_jsonparsed_data('https://api.gemini.com/v1/pubticker/btcusd')

	return json_gemini


def api_cexio(arg1):
	"""
	Receive the content of Cex.io API, parse it as JSON and return the value of selected argument.

	Parameters
	----------
	arg1 : str

	Options
	-------
	arg1 (timestamp, low, high, last, volume, volume30d, bid, ask)

	"""
	json_cexio = cpxFunctions.get_jsonparsed_data('https://cex.io/api/ticker/BTC/USD')

	return {
		'timestamp' : json_cexio[arg1],
		'low' : json_cexio[arg1],
		'high' : json_cexio[arg1],
		'last' : json_cexio[arg1],
		'volume' : json_cexio[arg1],
		'volume30d' : json_cexio[arg1],
		'bid' : json_cexio[arg1],
		'ask' : json_cexio[arg1]

	}[arg1]


def api_cexioAll():
	"""
	Receive the content of Cex.io API.

	"""
	json_cexio = cpxFunctions.get_jsonparsed_data('https://cex.io/api/ticker/BTC/USD')

	return json_cexio


def api_okcoin(arg1):
	"""
	Receive the content of OKCOIN API, parse it as JSON and return the value of selected argument.

	Parameters
	----------
	arg1 : str

	Options
	-------
	arg1 (high, vol, last, low, buy, sell)

	"""
	json_okcoin = cpxFunctions.get_jsonparsed_data('https://www.okcoin.com/api/v1/ticker.do?symbol=btc_usd')

	return {
		'high' : json_okcoin['ticker'][arg1],
		'vol' : json_okcoin['ticker'][arg1],
		'last' : json_okcoin['ticker'][arg1],
		'low' : json_okcoin['ticker'][arg1],
		'buy' : json_okcoin['ticker'][arg1],
		'sell' : json_okcoin['ticker'][arg1]


	}[arg1]


def api_okcoinAll():
	"""
	Receive the content of OKCOIN API.

	"""
	json_okcoin = cpxFunctions.get_jsonparsed_data('https://www.okcoin.com/api/v1/ticker.do?symbol=btc_usd')

	return json_okcoin


def api_hitbtc(arg1):
	"""
	Receive the content of HitBTC API, parse it as JSON and return the value of selected argument.

	Parameters
	----------
	arg1 : str

	Options
	-------
	arg1 (ask, bid, last, open, low, high, volume)

	"""
	json_hitbtc = cpxFunctions.get_jsonparsed_data('https://api.hitbtc.com/api/2/public/ticker/btcusd')

	return {
		'ask' : json_hitbtc[arg1],
		'bid' : json_hitbtc[arg1],
		'last' : json_hitbtc[arg1],
		'open' : json_hitbtc[arg1],
		'low' : json_hitbtc[arg1],
		'high' : json_hitbtc[arg1],
		'volume' : json_hitbtc[arg1]

	}[arg1]


def api_hitbtcAll():
	"""
	Receive the content of HitBTC API.

	"""
	json_hitbtc = cpxFunctions.get_jsonparsed_data('https://api.hitbtc.com/api/2/public/ticker/btcusd')

	return json_hitbtc


def api_btcbolsa(arg1):
	"""
	Receive the content of BTCBolsa API, parse it as JSON and return the value of selected argument.

	Parameters
	----------
	arg1 : str

	Options
	-------
	arg1 (last, buy, sell, low, high, volume, trades, timestamp)

	"""
	json_btcbolsa = cpxFunctions.get_jsonparsed_data('https://api.btcbolsa.com/v1/ticker/BTC')

	return {
		'last' :  json_btcbolsa['result'][arg1],
		'buy' : json_btcbolsa['result'][arg1],
		'sell' : json_btcbolsa['result'][arg1],
		'low' : json_btcbolsa['result'][arg1],
		'high' : json_btcbolsa['result'][arg1],
		'volume' : json_btcbolsa['result'][arg1],
		'trades' : json_btcbolsa['result'][arg1],
		'timestamp' : json_btcbolsa['result'][arg1]

	}[arg1]


def api_btcbolsaAll():
	"""
	Receive the content of BTCBolsa API.

	"""
	json_btcbolsa = cpxFunctions.get_jsonparsed_data('https://api.btcbolsa.com/v1/ticker/BTC')

	return json_btcbolsa


def api_poloniex(arg1):
	"""
	Receive the content of HitBTC API, parse it as JSON and return the value of selected argument.

	Parameters
	----------
	arg1 : str

	Options
	-------
	arg1 (last, lowestAsk, highestBid, percentChange, high24hr, low24hr)

	"""
	json_poloniex = cpxFunctions.get_jsonparsed_data('https://poloniex.com/public?command=returnTicker')

	return {
		'last' : json_poloniex['USDT_BTC'][arg1],
		'lowestAsk' : json_poloniex['USDT_BTC'][arg1],
		'highestBid' : json_poloniex['USDT_BTC'][arg1],
		'percentChange' : json_poloniex['USDT_BTC'][arg1],
		'high24hr' : json_poloniex['USDT_BTC'][arg1],
		'low24hr' : json_poloniex['USDT_BTC'][arg1]
	}[arg1]


def api_poloniexAll():
	"""
	Receive the content of HitBTC API.

	"""
	json_poloniex = cpxFunctions.get_jsonparsed_data('https://poloniex.com/public?command=returnTicker')

	return json_poloniex