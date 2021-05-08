# 18 WHILE, RO'YXATLAR VA LUG'ATLAR
ismlar = []
print("Yaqin do'stlaringizni ro'yxatini tuzamiz.")
n = 1 # ismlarni sanash uchun o'zgaruvchi
while True:
	savol = f"{n}-do'stingiz ismini kiriting: "
	ism = input(savol)
	ismlar.append(ism)
	javob = input("Yana ism qo'shasizmi? ha/yo'q: ")
	if javob == 'ha':
		n+=1
		continue
	else:
		break
print("Do'stlaringiz ro'yxati: ")
for ism in ismlar:
	print(ism.title())

# WHILE YORDAMIDA LUG'ATNI TO'LDIRISH
print("Do'stlaringizni yoshini saqlaymiz.")
dostlar = {}
ishora = True
while ishora:
	ism = input("Do'stingizni ismini kiriting: ")
	yosh = input(f"{ism.title()}ning yoshini kiriting: ")
	dostlar[ism] = int(yosh) # ism kalit, yosh qiymat

	javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q) ")
	if javob == "yo'q":
		ishora = False

for ism,yosh in dostlar.items():
	print(f"{ism.title()} {yosh} da")

# RO'YXAT ELEMENTLARINI O'CHIRISH
cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
	cars.remove('nexia') # nexia ni ro'yxatdan olib tashla
print(cars)

# RO'YXATDAN RO'YXATGA ELEMENT KO'CHIRISH
talabalar = ['hasan', 'husan', 'olim', 'botir']
baholangan_talabalar = {}
while talabalar:
	talaba = talabalar.pop()
	baho = input(f"{talaba.title()}ning bahosini kiriting: ")
	print(f"{talaba.title()} baholandi.")
	baholangan_talabalar[talaba] = baho
print(baholangan_talabalar)
print(talabalar)
