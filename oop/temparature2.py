from functools import total_ordering

@total_ordering
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
	def __eq__(self, t):
		return self.c == t.c
	def __gt__(self, t):
		return self.c > t.c

		
t1 = T(0)
print(f"t1={t1}")
t2 = T(64, T.FAHRENHEIT)
print(f"t2={t2}")
print(f"t1 < t2: {t1 < t2}")

