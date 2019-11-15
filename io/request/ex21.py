# Бібліотека requests:
# pip install requests
# docs: https://2.python-requests.org/en/master/

import requests

# Бібліотека Terminal Tables
# pip install terminaltables
# docs: https://robpol86.github.io/terminaltables/
from terminaltables import SingleTable

# API курси валют Приватбанка:
# docs: https://api.privatbank.ua/#p24/exchange
URL = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'

response = requests.get(URL)
# print(response.status_code)
# print(response.headers['content-type'])
# print(response.encoding)
# print(response.content)
# print(response.text)
# print(response.json())

if response:
	'''
	for rate in response.json():
		print(format_str.format(
			rate['base_ccy'] + '/' + rate['ccy'],
			rate['buy'],
			rate['sale'],
		))
	'''
	data = [['Валюта', 'Купівля', 'Продаж']]
	for rate in response.json():
		data.append([rate['ccy'], rate['buy'], rate['sale']])
	table = SingleTable(data)
	print(table.table)
else:
	print('Error!')