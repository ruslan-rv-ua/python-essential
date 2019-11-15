from time import sleep
t=5
f = open('temp.txt', 'w')
while True:
	f.write(str(t))
	f.flush()
	sleep(t)