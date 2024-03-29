<!---
Толково:
https://devpractice.ru/python-modules-and-packages/
-->

Імпортувати модуль можна за допомогою оператора import. Після ключового слова `import` вказують назву імпортованого модуля або розділені комою імена імпортованих модулів:

	:::python
	import os
	import json, requests
	
Але зауважимо, що хорошою практикою в Python є імпортування модулів по одному у кожному рядку.

Пам'ятаєте, що в Python усе є об'єкт? При імпортуванні модуля Python створює відповідний об'єкт а також ім'я, яке пов'язує з цим модулем. Ім'я об'єкта модуля буде співпадати з назвою самого модуля, але це можна змінити. Достатньо при імпортуванні модуля вказати інше ім'я після ключового слова `as`:

	:::python
	>>> import mathplotlib as mp
	>>>

Модуль завантажується лише один раз. Усі наступні спроби імпортування просто повертають посилання на вже імпортований модуль. 

При імпорті модуля виконується увесь його вміст, рядок за рядком! 
Тобто, наприклад, якщо у модулі присутні 
виклики функції `print()`, 
то при імпорті цього модуля вони спрацюють. 

Кожен модуль задає новий простір імен, атрибути якого відповідають іменам, визначеним у файлі:

Можна імпортувати тільки певні імена з модуля, після чого вони стануть доступними як глобальні імена поточного модуля.  Зробити це можна за допомогою оператора `from...import`. 
Після ключового слова `from` вказують ім'я модуля, з якого ведеться імпорт, потім після 
ключового слова `import` через кому перераховують імена того, що ми хочемо імпортувати. 
Також після кожного імені можна вказати ключове слово `as` і альтернативне ім'я:

	:::python
	>>> from math import pi
	>>> pi
	3.141592653589793
	>>>
	
Синтаксис оператора довзволяє перерахувати декілька імен через кому і, можливо, переіменувати деякі з них:

	:::python
	from usefull import long_function_name as lfn, func
	
Оператор `from...import` можна концептуально представити наступним способом:

	:::python
	import usefull
	lfn = usefull.long_function_name
	func = usefull.func
	del usefull
	
Якщо після `from...import` вказати зірочку, 
то з модуля буде імпортовано усі сутності, 
імена яких не починається з символа підкреслення: 

	:::python
	>>> from json import *
	>>> loads(dumps('123'))
	'123'
	>>>

Але зауважте, що усе імпортоване стане глобальним для поточного модуля. тому такий спосіб імпорта не завжди є хорошою практикою. 

При створенні модуля ми можемо обмежити імпорт з зірочкою  
присвоївши спеціальній змінній модуля `__all__` список з ідентифікаторами модуля. 
Наприклад, якщо у модулі `usefull` ми визначимо:

	:::python
	__all__ = []
	
то при імпорті усього вмісту цього модуля:

	:::python
	from usefull import *

не буде імпортовано нічого.

Слід зауважити, щоо `import` і `from` — це виконувані вирази, і виконуються вони у процесі виконання скрипта, а не на етапі компіляції. Це дозволяє гнучко підходити до процесі імпортування: використовувати умовні вирази і подібне.
	

	
Доступ до певної сутності модуля відбувається вказуючи її ім'я в якості атрибута модуля:

	:::python
	>>> import math
	>>> math.attr = 7
	>>> math.attr
	7
	>>> del math.attr
	>>>
	
	
В модулі завжди присутні спеціальні атрибути, розглянемо деякі з них.

***`__file__`*** — містить шлях до файла модуля:

	:::python
	>>> json.__file__
	'C:\\Python36\\lib\\json\\__init__.py'
	>>>
	
***`__name__`*** — містить ім'я модуля:

	:::python
	>>> json.__name__
	'json'
	>>>

***`__cached__`*** — містить шлях до файла зкомпільованого байт-кода:
	
	:::python
	>>> json.__cached__
	'C:\\Python36\\lib\\json\\__pycache__\\__init__.cpython-36.pyc'
	>>>

### Оформлення коду

Згідно PEP8 імпорт модулів оформляється наступним чином:

1. Усі імпорти — на початку файла.
1. Спочатку вказуємо оператори `import`, імена модулів відсортовано у лексиграфічному порядку.
1. Потім вказуємо оператори `from...import`, імена відсортовано у лексиграфічному порядку.
1. Два порожніх рядки текста вкінці.
1. Уникаємо імпорту "з зірочкою".
