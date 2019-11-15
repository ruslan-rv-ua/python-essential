with open('some_file.txt', 'rb', encoding='UTF-8') as file:
	data = file.read()
	# data = bytearray(100)
	# size = file.readinto(data)
	
s = data.decode('UTF-8')
print(s)