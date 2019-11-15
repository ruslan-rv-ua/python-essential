class Animal:
	pass


class Eagle(Animal):
	pass


class Horse(Animal):
	pass


class Pegasus(Eagle, Horse):
	pass

class Pegasus(Horse, Eagle):
	pass
	
def print_mro(cls):
	print('MRO for class', cls.__name__, end=': ')
	print(', '.join(c.__name__ for c in cls.mro()))
	
print_mro(Pegasus)
	
p = Pegasus()
p.hello()