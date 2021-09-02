class MyInt(int):
	def __new__(cls, value):
		obj = int.__new__(cls, value[1:-1])
		return obj
		
x = MyInt('<1>')
