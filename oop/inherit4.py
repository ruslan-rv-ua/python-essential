class Person:
	def __init__(self, name):
		self.name = name[0].upper() + name[1:].lower()
	def say_hello(self):
		print('Hi, I am', self.name)




		
class Employee(Person):
	def __init__(self, name, salary):
		Person.__init__(self, name)
		self.salary = salary
	def say_hello(self):
		Person.say_hello(self)
		print('My salary is', self.salary)
		
p = Person('john')
p.say_hello()
e = Employee('janE', 120)
e.say_hello()

