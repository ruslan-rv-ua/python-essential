'''
seq = [1,3,5,7]
for i in seq:
	print(i,)
	
for i in [1,3,5,7]: print(i)
	
for i in range(4): print(i)
	
def __iter__(self):
	return self
'''

def my_for(iterable, callback_func):
	iterator = iter(iterable)
	while True:
		try:
			value = next(iterator)
			callback_func(value)
		except StopIteration:
			break
			
def loop(value):
	print(value)
	
for value in 'bye':
	print(value)
	
my_for('bye', loop)