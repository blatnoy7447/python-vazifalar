def oraliq(min,max):
    sonlar = [] # bo'sh ro'yxat
    while min<max:
        sonlar.append(min)
        min += 1
    return sonlar	
print(oraliq(0,10))
print(oraliq(10,21))

# Yuqoridagi funksiyaga uchinchi, qadam deb nomlangan ixtiyoriy parameterni qo'sha olasizmi?
def oraliq(min, max, qadam=1):
	sonlar = []
	while min<max:
		sonlar.append(min)
		min += qadam
	return sonlar
print(oraliq(0,100,5))


# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini 
#qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. 
#Lug'atda foydalanuvchining yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling 
#(masalan, tel.raqam, el.manzil)
def mijoz_info(ism, familiya, yil, tjoy, mail='', tel=''):
	"""Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
	mijoz = {
		'ism':ism,
		'familiya':familiya,
		'yoshi':2021-yil,
		'Manzil':tjoy,
		'pochtasi':mail,
		'raqami':tel
	}
	return mijoz
print("Mijoz haqidagi ma'lumotlarni kiriting: ")
mijozlar = []
while True:
	ism = input("Ismingiz: ")
	familiya = input("Familiyangiz: ")
	yil = int(input("Tug'ilgan yilingiz: "))
	tjoy = input("Yashash manzilingiz: ")
	mail = input("Pochta: ")
	tel = input("Telefon raqamingiz: ")
	mijozlar.append(mijoz_info(ism, familiya, yil, tjoy, mail, tel))
	javob = input("Davom etasizmi? (ha/yo'q): ")
	if javob!='ha':
		break

print("Mijozlar: ")
for mijoz in mijozlar:
	print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}, " 
          f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['raqami']}")


# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
def kattasi(x,y,z):
	if x<y:
		javob = y
	elif x<z:
		javob = z
	elif z<x:
		javob = x
	else:
		javob = y
	return javob
c = kattasi(40,20,50)
print(c)
#yoki....
def kattasi(x,y,z):
    max = x
    if y>=max:
        max = y
    if z>=max:
        max = z
    return max
c = kattasi(40, 50, 30)
print(c)


# Foydalanuvchidan aylananing radiusini qabul qilib olib, uning radiusini, 
#diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing.
def aylana_info(radius,pi=3.14):
	aylana = {
		'radius':radius, # aylananing o'rta nuqtasidan yon chizig'igacha masofa radius deyiladi
		'diametr':2*radius, # aylananing u yonidan bu yonigacha masofa diametr(ya'ni radius*2)
		'perimetr':2*radius*pi, 
		'yuza':pi*radius**2
	}
	return aylana
s = aylana_info(28)
print(s)


# Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing 
#(tub sonlar — faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
def tub_sonlar_top(min,max):
	tub_sonlar = []
	for n in range(min, max+1):
		tub = True
		if (n==1):
			tub = False
		elif (n==2):
			tub = True
		else:
			for x in range(2,n):
				if(n%x==0):
					tub = False
		if tub:
			tub_sonlar.append(n)
	return tub_sonlar
r = tub_sonlar_top(0,35)
print(r)


# Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi 
#sonlar ro'yxatni qaytaruvchi funksiya yozing.  Ta’rif: Har bir hadi o’zidan oldingi 
#ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. 
#Bunda boshlang’ish had ko’pincha 1 deb olinadi.  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
def fibonacci(n):
	sonlar = []
	for x in range(n):
		if x==0 or x==1:
			sonlar.append(1)
		else:
			sonlar.append(sonlar[x-1]+sonlar[x-2])
	return sonlar
print(fibonacci(5))





