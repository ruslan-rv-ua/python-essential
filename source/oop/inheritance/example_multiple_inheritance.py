class Horse:
	def run(self):
		print("Я біжу!")
	def say_hello(self):
		print("Я — кінь!")
class Eagle:
	def fly(self):
		print("Я лечу!")
	def say_hello(self):
		print("Я — орел!")

class Pegasus(Horse, Eagle):
# class Pegasus(Eagle, Horse):
	pass

p = Pegasus()
p.run()
p.fly()


###################################

class Horse(Animal):
	def say_hello(self):
		print("Я — кінь!")

class Eagle(Animal):
	def say_hello(self):
		print("Я — орел!")

# class Pegasus(Horse, Eagle):
class Pegasus(Eagle, Horse):
	pass

p.say_hello()
