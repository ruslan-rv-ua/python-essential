from datetime import date

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	@classmethod
	def from_birth_year(cls, name, year):
		return cls(name, date.today().year - year)
	@staticmethod
	def is_adult(age):
		return age > 18
		