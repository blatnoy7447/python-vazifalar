# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
def ism_yosh_hisobla(ism, tugilgan_yil, joriy_yil=2021):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"{ism.title()} siz {joriy_yil-tugilgan_yil} yoshda ekansiz.")
tyil = int(input("Tug'ilgan yilingizni kiriting: "))
ism = input("Ismingiz nima? ")
ism_yosh_hisobla(ism, tyil)


# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
def kv_kub(son):
	"""Sonning kvadrati va kubini hisoblovchi dastur"""
	print(f"{son} ning kvadrati {son**2} ga teng.\n"
		  f"{son} ning kubi {son**3} ga teng.")
son = int(input("Istalgan sonni kiriting: "))
kv_kub(son)	

# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
def juftmi(son):
	"""Sonning juft yoki toqligini chiqaruvchi dastur"""
	if son%2==0:
		print(f"{son} - juft son")
	else:
		print(f"{son} - toq son")
son = float(input("Istalgan sonni kiriting: "))
juftmi(son)

print(juftmi)


# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. 
#Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
def solishtir(son1, son2):
	"""Ikki sonni solishtiruvchi funksiya"""
	if x>y:
		print(f"{x}>{y}")
	elif x<y:
		print(f"{x}<{y}")
	else:
		print(f"{x}={y}")
x = float(input("1-sonni kiriting: "))
y = float(input("2-sonni kiriting: "))
solishtir(x, y) 
#yoki...
def solishtir(x,y):
    """Ikki sonni solishtiruvchi funksiya"""
    if x>y:
        print(f"{x}>{y}")
    elif x<y:
        print(f"{y}>{x}")
    else:
        print(f"{x}={y}")

solishtir(10,20)
solishtir(-9,12)
solishtir(1223*5,5**4)

# Foydalanuvchidan x va y sonlarini olib, x ning darajasini konsolga chiqaruvchi funksiya yozing.
def daraja(x, y):
	print(f"{x} ning {y}-darajasi {x**y} ga teng.")
daraja(5,2)
daraja(3,3)
daraja(94,4)
daraja(6,3)


# Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
def daraja(x, y=2):
	print(f"{x} ning darajasi {x**y} ga teng.")
daraja(5)
daraja(3)
daraja(94)
daraja(6)


# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz 
#bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
def bolinish_alomatlari(x):
	for i in range(2,11):
		if not x%i:
			print(f"{x} {i} ga qoldiqsiz bo'linadi")
x = int(input("sonni kiriting: "))
bolinish_alomatlari(x)
# yoki....
def bolinish_alomatlari(son):
	for n in range(2,11):
		if not son%n:
			print(f"{son} {n} ga qoldiqsiz bo'linadi")

bolinish_alomatlari(21)



