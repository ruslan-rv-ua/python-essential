from typing import Iterable
from functools import reduce

def to_one_dimension_list(iterable: Iterable) -> list:
	def gen(iterable):
		for el in iterable:
			if isinstance(el, Iterable):
				yield from to_one_dimension_list(el)
			else:
				yield el
	return list(gen(iterable))

def to_one_dimension_list(list_: list) -> list:
	result = []
	for el in list_:
		result.extend(to_one_dimension_list(el) if isinstance(el, list) else [el])
	return result
from functools import reduce
	
def to_one_dimension_list(list_: list) -> list:
	return reduce(list.__add__, (to_one_dimension_list(el) if isinstance(el, list) else [el] for el in list_), [])
	
	
# tests
assert to_one_dimension_list([1, [2, 3, [4,5], 6]]) == [1, 2, 3, 4, 5, 6]
assert to_one_dimension_list([1, 2, 3]) == [1, 2, 3]
assert to_one_dimension_list([1, [[3]], 5]) == [1, 3, 5]