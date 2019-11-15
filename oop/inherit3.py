class A:
	def f1(self):
		print('f1 method in class A')

		
class B(A):
	def f2(self):
		print('f2 method in class B')

		
class C(B):
	def f2(self):
		print('f2 method in class C')
	def f3(self):
		print('f3 method in class C')

		
for cls in [A,B,C]:
	print('Class', cls.__name__,'mro: ' ,', '.join([c.__name__ for c in cls.mro()]))
		
obj = C()

