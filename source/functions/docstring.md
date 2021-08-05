---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# Документування функцій

Оскільки у мовах програмування, у тому числі Python, існує велика кількість вбудованих та третьосторонніх модулів, то пам'ятати їх усі, у тому числі і їх функціонал, неможливо. 

## Need help?

Інтерпретатор Python надає чудову можливість отримати вбудованими засобами довідку або документацію практичино до усього, до чого вона тільки існує, за допомогою вбудованої функції:

	:::python
	help()

Якщо функція викликається без аргументів, довідкова система запускається у інтерактивному режимі.
Якщо функції передано символьний рядок, то виконується спроба інтерпретувати її як ім'я модуля, функції, класу, метода або розділу документації, після чого довідка виводиться у консоль. Якщо ж функції передано об'єкт будь-якого іншого типу, довідка герерується по даним цього об'єкта (docstring).

	:::python
	>>> help(print)
	Help on built-in function print in module builtins:

	print(...)
		print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

		Prints the values to a stream, or to sys.stdout by default.
		Optional keyword arguments:
		file:  a file-like object (stream); defaults to the current sys.stdout.
		sep:   string inserted between values, default a space.
		end:   string appended after the last value, default a newline.
		flush: whether to forcibly flush the stream.

	>>>

Функцію `help()` використовують, в основному, у інтерактивному режимі інтерпретатора.

## docstring

Але звідки ж функція `help()` бере дані документації?

Під час написання коду до практично усіх сутностей Python (функція, метод, клас, модуль) ми одразу ж можемо створювати документацію. Робиться це за допомогою docstring.

*docstring* — це "особливий вид" коментаря. 
Перший коментар, що стоїть на самому початку модуля, функції та ін. і є docstring, або *рядком документації*.

Основні відміни docstring від звичайних коментарів:

- до рядків документації можна отримати доступ під час виконання програми
- рядки документації зберігаються у байт-коді
- до рядків документації мають доступ інтерпретатор, середовище розробки

Напряму доступ до рядків документації можна отримати через атрибут (поле) `__doc__` відповідних об'єктів.

	:::python
	>>> print(print.__doc__)
	print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

	Prints the values to a stream, or to sys.stdout by default.
	Optional keyword arguments:
	file:  a file-like object (stream); defaults to the current sys.stdout.
	sep:   string inserted between values, default a space.
	end:   string appended after the last value, default a newline.
	flush: whether to forcibly flush the stream.
	>>>

При роботі з інтерпретатором у інтерактивному режимі зручно використовувати функцію `help()`.

Згідно PEP8 `docstring` оформляється наступним чином:

- текст заключають у потрійні лапки
- текст може починатись одразу після відкриваючих лапок або ж з наступного рядка
- закриваючі лапки мають розташовуватись у окремому рядку

Написання документації, так само як і коментарів до початкового коду, є дуже важливим! 
Основне призначення коментарів – пояснити що робить код, як він працює. Основне призначення рядків документації – коротко описати в цілому для чого призначено об'єкт, які аргументи приймає, і що повертає. 

Супроводжуйте ваші функції якісною документацією і програмісти, котрі будуть працювати з вашим кодом після вас, будуть вдячні вам.
Зауважимо: документування прийнято виконувати англійською мовою. 
Багато проектів мають відкритий код, доступні у Вебі, їх вивчають і модифікують програмісти з різних країн. 
Використання однієї мови дозвояє їм розуміти один одного. 
Тому професійний програміст має володіти английською хоча б на початковому рівні. 
Google Translate – теж варіант. 

## Приклади

Оголосимо функцію і одразу ж створимо до неї документацію:

	:::python
	>>> def rectangle_square(width, height):
	...     """
	...     Calculates and returns square of rectangle with 'width' and 'height'
	...     """
	...     return width * height
	...
	>>> help(rectangle_square)
	Help on function rectangle_square in module __main__:

	rectangle_square(width, height)
		Calculates and returns square of rectangle with 'width' and 'height'

	>>> rectangle_square.__doc__
	"\n\tCalculates and returns square of rectangle with 'width' and 'height'\n\t"
	>>> rectangle_square(15, 20)
	300
	>>>

## Завдання

1. Скориставшись функцією `help()` ознайомтесь з документацією тих сутностей Python, що вас цікавить найбільше на даний момент. 
1. Спробуйте вивчити документацію до функції `help()` 
