def pow2_gen():
	for x in range(11):
		if x % 2 == 0:
			yield 2 ** x
		
print(sum(pow2_gen()))
		
g = (2**x for x in range(11) if x%2==0)
print(sum(g))
print(sum(2**x for x in range(11) if x%2==0))

def white_fields_generator():
	for column in range(8):
		for row in range(8):
			if (column+row) % 2 == 1:
				yield 'abcdefgh'[column] + '12345678'[row]
				
print(' '.join(white_fields_generator()))

white_fields_generator = (
	'abcdefgh'[column] + '12345678'[row]
	for column in range(8)
	for row in range(8)
	if (column+row) % 2 == 1
)

print(' '.join(white_fields_generator))

# white_fields_generator = (column + row for column in columns for row in rows if (columns.index(column)+rows.index(row)) % 2 == 1)
# w = white_fields_generator
# for _ in range(8):
#	print(next(white_fields_generator))

	
# white_fields_generator = (column + row for column in columns for row in rows if (columns.index(column)+rows.index(row)) % 2 == 1)
# print(list(w)[:8])


