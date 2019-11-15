from functools import lru_cache
from sys import setrecursionlimit

def memoize(f):
	def wrapper(*args, **kwargs):
		key = args + tuple(kwargs.items())
		if key not in wrapper.memo:
			wrapper.memo[key] = f(*args, **kwargs)
		return wrapper.memo[key]
	wrapper.memo = {}
	return wrapper

def memoize(f):
	def wrapper(n):
		if n not in wrapper.memo:
			wrapper.memo[n] = f(n)
		return wrapper.memo[n]
	wrapper.memo = {}
	return wrapper
	
# @memoize
@lru_cache(maxsize=5)
def fibo(n):
	return fibo(n-1) + fibo(n-2) if n > 2 else 1

from collections import Counter
c = Counter()
# @lru_cache(maxsize=5)
def fiboc(n):
	c[n] += 1
	return fiboc(n-1) + fiboc(n-2) if n > 2 else 1
fiboc(10)
for arg, count in c.most_common():
	print(f'{count} - {arg}')


	
# setrecursionlimit(9000)
from math import sqrt
SQRT5 = sqrt(5)
PHI =  (sqrt(5) + 1) / 2
def fibo2(n):
	return int(pow(PHI, n) / SQRT5 + 0.5)
	return int(pow((sqrt(5) + 1) / 2, n) / sqrt(5) + 0.5)
	