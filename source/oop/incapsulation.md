# Інкапсуляція

Класи в ООП бувають великими і складними. В них може бути багато полів і методів, які не повинні використовуватись за його межами. Вони просто для цього не призначені. Вони свого роду внутрішні шестерні, які забезпечують нормальну роботу великого механізму.

Хорошою практикою вважається приховування усіх полів об'єктів, щоб запобігти прямого присвоєння значень з іншого місця програми. Їх значення можна змінювати і отримувати лише через виклики методів, спеціально для цього визначених.
Наприклад, якщо необхідно перевіряти значення, яке присвоюється певному полю на коректність, то робити це кожного разу в основному коді програми буде неправильним. Перевірочний код має бути розміщено у методі, котрий отримує дані для присвоення полю. А саме поле має бути закритим для доступу ззовні класа. У цьому випадку йому неможливо буде присвоїти недопустиме значенння.

> ***Інкапсуляція*** (encapsulation) — це механізм, який об'єднує дані і код, який маніпулює цими даними, а також захищає і те, і інше від зовнішнього втручання або неправильного використання.

Розглянемо приклад:

	:::python
	>>> class Person:
	...     def __init__(self, age):
	...             self.age = age
	...
	>>> p = Person(age=-35)
	>>> p.age
	-35
	>>> p.age = '35'
	>>> p.age
	'35'
	>>>
	
Поле age класа Person — це вік людини. У вищенаведеному прикладі ми двічі присвоїли некоректне значення цьому полю: при створенні об'єкта через конструктор і вказавши значення поля "напряму".



### Приховування атрибутів класа

В багатьох мовах програмування, які підтримують парадигму ООП, існують спеціальні модифікатори доступу атрибутів. Вони явно вказують, чи можна мати доступ до певного атрибуту класа "ззовні", чи цей атрибут доступний тільки всередині класа.

В Python механізму модифікаторів доступу не існує. 
Для імітації приховування атрибутів в Python використовується домовленість згідно якої якщо ідентифікатор атрибута починається з знака підкреслення, то цей атрибут призначено виключно для внутрішнього використання.

	:::python
	>>> class Person:
	...     def __init__(self, age):
	...             self._age = age
	...
	>>>
	
Але домовленість — це не синтаксичне правило мови програмування, і при великому бажанні її можна порушити:

	:::python
	>>> p = Person(35)
	>>> p._age
	35
	>>>	

Звісно, що порушувати домовленості — річ погана.

Можна ще більше приховати атрибут класа. Для цього його ідентифікатор має починатись не з одного, а з двох знаків підкреслення:

	:::python
	>>> class Person:
	...     def __init__(self, age):
	...             self.__age = age
	...
	>>> p = Person(35)
	>>> p.__age
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	AttributeError: 'Person' object has no attribute '__age'
	>>>
	
Невже якщо ідентифікатор атрибута починається з символів `__`, то до нього не можна отримати доступ ззовні класа? Насправді можна, але вже трохи важче. 
Необхідно вказати атрибут класа таким чином:

1. символ підкреслення
1. ім'я класа
1. ім'я атрибута як у класі, тобто з двома підкресленнями на початку:

Отже для вищенаведеного прикладу:

	:::python
	>>> p._Person__age
	35
	>>>
	
Зауважте, що це знову ж таки домовленість. В результаті "атрибут як він є" стає  замаскованим. Ззовні класа такого атрибута просто не існує. Для програміста ж наявність двох символів підкреслення перед іменем атрибута повинно сигналізувати, що чіпати його поза класом не слід взагалі.




### Сетери, гетери і делетери

OK, ми захистили поле від доступу. Але як тепер отримати його значення? Зробити це можна за допомогою метода:

	:::python
	>>> class Person:
	...     def __init__(self, age):
	...             self.__age = age
	...     def get_age(self):
	...             return self.__age
	...
	>>> p = Person(35)
	>>> p.get_age()
	35
	>>>

Так само за допомогою методів можна реалізувати присвоєння значень прихованим атрибутам класа:

	:::python
	>>> class Person:
	...     def __init__(self, age):
	...         self.set_age(age)
	...     def get_age(self):
	...         return self.__age
	...     def set_age(self, age):
	...         if age > 0:
	...             self.__age = age
	...
	>>> p = Person(35)
	>>> p.get_age()
	35
	>>> p.set_age(-35)
	>>> p.get_age()
	35
	>>>

В об'єктно-орієнтованому програмуванні прийнято імена методів для вилучення даних починати зі слова `get`(взяти), а імена методів, в яких полям присвоюються певні значення — зі слова `set`(встановити). А самі методи часто називають відповідно **сетерами** і **гетерами**. Існують також **делетери** — методи для видалення (`delete`) полів класа.

У вищенаведеному прикладі `get_age` — це гетер, а `set_age` — сетер. 
Зауважте що для встановлення значення для прихованого атрибута в конструкторі ми скористались сетером.




### Властивості

Значення, які характерезують стан об'єкта (атрибути), доступ до яких відбувається за допомогою сетерів і гетерів, називають **властивостями** (property).

Для створення властивості використовують функцію:

	 property(fget, fset, fdel, doc)
	 
де:

- fget — Функція, яка реалізує повернення значення властивості
- fset — Функція, яка реалізує встановлення значення властивості
- fdel — Функція, яка реалізує видалення значення властивості
- doc — рядок документації для властивості. Якщо не задано, то береться від `fget`

Усі параметри необов'язкові.

	:::python
	>>> class Person:
	...     def __init__(self, age):
	...             self.set_age(age)
	...     def get_age(self):
	...             return self.__age
	...     def set_age(self, age):
	...             if age > 0:
	...                     self.__age = age
	...     age = property(get_age, set_age, None, "Person's age, full years")
	...
	>>> p = Person(35)
	>>> p.age
	35
	>>> p.age = 18
	>>> p.age
	18
	>>> p.age = -18
	>>> p.age
	18
	>>>
	>>> help(Person.age)
	Help on property:

		Person's age, full years

	>>>

В Python також є ще один більш елегантний спосіб визначення властивостей за допомогою декораторів. 

Для створення властивості-гетера використовуємо:

	@property
	
Для створення властивості-сетера використовуємо:

	@<властивість-гетер>.setter
	
Перепишемо клас Person з використанням декораторів:

	:::python
	>>> class Person:
	...     def __init__(self, age):
	...             self.__age = 0
	...             self.age = age
	...     @property
	...     def age(self):
	...             return self.__age
	...     @age.setter
	...     def age(self, age):
	...             if age > 0:
	...                     self.__age = age
	...
	>>> p = Person(35)
	>>> p.age
	35
	>>> p.age = -18
	>>> p.age
	35
	>>> p = Person(-35)
	>>> p.age
	0
	>>>

Зверніть увагу на наступне:

- сетер визначається після гетера
- і сетер, і гетер називаються однаково — `age`. І оскільки гетер називається `age`, то над сетером встановлюється анотація @age.setter
- і до гетера і до сетера ми звертаємось через вираз p.age



### Обчислювані властивості

Давайте створимо клас у якому будемо зберігати значення температури, наприклад температури повітря. У різних країнах температуру повітря вимірюють по різних шкалах: в Україні — за Цельсієм, у, наприклад, США — за шкалою Фаренгейта. Спроектуємо наш клас таким чином, щоб з температурою можна було б працювати одразу у двох системах:

Перше що зробимо, це з'ясуємо як перевести температуру з градусів Цельсія у градуси Фаренгейта і навпаки:

	f = c *  9/5 + 32
    c = (f -32)* 5/9
	
Спроектуємо наш клас наступним чином:

- температуру будемо зберігати у градусах цельсія у властивості `c`
- якщо нам треба дізнатись температуру по Фаренгейту, ми звертатимемось до властивості `f`. Гетер автоматично переводитиме значення у градуси Фаренгейта використовуючи значення атрибута `c`
- сеттер властивості `f` буде встановлювати значення властивості `c`
- у конструкторі передбачимо спосіб вказати у якій шкалі ми задаємо температуру

Клас спроектовано, залишається, як завжди, записати це мовою Python:

	:::python
	>>> class T:
	...     CELSIUS = 1
	...     FAHRENHEIT = 2
	...     def __init__(self, t, scale=CELSIUS):
	...             if scale == T.CELSIUS:
	...                     self.c = t
	...             else:
	...                     self.f = t
	...     @property
	...     def f(self):
	...             return (self.c * 9/5) + 32
	...     @f.setter
	...     def f(self, f):
	...             self.c = (5/9) * (f - 32)
	...     def __str__(self):
	...             return str(self.c) + 'C'
	...     def __repr__(self):
	...             return f"T({self.c}C)"
	...
	>>> t1 = T(32, T.FAHRENHEIT)
	>>> t1
	T(0.0C)
	>>> t1.f
	32.0
	>>> t1.c
	0.0
	>>> t2 = T(0)
	>>> t2.f
	32.0
	>>> t2.c
	0
	>>> t2
	T(0C)
	>>>

