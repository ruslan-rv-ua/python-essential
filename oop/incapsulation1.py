class Person():
	def __init__(self, age):
		self.set_age(age)
	def get_age(self):
		return self.__age
	def set_age(self, age):
		if age > 0:
			self.__age = age
	age = property(get_age, set_age, None, "Person's age, full years")

p = Person(35)
