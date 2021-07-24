class Stack:
	def __init__(self):
		self.items = []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
		
s = Stack()
for i in range(1, 6):
	s.push(i)
for _ in range(3):
	print(s.pop())