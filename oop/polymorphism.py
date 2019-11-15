from winsound import Beep


class Beeper:
	def __init__(self, times):
		self.times = times
	def __str__(self):
		for i in range(self.times):
			Beep(1000 + 100*i, 50)
		return ''


		
b = Beeper(10)
print(b)


class Duck:
    def quack(self):
        print('Кря!')

class Person:
    def __init__(self, name):
        self._name = name
    def quack(self):
        print('Людина імітує крякання: "Кря!"')
    @property
    def name(self):
        return self._name

def in_the_forest(duck):
    duck

donald = Duck()
john = Person('Іван')
donald.quack()
john.quack()