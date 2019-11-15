with open('some_file.txt', 'w') as file:
	pass

	
__enter__(self)

__exit__(self, exc_class, exc_obj, exc_traceback)

import os

class cd:
	def __init__(self, path):
		self.path = path
	def __enter__(self):
		self.old_path = os.getcwd()
		os.chdir(self.path)
	def __exit__(self, c, e, t):
		os.chdir(self.old_path)

print(os.getcwd())
with cd("\\"):
    print(os.getcwd())
print(os.getcwd())

import io
print(io.IOBase.__enter__)
