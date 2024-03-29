# Цілі числа

## Створення цілих чисел

При створенні за допомогю літерала можна вказати систему числення 
використовуючи відповідні префікси: 

	:::python
	>>> 30 # у десятковій системі числення
	30
	>>> 0x1E # у шістнадцятковій системі числення
	30
	>>> 0o36 # у вісімковій системі числення
	30
	>>> 0b11110 # у двійковій системі числення
	30
	>>>
	
Для більш легшого візуального сприйняття 
цифри цілого числа можна розділяти символом підкреслення групуючи по 3: 

	:::python
	>>> n = 1_345_678
	>>> n
	1345678
	>>> 1_0_0 # насправді підкреслення ігноруються
	100
	>>> 0X10_FF_FF
	1114111
	>>>
	
Виклик `int()` без аргументыв дає `0`. 
	
## Приведення інших типів до `int`

	int(s, base=10)
	
- `s` – `str`, `bytes` або `bytearray`: представлення літерала цілого числа
- `base` – ціле число, що визначає кількість цифр у системі числення; допустимы значення: 0, 2-36 

Приклади:

	:::python
	>>> int('  +15  ',10)
	15
	>>> int('17',8)
	15
	>>> int('20',16)
	32
	>>> int('2EF',16)
	751
	>>> int('19',8) # помилка, цифра 9 не може бути у 8-й системі числення
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ValueError: invalid literal for int() with base 8: '19'
	>>>
	
Дійсні числа приводяться до `int` шляхом відкидання дробової частини: 

	:::python
	>>> int(1.9999)
	1
	>>>
	
Класи можуть реалізовувати власний метод `__int__()` для приведення об'єкта до `int`: 

	:::python
	>>> from datetime import datetime
	>>> class MyDateTime(datetime):
	...     def __int__(self):
	...         return int(self.timestamp())
	...
	>>> d = MyDateTime.now()
	>>> d
	MyDateTime(2021, 9, 6, 14, 19, 44, 319623)
	>>> int(d)
	1630927184
	>>> 

Для створення `int` з послідовності байт використовують класовий метод `int.from_bytes()`. 
	
## Приведення `int` до інших типів

Перетворити `int` на символьний рядок — використовуємо вбудовані функції `str(), bin(), oct(), hex()`: 

	:::python
	>>> str(30) # у десятковій системі числення
	'30'
	>>> bin(30) # у двійковій системі числення
	'0b11110'
	>>> oct(30) # у вісімковій системі числення
	'0o36'
	>>> hex(30) # у шістнадцятковій системі числення
	'0x1e'
	>>>
	
Для представлення `int` у вигляді послідовності байт використовують метод `int.to_bytes()`. 
	
## Бітові операції

<!-- https://www.bestprog.net/uk/2019/10/21/python-bitwise-operators-ua/#q07 -->

Мова Python підтримує роботу з двійковими розрядами (бітами) цілочисельних величин, 
де кожен біт числа розглядається окремо. 
Для забезпечення цього в Python використовуються так звані бітові або порозрядні оператори, 
що реалізують загальновідомі бітові операції. 

У бітових операторах кожен операнд розглядається як послідовність двійкових розрядів (бітів), 
що приймають значення 0 або 1 (двійкова система числення). 
Над цими розрядами можна виконувати відомі операції: логічне "І", логічне "АБО", інші. 

Бітові оператори в порядку спадання пріоритету: 

|Оператор|Операція|
|-|-|
|`~`|інверсія (НІ, NOT)|
|`<<`, `>>`|зсув вліво/вправо на задану кількість біт (SHIFT LEFT/RIGHT)|
|`&`|(І, AND)|
|`^`|(виключне АБО, XOR)|
|`|`|(АБО, OR)|

Зауважте: Python тип `int` представлений як знакове ціле число. 
Відповідно бітові операції проводяться над знаковими цілими. 
Наприклад при інверсії додатнє число стає від’ємним зі зсувом на -1. 
Так само від’ємне число стає додатнім зі зсувом на -1. 

	:::python
	>>> a = 0b1001
	>>> a
	9
	>>> b = ~a
	>>> b
	-10
	>>> bin(b)
	'-0b1010'
	>>> bin(~0b1111)
	'-0b10000'
	>>> bin(~-0b1111)
	'0b1110'
	>>>
	
Дізнатись кількість біт необхідних для представлення цілого числа 
можна за допомогою відповідного метода: 

	:::python
	>>> (-10).bit_length()
	4
	>>> bin(-10)
	'-0b1010'
	>>>

Оскільки Python є мовою програмування з високим ступенем абстракції 
бітові операції на практиці використовуються досить рідко порівняно з іншими мовами програмування. 
Тому в рамках даного курса ми не розглядаємо детально бітові операції. 
Рекомендуємо звернутись до документації Python. 

## Додаткові матеріали

- [Документація Python: бітові операції](https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types)