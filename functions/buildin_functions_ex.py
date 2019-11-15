'''
Типи даних у булевому контексті

Falsie Values (Хибні значення)
NoneType None 
int 0 
float 0.0
list [] 
dict {} 
tuple () 
все, у чого len() == 0 
'''
s = [True, '']
print(any(s))
1/0


# enumerate
persons = ['Петренко', 'Іваненко', 'Сидоренко', 'Михаайличенко']
res = enumerate(persons)
print(res)
res = list(enumerate(persons))
for num, person in enumerate(persons, start=1):
	print(num, person)


# id
a = 'wow'
b = a
id(a) == id(b)


