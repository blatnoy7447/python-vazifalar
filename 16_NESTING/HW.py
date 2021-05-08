# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi 
#ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, 
#va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
# shaxslar = {
# 	'abu':{
# 		'familiya':'abdulloh muhammad ibn ismoil',
# 		'tyil':810,
# 		'umr':60,
# 		'shahri':'buhoro'
# 	},
# 	'abdulla':{
# 		'familiya':'qodiriy',
# 		'tyil':1894,
# 		'umr':44,
# 		'shahri':'toshkent',
# 	},
# 	'erkin':{
# 		'familiya':'vohidov',
# 		'tyil':1936,
# 		'umr':80,
# 		'shahri':'farg\'ona'
# 	},
# 	'alisher':{
# 		'familiya':'navoiy',
# 		'tyil':1441,
# 		'umr':60,
# 		'shahri':'xirot'
# 	}
# }
# for ism,info in shaxslar.items():
# 	print(f"{ism.title()} {info['familiya'].title()} " 
# 		  f"{info['tyil']}-yilda {info['shahri'].title()}da tavallud topgan. "
# 		  f"{info['umr']}-yil umr ko'rgan.")

#yoki...
# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro'
#            }
# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent'
#            }
# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona"
#            }
# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot"
#            }
# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     tyil = shaxs['tyil']
#     vyil = shaxs['vyil']
#     tjoy = shaxs['tjoy']
#     print(f"{ism} {tyil}-yilda {tjoy}da tavallud topgan. "
#           f"{vyil-tyil} yil umr ko'rgan.")

# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. 
#For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.

# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro',
#            'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", 
#            			  "At-tarix al-kabir", "At-tarix as-sag‘ir"]
#            }
# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent',
#            'asarlar':["O'tkan kunlar","Mehrobdan Chayon",
#            			  'Obid ketmon']
#            }
# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona",
#            'asarlar':["Tong nafasi","Qo'shiqlarim sizga",
#            			  "O'zbegim","Qiziquvchan Matmusa"]
#            }
# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot",
#            'asarlar':["Xamsa","Lison ut-Tayr",
#            			  "Mahbub Al-Qulub",'Munojot']
#            }
# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
# for shaxs in shaxslar:
# 	ism = shaxs['ism']
# 	asarlar = shaxs['asarlar']
# 	print(f"\n{ism.title()}ning mashxur asarlari:")
# 	for asar in sorted(asarlar):
# 		print(asar)


# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. 
#Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'atga saqlang.  
#Natijani konsolga chiqaring.

# kinolar = {'sulton':['Hech kim', 'Ichkarida', 'Kurtlar vadisi'],
# 		   'shohruh':['Rembo', 'Terminator', 'Tezlik 5'],
# 		   'maruf':['Saodat asri', 'Umar', 'Bog\'bon'],
# 		   'husan':['Mahallada duv-duv gap','John Wick']}
# for ism,kinolar in kinolar.items():
# 	print(f"\n{ism.title()}ning sevimli kinolari: ")
# 	for kino in kinolar:
# 		print(kino)


# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar 
#haqida ma'lumotlarni lug'at ko'rinishida saqlang. 
#Har bir davlat haqida ma'lumotni konsolga chiqaring.
davlatlar = {
			 'o\'zbekiston':{
			 	'poytaxt':"toshkent",
			 	'maydon':448978,
			 	'aholisi':33_000_000,
			 	'pul birligi':"so'm"
			 },
			 'rossiya':{
			 	'poytaxt':"moskva",
			 	'maydon':17_098_246,
			 	'aholisi':144_000_000,
			 	'pul birligi':'rubl'
			 },
			 'aqsh':{
			 	'poytaxt':"vashington",
			 	'maydon':9_631_418,
			 	'aholisi':327_000_000,
			 	'pul birligi':"dollar"
			 },
			 'malayziya':{
			 	'poytaxt':'kuala-lumpur',
			 	'maydon':329750,
			 	'aholisi':25_000_000,
			 	'pul birligi':"rinngit"
			 }
		}
# for davlat,info in davlatlar.items():
# 	if davlat.lower()=='aqsh':
# 		davlat = davlat.upper()
# 	else:
# 		davlat = davlat.capitalize()
# 	print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
# 		  f"\nHududi:{info['maydon']} kv.km"
# 		  f"\nAholisi:{info['aholisi']}"
# 		  f"\nPul birligi:{info['pul birligi']}")

# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, 
#foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning 
#lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.	

davlat = input('Davlat nomini kiriting: ').lower()

if davlat in davlatlar:
	info = davlatlar[davlat]
	print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
		  f"\nHududi:{info['maydon']} kv.km"
		  f"\nAholisi:{info['aholisi']}"
		  f"\nPul birligi:{info['pul birligi']}")
else:
	print("Bizda bu davlat haqida ma'lumot yo'q")
