---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
---

# enumerate()

А от було б непогано якби у циклі ми могли б 
отримати одразу і черговий елемент послідовності, і його індекс? 

На допомогу приходить функція `enumerate()`. 
В якості аргументу вона приймає послідовність, 
і повертає теж послідовність, послідовність з кортежів. 
Кортеж на кожній ітерації містить індекс елемента і його значення: 

	:::python
	>>> for i in enumerate('abcdef'):
	...   print(i)
	...
	(0, 'a')
	(1, 'b')
	(2, 'c')
	(3, 'd')
	(4, 'e')
	(5, 'f')
	>>>

Оскільки ми чітко знаємо кількість елементів кожного кортежу, 
а саме 2 (індекс і елемент), 
то кортеж можемо розкласти прямо у заголовку циклу:

	:::python
	>>> for index, value in enumerate('abcdef'):
	...   print(index, '-', value)
	...
	0 - a
	1 - b
	2 - c
	3 - d
	4 - e
	5 - f
	>>>
	
Функція `enumerate()` повертає послідовність спеціального типу: 

	:::python
	>>> a = enumerate('abcde')
	>>> a
	<enumerate object at 0x000002A9776A1E10>
	>>> type(a)
	<class 'enumerate'>
	>>> tpl = tuple(enumerate('abcde'))
	>>> tpl
	((0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'))
	>>>
	
Розглянемо на прикладі. 
У списку цілих чисел треба усі елменти 
які менше ніж 5 помножити на 10. 

	:::python
	>>> numbers = list(range(10))
	>>> numbers
	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	>>> for index, number in enumerate(numbers):
	...     if number < 5:
	...             numbers[index] = number * 10
	...
	>>> numbers
	[0, 10, 20, 30, 40, 5, 6, 7, 8, 9]
	>>>

