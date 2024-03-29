Генератори — дуже потужний механізм в Python початково створений для спрощення написання ітераторів, але за допомогою якого можна вирішувати і деякі інші задачі, зокрема написання асинхроного коду.

Термін ***генератор*** (generator), в залежності від контекста, може означати або функцію-генератор, або ітератор генератора.

> ***Функція-генератор*** (generator function) — це функція, яка повертає спеціальний *ітератор генератора* (generator iterator) або (інша назва) об'єкт-генератор (generator object). 

Така функція характеризується наявністю ключового слова `yield`. Якщо в функції присутнє ключове слово `yield`, тоді Python створить не об'єкт функції, а об'єкт функції-генератора. 

Коли викликається функція-генератор, її код, на відміну звичайним функціям, насправді не виконується. Замість цього функція-генератор повертає спеціальний об'єкт генератора, який також є ітератором. А вже коли виконується ітерування по цьому об'єкту, вже тоді виконується код функції-генератора, причому виконується як би "порціями".

Код функції генератора виконується доти, доки не зустрінеться ключове слово `yield`. Інструкція `yield` як би ставить на паузу виконання і заморожує стан функції-генератора і повертає чергове значення генератора (або ж ітератора, у данному випадку це одне й те ж саме). Після наступного виклика `__next__()` функція-генератор продовжує своє виконання з того місця, де його було призупинено.

Коли виконання функції-генератора завершується (за допомогою ключового слова `return` або ж  при досягненні кінця функції), піднімається виняток `StopIteration`.

Перевага використання генераторів для створення ітераторів полягає у тому,  що магічні методи `__iter__` і `__next__` для генераторів створюються автоматично. Ми у функції-генераторі просто описуємо логіку (алгоритм) для отримання чергового значення.

Давайте розглянемо на прикладі. Створимо найпростіший генератор:

	:::python
	>>> def gen():
	...     yield 'Hello'
	...     yield 'world'
	...
	...
	>>>	
	
Спершу може здатись, що це звичайнісінька собі функція:

	:::python
	>>> gen
	<function gen at 0x0000017E2A663E18>
	>>>

Але якщо ми викличемо таку функцію, то вона поверне об'єкт генератор:

	:::python
	>>> g = gen()
	>>> g
	<generator object gen at 0x0000017E2A72D308>
	>>>

У цього об'єкта є метод `__iter__()`, отже це ітерабельний об'єкт:

	:::python
	>>> g.__iter__
	<method-wrapper '__iter__' of generator object at 0x0000017E2A72D308>
	>>>

Крім того є і метод `__next__()`, отже це і ітератор також:

	:::python
	>>> g.__next__
	<method-wrapper '__next__' of generator object at 0x0000017E2A72D308>
	>>>
	
Окей, тоді давайте проітеруємось по ньому:

	:::python
	>>> next(g)
	'Hello'
	>>> next(g)
	'world'
	>>> next(g)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	StopIteration
	>>>
	
Проітеруємось за допомогою `for`:

	:::python
	>>> for i in gen(): print(i)
	...
	Hello
	world
	>>>
	


	
	
### Лічилочка

	:::python
	>>> def counting_out(max_count):
	...     count = 1
	...     while count <= max_count:
	...             yield count
	...             count += 1
	...
	>>> for i in counting_out(5): print(i)
	...
	1
	2
	3
	4
	5
	>>>
	
	
	
	
	
	
### Фібоначчі-генератор

Створимо генератор, який буде повертати нам числа з послідовності Фібоначчі довжиною `max_count`:

	:::python
	>>> def fibo_generator(max_count):
	...     if max_count >= 1:
	...             yield 1
	...     if max_count >= 2:
	...             yield 1
	...     first, second = 1, 2
	...     count = 3
	...     while count <= max_count:
	...             yield second
	...             first, second = second, first + second
	...             count += 1
	...
	>>> f_gen = fibo_generator(10)
	>>> list(f_gen)
	[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
	>>>

Порівняйте вищенаведений код з усіма реалізаціями знаходження чисел Фібоначчі, які ми виконували раніше. Як щодо отримати сто тисяч числел Фібоначчі?


	
Ну насправді можна написати ще простіше:

	:::python
	def fibo_generator(max_count):
		first, second = 0, 1
		for _ in range(max_count):
			yield second
			first, second = second, first + second
			
