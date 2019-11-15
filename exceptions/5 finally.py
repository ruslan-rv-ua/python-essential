def f():
	try:
		2 / 0
	except Exception as e:
		return 'We have catched: ' + str(e)
	finally:
		print('Finally block is always executed')

print(f())

