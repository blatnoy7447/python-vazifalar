# # lambda YOHUD NOMSIZ FUNKSIYA
# # Nomsiz funksiyalar quyidagicha yaratiladi:
# #   lambda argument:ifoda
# import math
# uzunlik = lambda pi, r : 2*pi*r
# print(uzunlik(math.pi, 10))


# product = lambda x, y : x ** y
# print(product(2, 3))


# def daraja(n):
# 	return lambda x : x**n

# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3-ning kvadrati {kvadrat(3)}, kubi {kub(3)} ga teng")


# map() FUNKSIYASI
# from math import sqrt

# sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
# ildizlar = list(map(sqrt, sonlar))
# print(ildizlar)


# sonlar = list(range(11))
# def daraja2(x):
# 	"""Berilgan sonning kvadratini qaytaruvchi funksiya"""
# 	return x*x
	
# print(list(map(daraja2, sonlar))) # sonlar ning kvadratini hisoblaymiz
# # Endi keling huddi shu misolni lambda yordamida yozamiz:
# kvadratlar = list(map(lambda x : x*x, sonlar))
# print(kvadratlar)
# # map() funksiyasi bo'lmaganida biz bunday dasturlarni for yordamida yozishimiz kerak bo'lar edi:
# kvadratlar = []
# for son in sonlar:
# 	kvadratlar.append(son*son)

# # map() funksiyasiga bir nechta ro'yxatlar ham uzatish mumkin:
# a = [4, 5, 6]
# b = [7, 8, 9]
# a_plus_b = list(map(lambda x,y : x+y, a,b))
# print(a_plus_b)
# # map() istalgan ko'rinishdagi ma'lumot turlari bilan ishlaydi:
# ismlar = ['hasan', 'husan', 'olim', 'umid']
# print(list(map(lambda matn : matn.upper(), ismlar)))


# filter() FUNKSIYASI
# import random as r

# sonlar = r.sample(range(100), 10)

# def juftmi(x):
# 	"""x juft bo'lsa True, aks holda False qaytaruvchi funksiya"""
# 	return x%2==0

# juft_sonlar = list(filter(juftmi, sonlar))
# print(sonlar)
# print(juft_sonlar)
# # Keling endi shu dasturni lambda yordamida yozamiz:
# import random as r

# sonlar = r.sample(range(100), 10)
# juft_sonlar = list(filter(lambda son : son%2==0, sonlar))
# print(sonlar)
# print(juft_sonlar)

# mevalar = ['olma', 'anor', 'anjir', 'shaftoli', "o'rik", "tarvuz", "qovun", "banan"]
# mevalar_b = list(filter(lambda meva : meva.startswith('b'), mevalar))
# print(mevalar_b)

# mevalar2 = list(filter(lambda meva : len(meva) <= 5, mevalar))
# print(mevalar2)

# mevalar3 = list(filter(lambda meva : (meva.startswith('a') and meva.endswith('r')), mevalar))
# print(mevalar3)


