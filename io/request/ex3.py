import requests

# API сайта "О погоде":
# docs: http://opogode.ua/api-v1
URL = 'http://opogode.ua/api/v1/current.json'

city = 'здолбунів'
response = requests.get(URL, params={'city':city})
if response:
	data = response.json()
	print('Місто:', data['city']['name_ua'])
	# print(data['city']['region']['name_ua'])
	print(
		data['weather']['temperature'], 'градусів, ',
		data['weather']['condition']['name_ua'], 
		
	)
	print('Вітер:', data['weather']['wind']['speed'], 'мітрів на секунду.')
	print('Вологість:', data['weather']['humidity'], 'процентів.')
	print('Тиск:', data['weather']['pressure'], 'міліметрів ртутного стовпчика.')
	

else:
	print('Інформацію не знайдено.')