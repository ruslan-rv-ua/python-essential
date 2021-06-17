# Вбудовані функції Python

В Python є велика кількість так званих вбудованих функцій. Такі функції можна використовувати без імпортування їх з модулів. Вони як би знаходяться у так званому віртуальному модулі `built-ins`. 

Повний список вбудованих функцій можна знайти у [документації Python](https://docs.python.org/3/library/functions.html).

### Деякі вбудовані функції

#### abs(*x*)

Повертає абсолютне значення числа. Аргумент може належати до типів int, float, complex.

#### all(*iterable*)

Повертає *True* якщо усі елементи послідовності *iterable* є *true* (або якщо *iterable* не містить жодного елемента). Еквіваленто наступному коду:

	:::python
	def all(iterable):
		for element in iterable:
			if not element:
				return False
		return True
	
#### any(*iterable*)

Повертає True якщо будь-який елемент послідовності *iterable* є *true*. Якщо  *iterable* не містить жодного елемента, повертає *False*. Еквіваленто:

	:::python
	def any(iterable):
		for element in iterable:
			if element:
				return True
		return False

#### enumerate(*iterable, start=0*)

Повертає послідовність типу	*enumerate*. Кожен елемент цієї послідовності представляє кортеж, який складається з порядкового номера чергового елемента послідовності *iterable* (за замовчуванням нумерація починається з 0) і, власне, самого елемента.

	:::python
	>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
	>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
	>>> enumerate(seasons)
	<enumerate object at 0x0000019C901D9B88>
	>>> list(enumerate(seasons))
	[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
	>>> list(enumerate(seasons, start=1))
	[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]


#### id(*object*)

Повертає ціле число, "ідентифікатор" об'єкта *object*. Гарантується що це число є унікальним і незмінним протягом усього часу, коли існує *object*.

	:::python
	>>> a = 'wow'
	>>> b = a
	>>> id(a)==id(b)
	True
	>>>


#### reversed(seq)

Повертає послідовність типу , елементами якої є елементи послідовності *seq* у зворотньому порядку.

	:::python
	>>> r=reversed((1,2,3,4))
	>>> type(r)
	<class 'reversed'>
	>>> list(r)
	[4, 3, 2, 1]
	>>> list(reversed('abcd'))
	['d', 'c', 'b', 'a']
	>>>

## Додаткові матеріали

[Документація Python — вбудовані функції](https://docs.python.org/3/library/functions.html)
	
## Завдання 1

Користуючись документацією Python ознайомтесь з наступними вбудованими функціями:

- input()
- print()
- divmod()
- pow()
- min()
- max()
- sum()

Чи дізнались ви чогось нового про вже відомі функції?

## Завдання 2

Не запускаючи код на виконання визначте результат наступних виразів (кожен вираз знаходиться в окремому рядку) а потім перевірте себе користуючись інтерактивним режимом інтерпретатора:

	:::python
	any([True])
	all((True,))
	any((True, False))
	all((True, 0))
	all((1000, []))
	all(([1000], 'hello'))
	all([])
	any([])
	all('hello')
