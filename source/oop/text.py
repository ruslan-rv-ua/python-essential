class Int(int):
	def __add__(self, other):
		return int(str(self) + str(other))
		
		
a = Int('2')
