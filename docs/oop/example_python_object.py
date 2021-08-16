from sys import getrefcount
t = 'some text'
l = [t, t]
print(getrefcount(t))
