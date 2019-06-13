import MySQLdb as mydb
import cpxAPIS
import time


def db_insert_value(table, column, data):
	"""
	Insert a float value on the selected column.

	Parameters
	----------
	table : str
	column : str
	data : float

	Returns
	-------
	True or False.
	"""

	try:
	    """query = "INSERT INTO %s (id,%s) VALUES (1,%f)" % (table, column, data)"""
	    query = "UPDATE %s SET %s = %f WHERE id = 1" % (table, column, data)
	    db = mydb.connect('localhost', 'root', '123', 'CryptoX')
	    cursor = db.cursor()
	    cursor.execute(query)
	    db.commit()

	    return True

	except (mydb.Error, mydb.Warning) as e:
		print(e)
		return False


def db_show_lastValue(table, column):
	try:
		query = "SELECT %s FROM %s ORDER BY ID DESC LIMIT 1" % (column, table)
		db = mydb.connect('localhost', 'root', '123', 'CryptoX')
		cursor = db.cursor()
		cursor.execute(query)
		db.commit()

		return cursor.fetchone()[0]
	except:
		'ERROR LASTVALOUE'

def db_run_cmd(query):
	"""
	Executes a query in the database.

	Parameters
	----------
	query : str

	Returns
	-------
	The output of the command or False.
	"""

	try:
		db = mydb.connect('localhost', 'root', '123', 'CryptoX')
		cursor = db.cursor()
		cursor.execute(query)
		db.commit()

		return cursor.fetchone()[0]

	except:
		return False

def db_input_bitstamp():
	'''

	(volume, last, timestamp, bid, vwap, high, low, ask, open)
	'''
	while True:
		json = cpxAPIS.api_bitstampAll()

		print ("\nBitStamp Last (BD): " + str(db_show_lastValue('bitstamp', 'last')))
		print ("BitStamp Last: " + str(json['last']))


		db_insert_value('bitstamp', 'last', float(json['last']))
		db_insert_value('bitstamp', 'volume', float(json['volume']))
		db_insert_value('bitstamp', 'timestamp', float(json['timestamp']))
		db_insert_value('bitstamp', 'bid', float(json['bid']))
		db_insert_value('bitstamp', 'vwap', float(json['vwap']))
		db_insert_value('bitstamp', 'high', float(json['high']))
		db_insert_value('bitstamp', 'low', float(json['low']))
		db_insert_value('bitstamp', 'ask', float(json['ask']))
		db_insert_value('bitstamp', 'open', float(json['open']))
		time.sleep(4)

def db_input_gemini():
	'''
	(ask, bid, last)
	'''
	while True:
		json = cpxAPIS.api_geminiAll()

		print ("\nGemini Last (BD): " + str(db_show_lastValue('gemini', 'last')))
		print ("Gemini Last: " + str(json['last']))

		db_insert_value('gemini', 'last', float(json['last']))
		db_insert_value('gemini', 'ask', float(json['ask']))
		db_insert_value('gemini', 'bid', float(json['bid']))
		time.sleep(4)

def db_input_cexio():
	'''
	(timestamp, low, high, last, volume, volume30d, bid, ask)
	'''
	while True:
		json = cpxAPIS.api_cexioAll()

		print ("\nCexIO Last (BD): " + str(db_show_lastValue('cexio', 'last')))
		print ("CexIO Last: " + str(json['last']))

		db_insert_value('cexio', 'last', float(json['last']))
		db_insert_value('cexio', 'timestamp', int(json['timestamp']))
		db_insert_value('cexio', 'low', float(json['low']))
		db_insert_value('cexio', 'high', float(json['high']))
		db_insert_value('cexio', 'volume', float(json['volume']))
		db_insert_value('cexio', 'volume30d', float(json['volume30d']))
		db_insert_value('cexio', 'bid', float(json['bid']))
		db_insert_value('cexio', 'ask', float(json['ask']))
		time.sleep(4)

def db_input_okcoin():
	'''
	(high, vol, last, low, buy, sell)
	'''
	while True:
		json = cpxAPIS.api_okcoinAll()

		print ("\nOKCoin Last (BD): " + str(db_show_lastValue('okcoin', 'last')))
		print ("OKCoin Last: " + str(json['ticker']['last']))

		if (float(db_show_lastValue('okcoin', 'last')) != float(json['ticker']['last'])):
			db_insert_value('okcoin', 'last', float(json['ticker']['last']))
			db_insert_value('okcoin', 'sell', float(json['ticker']['sell']))
			db_insert_value('okcoin', 'buy', float(json['ticker']['buy']))
			db_insert_value('okcoin', 'vol', float(json['ticker']['vol']))
			db_insert_value('okcoin', 'high', float(json['ticker']['high']))

		time.sleep(4)


def db_input_hitbtc():
	'''
	(ask, bid, last, open, low, high, volume)
	'''
	while True:
		json = cpxAPIS.api_hitbtcAll()

		print ("\nHITBTC Last (BD): " + str(db_show_lastValue('hitbtc', 'last')))
		print ("HITBTC Last: " + str(json['last']))

		db_insert_value('hitbtc', 'last', float(json['last']))
		db_insert_value('hitbtc', 'open', float(json['open']))
		db_insert_value('hitbtc', 'low', float(json['low']))
		db_insert_value('hitbtc', 'high', float(json['high']))
		db_insert_value('hitbtc', 'ask', float(json['ask']))
		db_insert_value('hitbtc', 'bid', float(json['bid']))
		time.sleep(4)


def db_input_poloniex():
	'''
	(last, lowestAsk, highestBid, percentChange, high24hr, low24hr)
	'''
	while True:
		json = cpxAPIS.api_poloniexAll()

		print ("\nPoloniex Last (BD): " + str(db_show_lastValue('poloniex', 'last')))
		print ("Poloniex Last: " + str(json['USDT_BTC']['last']))

		db_insert_value('poloniex', 'last', float(json['USDT_BTC']['last']))
		db_insert_value('poloniex', 'lowestAsk', float(json['USDT_BTC']['lowestAsk']))
		db_insert_value('poloniex', 'highestBid', float(json['USDT_BTC']['highestBid']))
		db_insert_value('poloniex', 'percentChange', float(json['USDT_BTC']['percentChange']))
		db_insert_value('poloniex', 'high24hr', float(json['USDT_BTC']['high24hr']))
		db_insert_value('poloniex', 'low24hr', float(json['USDT_BTC']['low24hr']))
		time.sleep(4)


def db_input_bitfinex():
	'''
	(volume, timestamp, bid, last_price, mid, high, low, ask)
	'''
	while True:
		json = cpxAPIS.api_bitfinexAll()

		print ("\nBitfinex Last (BD): " + str(db_show_lastValue('bitfinex', 'last_price')))
		print ("Bitfinex Last: " + str(json['last_price']))

		db_insert_value('bitfinex', 'last_price', float(json['last_price']))
		db_insert_value('bitfinex', 'bid', float(json['bid']))
		db_insert_value('bitfinex', 'mid', float(json['mid']))
		db_insert_value('bitfinex', 'high', float(json['high']))
		db_insert_value('bitfinex', 'low', float(json['low']))
		db_insert_value('bitfinex', 'ask', float(json['ask']))
		time.sleep(4)
