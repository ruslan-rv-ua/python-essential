import pickle

class Person(object):
    def __init__(self, name, age, sibling=None):
        self.name = name
        self.age = age
        self.sibling = sibling

'''
peter = Person('Петро', 20)
mary = Person('Мар\'яна', 21, peter)
peter.sibling = mary

with open('people.bin', 'wb') as file:  # 'wb' - записуємо бінарний файл!
	pickle.dump([peter, mary], file)
'''	
	

with open('people.bin', 'rb') as file:
	data = pickle.load(file)

print(data[0].name)
print(data[0].sibling.name)
