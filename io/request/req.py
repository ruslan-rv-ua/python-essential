# Бібліотека requests:
# pip install requests
# docs: https://2.python-requests.org/en/master/

import requests

URL = 'http://inclusive-it.org/python-essentials/'

response = requests.get(URL)
with open('index.html', 'wb') as file:
	file.write(response.content)