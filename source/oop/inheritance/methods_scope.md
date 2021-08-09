# Пошук методів і лінеарізація

Як згадувалось раніше, доступ до атрибутів базового класа можна отримати шляхом прямого вказання назви класа і, власне, атрибута. Існує ще один спосіб, який позбавлений недоліків попереднього.

Існує спеціальний клас `super`, екземпляри якого є спеціальними проксі-об'єктами (об'єктами-посередниками), які прив'язані до даної ієрархії класів і які надають доступ до атрибутів наступного класа в лінеаризації 
того класа, в якому було створено об'єкт `super`.

Таким чином, за допомогою `super` можна отримати доступ до атрибутів суперкласа, не вказуючи його імені, причому це буде давати коректні результати навіть при використанні множинного успадкування.

Приклад:

	:::python
	super(MyClass, self).method()
	
Якщо при створенні екземпляра класа `super` не вказувати параметри, то автоматично будуть отримані поточні клас і його екземпляр:

	:::python
	super().method()
	
Приклад використання `super()` при простому успадкуванні:

	:::python
	>>> class Person:
	...     def __init__(self, name):
	...             self.name = name.title()
	...     def say_hello(self):
	...             print('Hi, I am', self.name)
	...
	>>>
	... class Employee(Person):
	...     def __init__(self, name, salary):
	...             super().__init__(name)
	...             self.salary = salary
	...     def say_hello(self):
	...             super().say_hello()
	...             print('My salary is', self.salary)
	...
	>>>
	>>> e = Employee('janE', 120)
	>>> e.say_hello()
	Hi, I am Jane
	My salary is 120
	>>>

З класа `Employee` ми отримуємо доступ до атрибутів класа `Person` за допомогою `super()`. Зауважте: нам тепер не треба вказувати навіть поточний екземпляр класа.

Тепер звернемось до множинної спадковості:

	:::python
	>>> class Animal:
	...     def __init__(self):
	...             self.can_run = False
	...             self.can_fly = False
	...
	>>>
	>>> class Horse(Animal):
	...     def __init__(self):
	...             super().__init__()
	...             self.can_run = True
	...
	>>>
	>>> class Eagle(Animal):
	...     def __init__(self):
	...             super().__init__()
	...             self.can_fly = True
	...
	>>>
	>>> class Pegasus(Horse, Eagle):
	...     pass
	...
	>>> p = Pegasus()
	>>> p.can_run
	True
	>>> p.can_fly
	True
	>>>
	
Щоб краще зрозуміти, як це працює, давайте спочатку вивчимо лінеаризацію класа `Pegasus`:
	
	:::python
	>>> Pegasus.mro()
	[<class '__main__.Pegasus'>, <class '__main__.Horse'>, <class '__main__.Eagle'>, <class '__main__.Animal'>, <class 'object'>]
	>>>
	
Тепер покроково:

1. В класі `Pegasus` конструктора не оголошено, отже згідно лінеаризації викликаємо конструктор класа `Horse`
1. В конструкторі `Horse` за допомогою `super()` викликається конструктор "попереднього" класа, згідно MRO це буде конструктор класа `Eagle`
1. В конструкторі `Eagle` за допомогою `super()` викликається конструктор "попереднього" класа, згідно MRO це буде конструктор класа `Animal`
	
	
	
	
	
	
	

## Додаткові матеріали

[C3-линеаризация](https://ru.wikipedia.org/wiki/C3-%D0%BB%D0%B8%D0%BD%D0%B5%D0%B0%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F)

<!---
https://otus.ru/nest/post/165/
--->