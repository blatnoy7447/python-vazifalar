# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. 
#Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. 
#Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa 
#"Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

mahsulotlar = ['grill', 
				'cola', 
				'pepsi', 
				'non', 
				'shakar', 
				'sariyog', 
				'sut', 
				"go'sht", 
				'shirinlik', 
				'tovuq']
savat = []

for n in range(5):
	savat.append(input(f'Savatga {n+1}-mahsulotni qushing: '))

for mahsulot in savat: # savatdagi mahsulotni olamiz
	if mahsulot in mahsulotlar: # usha mahsulot mahsulotlarda bo'lsa
		print(f"Do'konimizda {mahsulot} bor")
	else: # bo'lmasa 
		print(f"Do'konimizda {mahsulot} yo'q")








