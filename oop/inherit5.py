class L0:
	p_a = 'L0'
	def a(self):
		print('L0')
	
class L1A(L0):
	p_a = 'L1 A'
	def a(self):
		print('L1A')
	
class L1B(L0):
	p_a = 'L1 B'
	def a(self):
		print('L1B')	
		

class L2(L1A, L1B):
	pass
	
o = L2()