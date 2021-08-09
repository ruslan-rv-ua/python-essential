# Успадкування і приватні атрибути

Як нам вже відомо, атрибути, які починаються з двох символів підкреслення (але не закінчуються ними) є приватними атрибутами класа. Поза видимістю класа до таких атрибутів застосовується механізм `name mangling` (спотворення імені), тобто такі атрибути "поза класом" будуть мати інші імена (клас+атрибут), у тому числі і в успадкованих класах. Це дозволяє "приховати" внутрішню реалізацію класа навіть для класів, які від нього успадкуються. Приклад:

	:::python
	>>> class Base:
	...     def __init__(self):
	...             self.__prop = 'property'
	...     def base_method(self):
	...             print("Це метод з класа Base.")
	...             print("У об'єкта класа Base є атрибут __prop, його значення:", self.__prop)
	...
	>>> class Child(Base):
	...     def child_method(self):
	...             print("Це метод з класа Child.")
	...             print("Спробуємо дістатись до атрибута з метода успадкованого класа:", self.__prop)
	...
	>>> c = Child()
	>>> c.base_method()
	Це метод з класа Base.
	У об'єкта класа Base є атрибут __prop, його значення: property
	>>> c.child_method()
	Це метод з класа Child.
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "<stdin>", line 4, in child_method
	AttributeError: 'Child' object has no attribute '_Child__prop'
	>>>

	





