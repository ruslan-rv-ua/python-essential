'''
def fibo_generator(max_count):
	if max_count >= 1:
		yield 1
	if max_count >= 2:
		yield 1
	first, second = 1, 2
	count = 3
	while count <= max_count:
		yield second
		first, second = second, first + second
		count += 1

'''		
def fibo_generator(max_count):
	first, second = 0, 1
	for _ in range(max_count):
		yield second
		first, second = second, first + second
	
f_gen = fibo_generator(100000)
l = list(f_gen)
print(len(l))
print(l[:10])
# for i in fibo_generator(100000):
# 	pass

# print(list(f_gen))


