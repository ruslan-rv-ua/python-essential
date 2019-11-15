# type hinting
def f(x:int)->str:
	return str(x)
	

class A:
	def __setattr__(self, name, value):
		self.name = value
	# def __setattr__(self, name, value):
		# self.__dict__[name] = value
		
obj = A()
obj.x = 7
print(obj.x)
		
		
class MySeq:
	def __init__(self, data):
		self.data = data
	def __getattr__(self, name):
		return self.data[int(name[1:])]
		
l = MySeq([1,2,3,4,5])
s = MySeq('abcde')



class Dict(dict):
	def __getattr__(self, name):
		return self[name]
		
d = Dict({
	'k1': 11,
	'k2': 22,
})



		