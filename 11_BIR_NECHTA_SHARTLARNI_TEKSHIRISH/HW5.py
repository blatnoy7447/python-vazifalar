# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. 
#Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yangi, bor_mahsulotlar degan ro'yxatga,
#do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  
#Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, 
#aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.

mahsulotlar = ['grill', 'cola', 'pepsi', 'non', 'shakar', 
				'sariyog', 'sut', "go'sht", 'shirinlik', 'tovuq']
savat = []
for n in range(5):
	savat.append(input(f'Savatga {n+1} mahsulotni qushing: '))#userdan 5 ta mahsulotni ketma-ket kiritishni suraymiz,uni savatga kiritamiz
bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat: # savatdagi mahsulotlarni mahsulotga uzgaruvchi qilib
	if mahsulot in mahsulotlar:#usha mahsulot umumiy mahsulotlarda bo'lsa 
		bor_mahsulotlar.append(mahsulot)#bor_mahsulotlarga kiritamiz
	else:
		mavjud_emas.append(mahsulot)#bo'lmasa mavjud_emas ga kiritamiz
if mavjud_emas:
	print("Quyidagi mahsulotlar do'konimizda yo'q:")
	for mahsulot in mavjud_emas:#mavjud_emas dagi mahsulotlarni
		print(mahsulot)#ketma-ketlikda consolega chiqaramiz
else:# aks holda
	print("Siz so'ragan barcha mahsulotlar do'konimizda bor")#hammasi bor


