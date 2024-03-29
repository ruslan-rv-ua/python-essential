Бувають ситуації, коли не можна однозначно визначити, чи відбулась помилка у програмі, чи ні. 
Начебто і виникла певна неоднозначна (виняткова) ситуація, 
але програма може продовжувати роботу. 
Було б непогано сповістити про цей факт користувача чи програміста, 
щоб він принаймі знав, що відбулось щось "незвичайне" і звернув на це увагу. 

В Python для цього є механізм так званих "попереджень". 
Це схоже на винятки: 
інформація про виняткову ситуацію виводиться у стандартний потік помилок, 
але програма не припиняє свою роботу. 

Базовим класом для попереджень є `Warning`, який успадковано від `Exception`. 

	:::python
	>>> Warning
	<class 'Warning'>
	>>> Warning.mro()
	[<class 'Warning'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>]
	>>>
	
Від цього класа успадковано класи стандартних для Python попереджень. 
Також ми можемо створити власні попередження, свої класи успадковуємо від `UserWarning`:

	:::python
	>>> UserWarning.mro()
	[<class 'UserWarning'>, <class 'Warning'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>]
	>>> class DeprecatedFeature(UserWarning):
	...     pass
	...
	>>>	

## "Підйом" попереджень

Вивести попередження найпростіше за допомогою функції `warn` з вбудованого модуля `warnings`:

	:::python
	warn(message, category=UserWarning, stacklevel=1)


* `message` — обов'язковий параметр. Рядок-повідомлення, або екземпляр класа або підкласа Warning (у цьому випадку параметр `category` встановлюється автоматично).
* `category` — опціональний параметр, клас попередження.
* `stacklevel` — рівень вкладеності функцій, починаючи з якого необхідно виводити вміст стека викликів. Корисно, наприклад, для функцій-обгорток для вивода попереджень, де необхідно задати `stacklevel=2`, щоб попередження відносилось до місця виклику даної функції, а не самої функції.

Приклад:

	:::python
	from warnings import warn

	class IncorrectNameWarning(UserWarning):
		pass
		
	class Person:
		def __init__(self, name):
			if len(name.split()) > 3:
				warn(
					'Name format maybe incorrect:' + name,
					IncorrectNameWarning,
					stacklevel=2
				)
			self._name = name
		@property
		def name(self):
			return self._name
			
			
	p = Person('Гассан Абдуррахман ібн Хоттаб')
	print(p.name)
	print()
	p1 = Person('Еріх Марія Ремарк')
	print(p1.name)
		
В результаті виконання цього коду отримаємо приблизно таке:

	:::python
	c:\dev\warning_test.py:21: IncorrectNameWarning: Name format maybe incorrect:Гассан Абдуррахман ібн Хоттаб
	  p = Person('Гассан Абдуррахман ібн Хоттаб')
	Гассан Абдуррахман ібн Хоттаб
	>>>	
	
Зверніть увагу, що інтерпретатор повідомив нам, що попередження відноситься до наступного рядка програми: 

	:::python
	p = Person('Гассан Абдуррахман ібн Хоттаб')
	
Це набагато інформативніше, 
ніж якби нам повідомили, 
що попередження віднгоситься до коду в конструкторі класа, 
атже у такому разі невідомо, 
конструювання якого конкретного екземпляра призвело до появи попередження. 
Досягли ми цього задавши параметр `stacklevel=2` для функції `warn`, 
тобто ми почали з другого рівня стеку викликів. 

Детальніше про використання попереджень можна дізнатись з офіційної документації Python.

## Додаткові матеріали

[Документація Python: попередження](https://docs.python.org/3/library/warnings.html)