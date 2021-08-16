'''
class Person:
	about = 'Клас описує людину'
	print(about)
	
Person.about
'''
########
class Person:
	about = 'Клас описує людину'
	def print():
		print(Person.about)

Person.print()
########
p1 = Person()
p2 = Person()

p1.print()
Person.print(p1)