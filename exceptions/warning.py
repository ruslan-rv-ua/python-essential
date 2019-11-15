from warnings import warn

class IncorrectNameWarning(UserWarning):
	pass
	
class Person:
	def __init__(self, name):
		if len(name.split()) > 3:
			warn(
				'Name format maybe incorrect:' + name,
				IncorrectNameWarning,
				stacklevel=2
			)
		self._name = name
	@property
	def name(self):
		return self._name
		
		
def main():
	p = Person('Гассан Абдуррахман ібн Хоттаб')
	print(p.name)
	print()
	p1 = Person('Еріх Марія Ремарк')
	print(p1.name)
	
	
	
if __name__ == '__main__':
	main()

	