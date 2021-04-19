# Foydalanuvchidan ikkita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi 
#haqida xabarni chiqaring
x = float(input('1-sonni kiriting: '))
y = float(input('2-sonni kiriting: '))
if x == y:
	print('Sonlar teng')
elif x > y:
	print(f'{x}>{y} dan katta')
elif x < y:
	print(f'{x}<{y} dan kichik')