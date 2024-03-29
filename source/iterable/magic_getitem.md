В Python коли ми отримуємо доступ до елементів контейнера конструкцією:

	obj[key]
	
завжди викликається магічний метод:
	
	__getitem__(obj, key)
	
Реалізуючи цей магічний метод ми і задаємо поведінку для екземплярів певних класів. Наприклад, для списків — це доступ до його елементів по індексу, в цьому випадку індексом може бути ціле число або зрізання, а для словників — це ключ елемента.

Пригадаємо: щоб об'єкт був ітерабельним, функція `iter()` має повернути ітератор для цього об'єкта. У свою чергу якщо функція `iter()` знаходить у потенційно ітерабельного об'єкта магічний метод `__getitem__()`, тоді Python спробує побудувати ітератор самостійно. 

Методу `__getitem__()` будуть передаватись цілі невід'ємні числа, тобто як індекси для списків, але які більше або дорівнюють нулю. 
Ми ж у свою чергу повинні реалізувати повернення необхідного значення, яке начебто відповідає переданому індексу. 

Якщо переданий "індекс" виходить за межі, атже нам треба ж якимось чином обмежити довжину послідовності, то ми маємо "підняти" виняток IndexError



### Ступені двійки

Створимо ітерабельний об'єкт, щоб можна було б отримувати послідовність із ступенів числа 2:

	:::python
	>>> class Pow2:
	...     def __init__(self, max_len):
	...         self.max_len = max_len
	...     def __getitem__(self, index):
	...         if 0 <= index <= self.max_len:
	...             return 2 ** index
	...         else:
	...             raise IndexError
	...	

	
Створимо екземпляр нашого ітерабельного об'єкта, і спочатку спробуємо звертатись до його елементів "традиційним" способом, тобто за допомогою індексування:

	:::python
	>>> p2 = Pow2(4)
	>>> p2[0]
	1
	>>> p2[4]
	16
	>>> p2[5]
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "<stdin>", line 8, in __getitem__
	IndexError
	>>>

А тепер давайте спробуємо отримати ітератор для створеного ітерабельного об'єкта:

	:::python
	>>> it = iter(p2)
	>>> it
	<iterator object at 0x000001F7396AF240>
	>>>
	
Python сам створив ітератор. Спробуємо за допомогою цього ітератора отримувати значення послідовності:

	:::python
	>>> next(it)
	1
	>>> next(it)
	2
	>>> next(it)
	4
	>>> next(it)
	8
	>>> next(it)
	16
	>>> next(it)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	StopIteration
	>>>
	
Зауважте: ітератор при досягненні кінця послідовності "піднімає" виняток `StopIteration`, власне як і має робити ітератор. 
Отже і цикл `for` буде працювати як і очікується:

	:::python
	>>> for n in p2: print(n)
	...
	1
	2
	4
	8
	16
	>>>


