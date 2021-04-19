# 10 IF-ELSE

avtolar = ['audi','bmw','volvo','kia','hyundai']

for avto in avtolar:  # avtolar ichidadi har bir avto uchun ...
	if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
		print(avto.upper())  # avto nomini hamma harflarini katta bilan yoz.
	else:  # aks holda ... 
		print(avto.title())  # avto nomini faqat birinchi harfini katta bilan yoz.


ism = 'Ali'
ism.lower() == 'ali' # True ifodasini beradi

ism = input("Ismingiz nima?\n>>>")

if ism.lower() != 'ali':
	print(f"Salom {ism.title()}, uzr biz Alini kutyapmiz!")
else:
	print("Salom, Ali")


javob = float(input("12x6 nechchiga teng?\n>>>"))

if javob != 72:
	print("Javob xato!")

yosh = int(input("Yoshingiz nechchida? "))

if yosh >= 18: # yosh 18 dan katta yoki teng bo'lsa
	print("Xush kelibsiz!")
else: # ask holda
	print("Kirish mumkin emas!")


login = input('yangi login tanlang: ')

if len(login) <= 5:
	print("Login 5 ta elementdan kam bo'lmasligi shart")


yil = int(input("Tug'ilgan yilingizni kiriting: "))

if 2021-yil > 18:
	print('Xush kelibsiz!')
else:
	print(f'Yoshingiz {2021-yil} da ekan.\nKirish mumkin emas')

yosh = int(input('Yoshingiz nechchida?'))

if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")


x, y = 25, 50  # x=25 va y=50
print("x>y") if x > y else print("x < y") # agar x > y dan katta bo'lsa "x>y" aks holda "x > y"
 


--------------------------------

H O M E W O R K


# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, 
# ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. 
# GM uchun ikkala harfni katta qiling.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

for car in cars:
	if car == 'gm':
		print(car.upper())
	else:
		print(car.title())


# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
for car in cars:
	if car != 'gm':
		print(car.title())
	else:
		print(car.upper())


# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, 
# "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" 
# xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
f_ismi = input('Loginni kiriting: ')
if f_ismi.lower() == 'admin':
	print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
	print(f"Xush kelibsiz, {f_ismi.title()}!")


# Foydalanuvchidan 2 ta son kiritishni so'rang. 
# Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
son1 = int(input('1-sonni kiriting: '))
son2 = int(input('2-sonni kiriting: '))
if son1 == son2:
	print("Sonlar teng")
yoki...
if son1 == son2: print(f"Sonlar teng {son1}={son2}")


# Foydalanuvchidan istalgan son kiritishni so'rang. 
# Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
son = int(input('sonni kiriting: '))
print('bu manfiy son') if son < 0 else print('bu musbat son')
yoki...
if son < 0:
	print('bu manfiy son')
else:
	print('bu musbat son')


# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. 
# Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
import math
ildiz = float(input('Sonni kiriting: '))
if ildiz > 0:
	raqam = math.sqrt(ildiz)
	print(raqam)
else:
	print('Musbat son kiriting')

# yoki...
print(ildiz**(1/2)) if ildiz > 0 else print('Musbat son kiriting')



