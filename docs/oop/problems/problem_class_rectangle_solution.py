'''
Реалізуйте клас Rectangle який описує прямокутник із заданими сторонами. 
Реалізуйте представлення для екземплярів класа. 
Реалізуйте метод get_square() який повертатиме площу прямокутника.
'''
class Rectangle:
	# ваш код починається тут
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def get_square(self):
		return self.a * self.b
	def __repr__(self):
		return f'Rectangle({self.a!r}, {self.b!r})'
	def __str__(self):
		return f'Rectangle {self.a}x{self.b}'

	
# не міняйте наступний код, це тести
r = Rectangle(7, 3)
print(r)
print(f'{r!r}')
assert r.get_square() == 21