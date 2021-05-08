# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. 
#Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo 
#ketma-ketligida chiroyli qilib konsolga chiqaring. 

python = {
	'integer':'butun son',
	'float':"o'nlik son",
	'string':'matn',
	'if':'shartlarni tekshirish operatori',
	'else':'aks holda sharti',
	'dictionary':"lug'at",
	'for':'biror amalni qayta qayta bajarish tsikli',
	'boolean':'mantiqiy qiymat',
	'variable':"o'zgaruvchi",
	'list':"ro'yhat"
}
for key,value in sorted(python.items()):
	print(f"{key.title()} - {value}")

#------------

# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, 
#keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 

davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'
}

print("Dunyo davlatlari:")
for davlat in sorted(davlatlar):
	print(davlat.upper())

# print("Davlatlarning poytaxtlari")
# for poytaxt in sorted(davlatlar.values()):
# 	print(poytaxt.title())

country = input('Qaysi davlatning poytaxtini bilishni xohlaysiz? ').lower()
capital = davlatlar.get(country)
if capital==None:
	print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
else:
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")

#-------------------

# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). 
# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. 
#Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, 
#agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
menu = {
	'KFC':20500,
	'palov':20000,
	'lag\'mon':17000,
	'tovuqsay':27000,
	'sho\'rva':17000,
	'norin':17000,
	'jiz-biz':35000,
	'somsa':5000,
	'kabob':10000,
	'steyk':13000,
	'non':4000
}
print("3 ta taom buyurtma bering.")
buyurtmalar = []
for i in range(3):
	buyurtmalar.append(input(f"{i+1}-taom: ").lower())
for buyurtma in buyurtmalar:	
	if buyurtma in menu:
		print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
	else:
		print(f'Kechirasiz, bizda {buyurtma} yo\'q.')






