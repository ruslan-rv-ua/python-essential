try:
	f = open('file.txt')
	txt = f.read()
	f.close()
	f = open('file.txt', 'a')
	f.write(txt)
	f.close()
except OSError:
	print('can not read the file')
	
# PermissionError
	
try:
	f = open('file.txt')
	txt = f.read()
	f.close()
except OSError:
	print('can not read the file')
else:
	f = open('file.txt', 'a')
	f.write(txt)
	f.close()
