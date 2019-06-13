import json
import urllib2
import ssl

'''
	FUNCOES GERAIS DA CRYPTOX
	----------------------------
'''

def get_jsonparsed_data(url):
	"""
	Receive the content of ''url'', parse it as JSON and return the object.

	Parameters
	----------
	url : str

	Returns
	-------
	json
	"""

	request = urllib2.Request(url)
	request.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36')
	response = urllib2.urlopen(request, context=ssl._create_unverified_context())
	data = response.read().decode("utf-8")
	return json.loads(data)