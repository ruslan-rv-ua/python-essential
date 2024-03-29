# Модуль contextlib

Вбудований модуль `contextlib` 
надає декоратори та інші корисні функції для створення менеджерів контекста. 
Далі розглянемо лише деякі з них, 
з рештою ознайомтесь самостійно. 

## `contextmanager(func)`

	`func` — функція-генероатор
	
Декоратор, який створює менеджер контекста з функції-генератора. Використання наступне:

	:::python
	@contextmanager
	def foo(args):
		statements
		try:
			yield value
		except Exception as e:
			error handling (if any)
		statements

Коли інтерпретатор зустрічає інструкцію `with foo(args) as value`, він викликає функцію-генератор з вказаними аргументами. Ця функція виконується до першої інструкції `yield`. Значення, яке повертає інструкциія `yield`, пов'язується зі змінною `value`. Після цього починається виконання тіла інструкції `with`. По закінченню виконання тіла інструкції `with` відновлюється робота функції-генератора. Якщо всередині тіла інструкції `with` виникає виняткова ситуація, виняток буде передано функції-генератору, де його можна обробити. Якщо помилка не може бути оброблена функциєю-генератором, вона повинна повторно підняти виняток.

## `nested(mgr1, mgr2, ..., mgrN)`

Функція, яка викликає декілька менеджерів контекста (`mgr1, mgr2 і так далі) у вигляді єдиної операції. Повертає кортеж, який містить різні значення які повертаються инструкціями `with`. 
Інструкція:

	`with nested(m1,m2) as (x,y)`
	
це те ж саме, що і інструкція 

	`with m1 as x: with m2 as y`
	
Варто зауважити, що якщо у вкладеному менеджері контекста буде перехоплено і оброблено виняток, то зовнішні менеджери не отримають про це ніякої інформації.

## `closing(object)`

Створює менеджер контекста, який автоматично повертає метод `object.close()` по закінченню виконання тіла інструкції `with`. 

## Додаткові матеріали

1. [Документація Python: оператор `with`](https://docs.python.org/3/reference/compound_stmts.html#with)
1. [Документація Python: модуль contextlib](https://docs.python.org/3/library/contextlib.html)
