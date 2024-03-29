<!---
Менеджери контекста дозволяють виділяти та звільняти ресурси суто по необхідності. 
Самим популярним прикладом менеджера контекста — використання оператора `with`.
-->

> ***Менеджер контекста*** (context manager) – об'єкт, який створює контекст виконання всередині оператора `with` і реалізує два методи: `_enter_` та `_exit_`. 

Менеджери контекста використовуються для збереження і відновлення глобального стану, 
блокування і розблокування ресурсів, 
автоматичного закрыття файлів та інше. 

Припустимо, у вас є дві пов'язані операції, 
які ви хочете виконати у парі, 
помістивши між ними блок кода. 
Менеджери контекста дозволяють зробити саме це. 
Наприклад: 

	:::python
	with open('some_file', 'w') as opened_file:
		opened_file.write('Hello!')
		
Цей код відкриває файл, 
записує в нього дані і закриває після цього файл. 
При виникненні помилки при запису даних в файл менеджер контекста спробує його закрити. 
Цей код є еквівалентним наступному: 

	:::python
	file = open('some_file.txt', 'w')
	try:
		file.write('Hello!')
	finally:
		file.close()
		
Порівнявши з попереднім блоком кода можна зауважити заміну шаблоного кода на використання `with`. 

<!---
Основна перевага використання `with` — це гарантія закрыття файла незалежно від того, 
як буде завершено вкладений код.
--->

Синтаксис конструкції `with ... as` виглядає так: 

	with <вираз> as <змінна>:
		<блок коду>
		
Частина `as ...` є необов'язковою. 
 
Якщо в конструкції `with ... as` було декілька виразів, 
то це еквівалентно декільком вкладеним інструкциіям. 
Наприклад: 

	with A() as a, B() as b:
		# some code

еквівалентнло наступному:

	with A() as a:
		with B() as b:
			# some code		

Розглянемо як можна створити власний менеджер контекста. 

## Контекст-менеджер як клас

Щоб об'єкт став менеджером контекста він має реалізовувати два спеціальних метода:

- `__enter__()`
- `__exit__()`

Нагадаємо собі ще раз конструкцію `with`:

	with <вираз> as <змінна>:
		<блок коду>
	
При виконанні даного блока відбувається наступне: 

1. Виконується вираз в конструкції `with ... as`.
1. Завантажується спеціальний метод `__exit__` для подальшого використання. 
1. Виконується спеціальний метод `__enter__`. Якщо конструкція `with` включає в себе `as`, то значення,  яке повертається методом `__enter__` пов'язується зі вказаною змінною.
1. Виконується блок коду.
1. Викликається метод `__exit__`, незалежно чи виконався блок коду чи під час його виконання сталась виняткова ситуація. 

Метод `__enter__()` має повертати ресурс, над яким виконуються дії в рамках даного контекста. 

У методі `__exit__()` можна обробити виняткові ситуації, які виникли під час виконання блока коду. Йому передаються три параметри: 

- exception_class — клас винятка
- exception_value — екземпляр винятка
- traceback — інформація про виняток

Якщо під час виконання блока жодного винятка не було піднято, усім цим параметрам передається значення `None`. 

Якщо метод `__exit__()` повертає `True` — вважається, 
що винятки оброблено у цьому методі і нагору вони не піднімаються. 

Давайте спробуємо створити власний контекст-менеджер. 

Припустимо нам треба виконати певні дії 
помінявши перед цим поточну робочу директорію нашої програми у файловій системі, 
а потім встановити поточну директорію такою, як була раніше. 
Нам знадобляться дві функції з модуля `os`: 

- `os.chdir()` — встановлює поточну директорію
- `os.getcwd()` — повертає поточну директорію

Наш менеджер контекста може виглядати так:

	:::python
	>>> from os import chdir, getcwd
	>>> class cd:
	...     def __init__(self, path):
	...             self.path = path
	...     def __enter__(self):
	...             self.old_path = getcwd()
	...             chdir(self.path)
	...     def __exit__(self, c, e, t):
	...             chdir(self.old_path)
	...             return False
	...
	>>>

Спробуємо скористатись щойно створеним менеджером контекста (у вас результат буде іншим):

	:::python
	>>> print(getcwd())
	c:\\dev\with
	>>> with cd("/"):
	...     print(getcwd())
	...
	c:\
	>>> print(getcwd())
	c:\\dev\with
	>>>

## Додаткові матеріали

1. [Документація Python: оператор `with`](https://docs.python.org/3/reference/compound_stmts.html#with)

<!--
https://python-scripts.com/contextlib

--->