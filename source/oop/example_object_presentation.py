t = 'text'
# print(str(t))
# print(repr(t))

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __str__(self):
		return f"{self.name}, {self.age} years old"
	def __repr__(self):
		# return f'Person({repr(self.name)}, {repr(self.age)})'
		return f'Person({self.name!r}, {self.age!r})'

p = Person('Alice', 25)
print(p)