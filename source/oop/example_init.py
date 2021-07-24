class Person:
	pass
	
p1 = Person()
p1.name = 'Даринка'
p1.name
p2 = Person()
# p2.name

class Person:
	def __init__(self, name):
		self.name = name
		
p1 = Person('Даринка')
p1.name
# p2 = Person()

class Person():
	def __init__(self, name, phone=''):
		self.name = name
		self.phone = phone
		
p1 = Person('Даринка', '322-223')
p2 = Person('Ярик')
p1.name, p1.phone
p2.name, p2.phone


class News2Telegram:
	def __init__(self):
		self.parser = NewsParser()
		self.bot = TelegramBot()