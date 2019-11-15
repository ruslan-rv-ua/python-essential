import io
s = io.StringIO('Hello, Alice!')
s.write('Вєтаю')
s.seek(1)
s.write('і')
s.seek(0, io.SEEK_END)
s.seek(s.tell()-len('alice')-1)
s.write('Алісо')
print(s.tell(), s.getvalue())

with io.StringIO() as stream:
	for number in range(5):
		print(number, file=stream)
	print(stream.getvalue())
		