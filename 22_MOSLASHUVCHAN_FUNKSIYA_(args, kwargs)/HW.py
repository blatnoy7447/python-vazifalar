# Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
def kupaytir(*args):
	kupaytma = 1
	for son in args:
		kupaytma *= son # yigindi = yigindi*son
	return kupaytma
print(kupaytir(1,2,3,4,5))


# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funksiya yozing. 
#Talabaning ismi va familiyasi majburiy argument, 
#qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.
def talaba_info(ism, familiya, **malumotlar):
	malumotlar['ism'] = ism
	malumotlar['familiya'] = familiya
	return malumotlar
talaba1 = talaba_info('Maruf', 'Yuldashev', yil=1990, kasb='Python developer')
talaba2 = talaba_info('Sultonqul', 'Nortoylokov', yil=2000, kasb='React developer')
talaba3 = talaba_info('Shohruh', 'Muhtorjonov', yil=1996, kasb='NodeJS developer')
print(talaba1)
print(talaba2)
print(talaba3)



