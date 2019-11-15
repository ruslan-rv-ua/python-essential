class Person:
	def __init__(self, name):
		self.name = name[0].upper() + name[1:].lower()
	def say_hello(self):
		print('Hi, I am', self.name)

		
class Employee(Person):
	def __init__(self, name, salary):
		super().__init__(name)
		self.salary = salary
	def say_hello(self):
		super().say_hello()
		print('My salary is', self.salary)


e = Employee('janE', 120)
e.say_hello()







class Animal:
	def __init__(self):
		self.can_run = False
		self.can_fly = False


class Horse(Animal):
	def __init__(self):
		super().__init__()
		self.can_run = True


class Eagle(Animal):
	def __init__(self):
		super().__init__()
		self.can_fly = True


class Pegasus(Horse, Eagle):
	pass
	
p = Pegasus()











