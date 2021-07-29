---
hide:
#  - navigation # Hide navigation
 - toc        # Hide table of contents
### https://habr.com/ru/company/otus/blog/555924/
---

# Моржовий оператор

Пригадаємо:

> Вираз обчислюється як значення, а інструкція виконує певну дію.

В Python 3.8 з'явився так званий "моржовий оператор" присвоєння. 
Він вирішує одразу дві задачі: 

- присвоює значення змінній
- повертає це значення

Синтаксис наступний:

	variable := expression
	
Семантика:

- обчислюється значення виразу `expression`
- це значення присвоюється змінній `variable`
- це ж значення повертається як результат обчислення виразу

Оператор отримав неформальну назву "моржовий" тому що двокрапка і знак дорівнює візуально схожі на моржа: очі та бивні. 

Найпростіший приклад:

	:::python
	>>> print(number:=17+71)
	88
	>>> number
	88
	>>>
	
Значення виразу `17+71` було присвоєно змінній `number`, 
і це ж значення стало аргументом для функції `print`. 

Ще приклад. Припустимо треба отримувати від користувача ввід і запам'ятовувати його поки користувач не введе "stop". 

	:::python
	>>> lines = []
	>>> while ((value:=input('Введіть що-небуть: ')).lower() != 'stop'):
	...     lines.append(value)
	...
	Введіть що-небуть: привіт
	Введіть що-небуть: пока
	Введіть що-небуть: StoP
	>>> lines
	['привіт', 'пока']
	>>>
	
Як правило вираз з моржовим оператором треба брати в дужки якщо він є складовою іншого виразу:

	:::python
	>>> x = 4 + (y := 8) # суто "синтетичний" приклад, не робіть так!
	>>> x
	12
	>>> y
	8
	>>>

Далі ще декілька прикладів: 

	:::python
	# Повторно використовуємо значення при формуванні списка: 
	items = [n := f(x), n * 2, n * 3]
	
	# len() викликається лише один раз
	if (n:= len(iterable)) > 10:
		print(f'Забагато елементів: {n}')
	
	# у спискових включеннях
	[value for x in data if (value := f(x)) > 0]
	
---
Стверджується що використання моржового оператора деколи дозволяє написати код коротше 
і зробити його більш читабельним. 
Також існує думка що введення в Python моржового оператора — це лише "примноження сутностей" і не "python-way". 

У деяких випадках використання моржового оператора може бути більш ефективним з точки зору обчислень. 
