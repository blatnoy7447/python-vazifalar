# PYTHON MODULLARI

#math MODULI
#  sqrt() - qavs ichida berilgan qiymatning kvadrat ildizini qaytaradi
# import math
# x=400
# print(math.sqrt(x)) # Natija: 20.0


#  pow(x,y) - x ning y-darajasini qaytaradi
# print(pow(4,4))


#  pi - ning qiymatini saqlovchi o'zgaruvchi
# from math import pi
# print(pi)


#  log2(x) va log10(x) - x ning 2 va 10-lik logorifmini qaytaruvchi funksiyalar
# print(math.log2(8))
# print(math.log10(10))



#random MODULI
#  randint(a,b) Bu funksiya a va b oraligi'da tasodifiy butun son qaytaradi. 
import random as r # random modulini r deb chaqirayapmiz
# son = r.randint(0,1500000) # 0 va 100 oralig'ida tasodifiy son
# print(son)

 
#  choice(x)  x ning ichidan tasodifiy qiymatni qaytaruvchi funksiya.
# ismlar = ['olim','anvar','hasan','husan']
# ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
# print(ism)
# print(r.choice(ism))


# x = list(range(0,51,5))
# print(x)
# print(r.choice(x))


#  shuffle(x)  x ichidagi elementlarni tasodifiy tartibda qaytaruvchi funksiya
x = list(range(11))
print(x)
r.shuffle(x)
print(x)

  

