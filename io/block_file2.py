# https://stackoverflow.com/questions/11853551/python-multiple-users-append-to-the-same-file-at-the-same-time

from time import sleep
t=2
f = open('temp.txt', 'w')
while True:
	f.write(str(t))
	f.flush()
	sleep(t)