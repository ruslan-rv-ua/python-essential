class Person:
	def __init__(self, name, email):
		self.name = name
		self.email = email
	def __str__(self):
		return f"{self.name} <{self.email}>"
	def __repr__(self):
		return f"Person('{self.name}', '{self.email}')"
