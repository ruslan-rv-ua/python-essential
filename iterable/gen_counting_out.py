def counting_out(max_count):
	count = 1
	while count <= max_count:
		yield count
		count += 1

c = counting_out(5)
l = list(c)
print(l)
