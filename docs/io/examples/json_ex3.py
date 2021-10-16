import json

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def f(self):
        pass

peter = Person('Петро', 20)
mary = Person('Мар\'яна', 19)

s = json.dumps(peter)