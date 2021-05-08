# 19 FUNKSIYA
#FUNKSIYA YARATAMIZ
# def salom_ber():
# 	'''Salom beruvchi funksiya'''
# 	print("Assalomu aleykum!")

# salom_ber()


# FUNKSIYAGA QIYMAT UZATISH
# def salom_ber(ism):
# 	'''Foydalanuvchi ismini qabul qilib, unga salom beruvchi funksiya'''
# 	print(f"Assalomu alaykum, hurmatli {ism.title()}!")
# salom_ber('maruf')


# DOCSTRING
# print(salom_ber.__doc__) # docstringni konsolga chiqarish uchun print(funksiya_nomi.__doc__) deb yozamiz


# FUNKSIYAGA BIR NECHA BOR MUROJAT QILISH
# def salom_ber(ism):
# 	'''Foydalanuvchi ismini qabul qilib, unga salom beruvchi funksiya'''
# 	print(f"Assalomu alaykum, hurmatli {ism.title()}!")
# salom_ber('maruf')
# salom_ber('xasan')
# salom_ber('mahmud')


# ARGUMENT VA PARAMETER
	#Yuqoridagi misolda ism bu salom_ber funksiyasining parametri
	#salom_ber('hasan') kodida 'hasan' bu argument


# FUNKSIYAGA BIR NECHTA ARGUMENT UZATISH

# def toliq_ism(ism, familiya):
# 	"""Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
# 	print(f"Foydalanuvchi ismi: {ism.title()}\n"
# 		  f"Foydalanuvchi familiyasi: {familiya.title()}")
# toliq_ism('maruf', 'yuldashev')
# toliq_ism('yuldashev', 'maruf') #Agar argumentlarni noto'g'ri ketma-ketlikda bersak, biz kutgan natija chiqmaydi

# def yosh_hisobla(ism, tugilgan_yil):
# 	"""Foydalanuvchi yoshini hisoblaydigan dastur"""
# 	print(f"{ism.title()} {2021-tugilgan_yil} yoshda")

# yosh_hisobla('maruf', 1990)
# yosh_hisobla(1990, 'maruf')#Ko'p xolatlarda esa, argumentlarni noto'g'ri tartibda uzatish xatolikka ham olib kelishi mumkin.


# KALIT SO'Z BILAN UZATISH
# yosh_hisobla(tugilgan_yil=1990, ism='maruf')
# toliq_ism(familiya='yuldashev', ism='maruf')


# STANDART QIYMAT
#standart qiymatga ega parametrlarni doim oxirida yozing.Aks holda xatolik yuzaga keladi.
# def yosh_hisobla(tugilgan_yil, joriy_yil=2021):#joriy_yil bu standart qiymat
# 	"""Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
# 	print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz.")
# yosh_hisobla(1990, 2021)
# yosh_hisobla(1990) #Endi esa faqat bitta argument (tugilgan_yil) bilan chaqiramiz


# FUNKSIYAGA MUROJAT QILISHDA XATOLIKLAR
# def yosh_hisobla(tugilgan_yil, joriy_yil=2021):
# 	"""Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
# 	print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

# tyil = input("Tug'ilgan yilingizni kiriting: ")
# yosh_hisobla(tyil)#Natija: TypeError: unsupported operand type(s) for -: 'int' and 'str'
# #------
# def yosh_hisobla(tugilgan_yil, joriy_yil):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

# yosh_hisobla(1993)#Natija: TypeError: yosh_hisobla() missing 1 required positional argument: 'joriy_yil'
# #-----
# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")
# salom_ber('hasan')#Natija: TypeError: salom_ber() takes 0 positional arguments but 1 was given
# #-----
# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
 
#  toliq_ism('olim hakimov')#Natija: TypeError: toliq_ism() missing 1 required positional argument: 'familiya'












