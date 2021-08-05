## intro
x = 'global'
def f():
	x = 'local'
	print(x)
f()

## global
my_name = 'my_name'
from random import *
print(globals().keys())

## local
def add_two(arg):
    var = 2
    print(list(locals().keys()))
    return arg + var


## enclosing
def outer():
    print('Start outer()')
    def inner():
        print('Start inner()')
        print('End inner()')
    inner()
    print('End outer()')
outer()

## LEGB
len = 'global'
def outer():
    len = 'enclosing'
    def inner():
        len = 'local'
        print(len)
    inner()
outer()

