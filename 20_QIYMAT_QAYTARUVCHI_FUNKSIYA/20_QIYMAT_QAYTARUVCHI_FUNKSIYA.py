#FUNKSIYADAN ODDIY QIYMAT QAYTARISH
def toliq_ism_yasa(ism, familiya):
	"""To'liq ism qaytaruvchi funksiya"""
	toliq_ism = f"{ism} {familiya}"
	return toliq_ism # qiymat qaytarish uchun return operatorini ishlatamiz
talaba1 = toliq_ism_yasa('olim', 'hakimov')
talaba2 = toliq_ism_yasa('hakim', 'olimov')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")




# IXTIYORIY ARGUMENTLAR
def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
	"""To'liq ism qaytaruvchi funksiya"""
	if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
		toliq_ism = f"{ism} {otasining_ismi} {familiya}"
	else:
		toliq_ism = f"{ism} {familiya}"
	return toliq_ism.title()

talaba1 = toliq_ism_yasa('olim', 'hakimov')
talaba2 = toliq_ism_yasa('hakim', 'olimov', 'abrorovich')
print(f"Darsga kelmagan talabalar: {talaba1} {talaba2}")




# FUNKSIYADAN LUG'AT QAYTARAMIZ
def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
	avto = {
		'kompaniya':kompaniya,
		'model':model,
		'rang':rangi,
		'korobka':korobka,
		'yil':yili,
		'narh':narhi
	}
	return avto
avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
avtolar = [avto1, avto2]
print("Onlayn bozordagi avtomashinalar: ")
for avto in avtolar:
	if avto['narh']: # agar mashinani narhi mavjud bo'lsa 
		narh = avto['narh'] # o'zgaruvchiga qiymat beramiz
	else: # aks holda
		narh = "Noma'lum" 
	print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")
# FUNKSIYALARNI TSIKLDA ISHLATISH
#Quyidagi misolda biz while yordamida avvalroq yaratgan avto_info 
#funksiyamizni bir necha bor chaqiramiz va salondagi avtolar ro'yxatini shakllantiramiz
print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar = []
while True:
	print("Quyidagi ma'lumotlarni kiriting:\n", end='')
	kompaniya = input("Ishlab chiqaruvchi: ")
	model = input("Modeli: ")
	rangi = input("Rangi: ")
	korobka = input("Korobka: ")
	yili = input("Ishlab chiqarilgan yili: ")
	narhi = input("Narhi: ")
	avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    # Yana avto qo'shish-qo'shmaslikni so'raymiz
	javob = input("Yana avto qo'shasizmi? (yes/no): ")

	if javob=='no':
		break
print(avtolar)



# FUNKSIYADAN RO'YXAT QAYTARAMIZ
def oraliq(min, max):
	sonlar = [] # bo'sh ro'yxat
	while min<max:
		sonlar.append(min)
		min += 1
	return sonlar

print(oraliq(0,10))
print(oraliq(0,20))








