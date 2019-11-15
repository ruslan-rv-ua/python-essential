def mhash(bytes):
	return sum(bytes) % 256
	
c = 0
for a in range(256):
	for b in range(256):
		bb = bytes([a,b])
		# print('{:X}'.format(a*256+b), end=' - ')
		if mhash( bb ) == 1:
			print('{:X}'.format(a*256+b))
			c += 1
		# print()