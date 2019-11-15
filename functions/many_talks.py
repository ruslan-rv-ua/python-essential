from collections import namedtuple

GENDER = namedtuple('gender', 'masculine feminine neuter'.upper())(0, 1, 2)

hunds = {
	0: '',
	1: 'сто',
	2: 'двісті',
	3: 'триста',
	4: 'чотириста',
	5: 'п\'тсот',
	6: 'шістсот',
	7: 'сімсот',
	8: 'вісімсот',
	9: 'дев\'ятсот',
}

decs = {
	0: '',
	10: 'десять',
	11: 'одинадцять',
	12: 'дванадцять',
	13: 'тринадцять',
	14: 'чотирнадцять',
	15: 'п\'ятнадцять',
	16: 'шістнадцять',
	17: 'сімнадцять',
	18: 'вісімнадцять',
	19: 'дев\'ятнадцять',
	20: 'двадцять',
	30: 'тридцять',
	40: 'сорок',
	50: 'п\'ятдесят',
	60: 'шістдесят',
	70: 'сімдесят',
	80: 'вісімдесят',
	90: 'дев\'яносто',
}

ones = {
	0: ('', '', ''),
	1: ('один', 'одна', 'одне'),
	2: ('два', 'дві', 'двоє'),
	3: ('три', 'три', 'троє'),
	4: ('чотири', 'чотири', 'четверо'),
	5: ('п\'ять', 'п\'ять', 'п\'ять'),
	6: ('шість', 'шість', 'шість'),
	7: ('сім', 'сім', 'сім'),
	8: ('вісім', 'вісім', 'вісім'),
	9: ('дев\'ять', 'дев\'ять', 'дев\'ять'),
}

def trio(number, gender=GENDER.MASCULINE, forms=('','',''), zero=True):
	try:
		gender = dict(m=0, f=1, n=2)[gender.lower()]
	except:
		print('gender not string')
		pass
	res = []
	h, d = divmod(number, 100)
	res.append(hunds[h])
	if d in decs:
		res.append(decs[d])
		# res.append(forms.split(',')[2])
		form = 2
	else:
		d, rest = divmod(d, 10)
		res.append(decs[d*10])
		res.append(ones[rest][gender])
		if rest == 1:
			form = 0
		elif 1 < rest < 5:
			form = 1
		else:
			form = 2
	res = [word for word in res if word]
	if not res and zero:
		res.insert(0, 'нуль')
	try:
		forms = [form.strip() for form in forms.split(',')]
	except:
		pass
	res.append(forms[form])
	return ' '.join(res)

# r = trio(922, GENDER.FEMININE, 'гривня,гривні,гривень')
r = trio(0, gender='f', forms='гривня,гривні,гривень')
print(r)
