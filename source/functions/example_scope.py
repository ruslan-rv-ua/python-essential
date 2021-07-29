def outer(arg):
	def inner(x):
		return x*x
    return inner(arg)

#-----
LEGB
Local — локальна (всередин≥ функції)
Enclosing — локальна область функцій-обгорток, які у свою чергу містять інші функції
Global — глобальна (модуль)
Built-in — вбудована (зарезервовані значення Python)

# enclosing

def outer():
    x = "x modified inside outer"
    def inner():
        print("inner():", x)
    inner()
    print("outer():", x)

outer()

# nonlocal

def outer():
    x = "x modified inside outer"
    def inner():
		nonlocal x
        x = "x modified inside inner"
        print("inner():", x)
    inner()
    print("outer():", x)

outer()

min(1, 2)
def min():
	return 'Nothing to do'
	
print(min(1,2))


def q(a, b, c):
	
	def helper(x):
		return a*x*x + b*x + c
		
	return helper
	
	
