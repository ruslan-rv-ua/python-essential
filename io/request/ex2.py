# Бібліотека requests:
# pip install requests
# docs: https://2.python-requests.org/en/master/

import requests

URL = 'http://inclusive-it.org/python-essentials/'
response = requests.get(URL)
# res = response.status_code
# res = response.encoding
# res = response.content
response.encoding = 'UTF-8'
res = response.text
# res = response.headers
# res = response.headers['content-type']
# res = response.json()
print(res)
