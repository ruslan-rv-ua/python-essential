from urllib.request import urlopen
import json
from pprint import pprint

# API docs: https://www.blockchain.com/uk/api/exchange_rates_api
URL = 'https://blockchain.info/ticker'

with urlopen(URL) as response:
	enc = response.headers.get_content_charset()
	data = response.read()
	
data = json.loads(data.decode(encoding=enc))
# pprint(data)
ccy_data = data['USD']
# pprint(ccy_data)
print(f"Курс BTC: {ccy_data['last']:10.5} {ccy_data['symbol']}")
