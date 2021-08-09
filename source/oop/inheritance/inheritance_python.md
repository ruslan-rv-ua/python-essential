# Успадкування в Python

В Python синтаксис для наслідування класів виглядає наступним чином:

	:::python
	class <subclass>(<superclass>):
		<subclass attributes>
		
Розглянемо на прикладі.

	:::python
	>>> class Base:
	...     def __init__(self):
	...             self.base_prop = 'base property'
	...     def method(self):
	...             print("Це метод з класа Base.")
	...             print("У об'єкта класа Base є атрибут base_prop, його значення:", self.base_prop)
	...
	>>> class Child(Base):
	...     def child_method(self):
	...             print("Це метод з класа Child.")
	...             print("Об'єкт класа Child має атрибут base_prop. Його створено в успадкованому конструкторі класа Base:", self.base_prop)
	...
	>>> c = Child()
	>>> c.method()
	Це метод з класа Base.
	У об'єкта класа Base є атрибут base_prop, його значення: base property
	>>> c.child_method()
	Це метод з класа Child.
	Об'єкт класа Child має атрибут base_prop. Його створено в успадкованому конструкторі класа Base: base property
	>>>
	
Що відбувається у цьому прикладі?

1. Клас Child успадковує від класа Base два методи: конструктор і метод `method()`.
1. Також клас Child має свій власний метод: `child_method()`.
1. При створенні об'єкта класа Child буде викликано успадкований конструктор класа Base. У конструкторі для об'єкта створюється атрибут base_prop. У об'єктів класа Child теж буде створено цей атрибут.

