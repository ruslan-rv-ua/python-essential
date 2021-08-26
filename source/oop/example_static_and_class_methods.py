class A:
	def i(self):
		print('instance method called', self)
	@classmethod
	def c(cls):
		print('class method called', cls)
	@staticmethod
	def s():
		print('static method called')
		
obj = A()


class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	@classmethod
	def parse(cls, string):
		parts = string.split(' ')
		return cls(parts[0], int(parts[1]))
		
	@staticmethod
	def is_adult(age):
		return age >= 18

p = Person('Jane', 25)
p = Person.parse('Jane 25')
r = Person.is_adult(25)
