class Fibo:
	def __init__(self, max_count):
		self.max_count = max_count
		self.count = 0
		self.first, self.second = 1, 1
	def __iter__(self):
		return self
	def __next__(self):
		self.count += 1
		if self.count > self.max_count:
			raise StopIteration
		elif self.count > 2:
			self.first, self.second = self.second, self.first + self.second
			return self.second
		else:
			return 1
			
f = list(Fibo(3))
print(f)
		