class CountingOUt:
	def __init__(self, count_to):
		self.current = 1
		self.count_to = count_to
	def __iter__(self):
		return self
	def __next__(self):
		if self.current <= self.count_to:
			current = self.current
			self.current += 1
			return current
		else:
			raise StopIteration
		
c = CountingOUt(5)
for n in c:
	print(n)
for n in c:
	print(n)	

