# Представлення класів

Часто буває корисним представлення класа у вигляді символьного рядка. В Python існує декілька методів, які ви можете визначити для налаштування поведінки вбудованих функцій при представленні вашого класа.

#### `__str__(self)`

Визначає поведінку функції `str()`, яка була викликана для екземпляра вашого класа.

#### `__repr__(self)`

Визначає поведінку функції 'repr()', викликаної для екземпляра вашого класа. Головна відмінність від `str()` — в цільовій аудиторії. `repr()` більше призначено для машино-орієнтованого вивода, більш того, це по можливості має бути валідний код на Python) для створення екземпляра класа. `str()` признзачено для читання людьми.

	:::python
	>>> class Person():
	...     def __init__(self, name, email):
	...             self.name = name
	...             self.email = email
	...     def __str__(self):
	...             return '{name} <{email}>'.format(name=self.name, email=self.email)
	...     def __repr__(self):
	...             return 'Person("{name}", "<{email}>")'.format(name=self.name, email=self.email)
	...
	>>> p = Person('John Doe', 'johnny@nowhere.com')
	>>> str(p)
	'John Doe <johnny@nowhere.com>'
	>>> print(p)
	John Doe <johnny@nowhere.com>
	>>> repr(p)
	'Person("John Doe", "<johnny@nowhere.com>")'
	>>> p
	Person("John Doe", "<johnny@nowhere.com>")
	>>>

	
