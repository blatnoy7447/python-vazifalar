# .items() METODI
talaba_0 = {
    'ism':'alijon',
    'familiya':'shamshiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
    }



for kalit, qiymat in talaba_0.items():
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat} \n")

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }

for k, q in telefonlar.items():
	print(f"{k.title()}ning telefoni {q}")


# .keys() METODI
mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }
print(mahsulotlar.keys())

print("Do'kondagi mahsulotlar:")
for mahsulotlar in mahsulotlar.keys():#for tsiklida .keys() metodini ishlatmasak ham huddi shu natija chiqadi.
	print(mahsulotlar.title())

bozorlik = ['anor','uzum','non','baliq']
for mahsulot in mahsulotlar:
	if mahsulot in bozorlik:
		print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

for buyum in bozorlik:
	if buyum not in mahsulotlar:
		print(f"Iltimos {buyum} ham olib keling.")

# LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH
print("Do'konimizdagi mahsulotlar")
for mahsulot in sorted(mahsulotlar):
	print(mahsulot.title())


# .values() METODI
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
	print(tel)

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }
print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
	print(tel)
print('-----')
for tel in set(telefonlar.values()):
	print(tel)

