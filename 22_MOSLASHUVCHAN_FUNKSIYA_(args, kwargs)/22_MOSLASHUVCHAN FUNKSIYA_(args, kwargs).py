# *args USULI
def summa(*sonlar):
	"""Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
	yigindi = 0
	for son in sonlar:
		yigindi += son # yigindi = yigindi + son
	return yigindi
print(summa(1,2,3,4,5))

# #yuqoridagi funksiyamizni yanada soddalashtirib yozishimiz mumkin:
def summa(*sonlar):
	"""Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
	return sum(sonlar)
print(summa(1,2,3,4,5))

#Agar funksiya bir nechta argument qabul qilsa, *args argument doim oxirida yoziladi:
def summa(x,y,*sonlar):
	"""Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
	return x+y+sum(sonlar)
print(summa(2,3)) # kamida 2 ta parametr qabul qiladi


# **kwargs USULI
def avto_info(kompaniya,model,**malumotlar):
	"""Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
	malumotlar['kompaniya'] = kompaniya
	malumotlar['model'] = model
	return malumotlar

avto1 = avto_info("GM", "Malibu", rangi='qora', yil=2018)
avto2 = avto_info("Kia", "K5", rangi='oq', narhi=29000, korobka='avtomat')
print(avto1)
print(avto2)
