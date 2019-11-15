class Horse:
	def run(self):
		print("Я біжу!")

		
class Eagle:
	def fly(self):
		print("Я лечу!")

		
class Pegasus(Horse, Eagle):
	pass

	
p = Pegasus()
p.run()
p.fly()

h = Horse()
# h.fly()



class A:
	pass
	
class A():
	pass
	
class A(object):
	pass