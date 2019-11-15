class T:
	CELSIUS = 1
	FAHRENHEIT = 2
	def __init__(self, t, scale=CELSIUS):
		if scale == T.CELSIUS:
			self.c = t
		else:
			self.f = t
	@property
	def f(self):
		return (self.c * 9/5) + 32
	@f.setter
	def f(self, f):
		self.c = (5/9) * (f - 32)
	def __str__(self):
		return str(self.c) + 'C'
	def __repr__(self):
		return f"T({self.c}C)"
	def __add__(self, t):
		return T(self.c + t.c)
		


