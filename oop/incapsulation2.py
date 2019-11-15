class Person:
	def __init__(self, age):
		self.__age = 0
		self.age = age
	@property
	def age(self):
		return self.__age
	@age.setter
	def age(self, age):
		if age > 0:
			self.__age = age

p = Person(35)
