# 11 BIR NECHTA SHARTLARNI TEKSHIRISH
# if-elif-else zanjiri, "and", "or" operatorlari bilan tanishamiz

yosh = int(input('Yoshingiz nechchida? '))
if yosh <= 4:
	print("Sizga kirish bepul")
elif yosh <= 12:
	print("Sizga kirish 5000 so'm")
else:
	print("Sizga kirish 10000 so'm")

# Kod yozishda yaxshi amaliyotlardan biri, kodlarni qisqa yozish va buyruqlarni qayta-qayta takrorlamaslik. 
# Bu kelajakda kodni o'zgartirishda ham juda qo'l keladi. 
yosh = int(input('Yoshingiz nechchida? '))
if yosh <= 4:
	price = 0
elif yosh <= 12:
	price = 5000
else:
	price = 10000
print(f"Sizga kirish {price} so'm")


yosh = int(input('Yoshingiz nechchida? '))
if yosh <= 4: # yosh bolalarga bepul
	price = 0
elif yosh <= 12: # 4 dan 12 yoshgacha 5000 so'm
	price = 5000
elif yosh < 65: # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
	price = 10000
else: # qariyalarga esa 8000 so'm
	price = 8000
print(f"Sizga kirish {price} so'm")

# if-elif-else zanjirida ham else qismi majburiy emas:
yosh = int(input('Yoshingiz nechchida? '))
if yosh <= 4: # yosh bolalarga bepul
	price = 0
elif yosh <= 12: # 4 dan 12 yoshgacha 5000 so'm
	price = 5000
elif yosh < 65: # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
	price = 10000
elif yosh >= 65:
	price = 8000
print(f"Sizga kirish {price} so'm")


kun = input('Bugun nima kun?\n>>>')
if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
	print('Bugun dam olish kuni.')
else:
	print('Bugun ish kuni.')

kun = input('Bugun nima kun? ')
havo = int(input('Havo harorati qanday? '))
if kun.lower() == 'yakshanba' and havo >= 30:
	print('Ketdik chumilgani')
elif kun.lower() == 'yakshanba' and havo < 30:
	print("Uyda dam olamiz")

kun = input('Bugun nima kun? ')
havo = int(input('Havo harorati qanday? '))
if (kun.lower()=='shanba' and kun.lower()=='yakshanba') or havo>=30:
	print('Chumilgani ketdik')
elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') or havo < 30:
	print('Uyda dam olamiz')

narh = 15000 # mijoz 15000 so'mga taom oldi.
choy = True # mijoz choy ham oldi
salat = False # mijoz salat olmadi
if choy and salat: # agar mijoz choy ham va salat ham olgan bo'lsa
	narh = narh + 10000 # narhga 10000 so'm qo'shamiz
elif choy or salat: # agar choy yoki salat olgan bo'lsa
	narh = narh + 5000 # narhga 5000 so'm qo'shamiz
print(f"Jami {narh} so'm") # yakuniy narhni chiqaramiz


narh = 15000 # mijoz 15000 so'mga ovqat oldi
choy = True
salat = False
non = True
kompot = True
assorti = False
#Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
if choy: # agar choy olsa
	print('Mijoz choy oldi')
	narh = narh + 3000
if salat: # agar salat olsa
	print('Mijoz salat oldi')
	narh = narh + 5000
if non: # agar non olsa
	print('Mijoz non oldi')
	narh = narh + 2000
if kompot: # agar kompot olsa
	print('Mijoz kompot oldi')
	narh = narh + 5000
if assorti: # agar assorti olsa
	print('Mijoz assorti oldi')
	narh = narh + 15000
print(f'Jami {narh} sum')


menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
'manti' in menu # menu da manti bormi?
#Natija: False

menu = ['osh','qazonkabob','shashlik','norin','somsa']
'osh' in menu # menu da osh bormi?
#Natija: True

menu = ['osh','qozonkabob','shashlik','norin','somsa']
ovqat = input("Nima ovqat yeysiz?\n>>>")
if ovqat.lower() not in menu:
	print("Afsuski biz bunday ovqat yo'q.")
else:
	print("Buyurtmangiz qabul qilindi")


menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh", "somsa", "manti", "shashlik"]

for taom in buyurtmalar:
	if taom in menu:
		print(f'Menuda {taom} bor')
	else:
		print(f"Kechirasiz, menuda {taom} yo'q")


menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]
if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
	for taom in buyurtmalar:
		if taom in menu:
			print(f'Menuda {taom} bor')
		else:
			print(f'Kechirasiz, menuda {taom} yuq')
else: # agar ro'yxat bo'sh bo'lsa
	print("Savatchangiz bo'sh")










       








