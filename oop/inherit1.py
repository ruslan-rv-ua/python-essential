class Base:
	def __init__(self):
		self.base_prop = 'base property'
	def method(self):
		print("Це метод з класа Base.")
		print("У об'єкта класа Base є атрибут base_prop, його значення:", self.base_prop)

class Child(Base):
	def child_method(self):
		print("Це метод з класа Child.")
		print("Об'єкт класа Child має атрибут base_prop. Його створено в успадкованому конструкторі класа Base:", self.base_prop)
	
c = Child()
c.method()
c.child_method()

class Base:
	def __init__(self):
		self.__prop = 'property'
	def base_method(self):
		print("Це метод з класа Base.")
		print("У об'єкта класа Base є атрибут __prop, його значення:", self.__prop)

class Child(Base):
	def child_method(self):
		print("Це метод з класа Child.")
		print("Спробуємо дістатись до атрибута з метода успадкованого класа:", self.__prop)

c = Child()
c.base_method()
# c.child_method()



class A:
	pass
	
class B(A):
	pass
	
class C(B):
	pass
	
class A: pass
	
class B(A): pass
	
class C(B): pass
	
