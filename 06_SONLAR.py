a = 20 # sonlar musbat yoki
b = -30 # manfiy bo'lishi mumkin
c = a + b
print(c)

Kvadratning yuzini hisoblaymiz
kvdt_tmni = 20 # kvadratning tomoni
kvdt_yuzi = kvdt_tmni ** 2 # kvadrat yuzini hisoblaymiz
print(kvdt_yuzi)

pi = 3.14159 # o'nlik son (float)
radius = 10 # butun son (integer)
diametr = 2*radius
print("Aylana uzunligi ", pi*diametr, "ga teng.")

a = 2
b = 3.0
print(a+b)
print(a*b)
print(a**b)
print(2*(a+b))



aholi_soni = 7_594_000_000
print("Yer kurrasida", aholi_soni, "yashaydi")

PI = 3.14159
radius = 21.2

x, y, z = 10, -7.25, -30

ism = 'Jobir'
yosh = 36
xabar = ism + ' ' + str(yosh) + ' ' + 'yoshda'
print(xabar)

#1 foydalanuvchining tug'ilgan yilini so'raymiz va qiymatni int ga aylantiramiz
t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
#2 foydalanuvchi yoshini xisoblaymiz
yosh = 2021 - t_yil
#3 foydalanuvchi yoshini konsolga chiqaramiz
print("Siz" + ' ' + str(yosh) + ' ' + "yoshda ekansiz")



HOME WORK
son_kiriting = int(input("Istalgan sonni kiriting: "))
kvadrat = son_kiriting ** 2
print(str(son_kiriting) + ' ' + 'ning kvadrati' + ' ' + str(kvadrat) + ' ' + 'ga teng')

yoshingiz = int(input("Yoshingiz nechchida? "))
t_yil = 2021 - yoshingiz
print("Siz" + str(t_yil) + "da tug'ilgansiz")


a = float(input("1-sonni kiriting: "))
b = float(input("2-sonni kiriting: "))

print("a + b =", a+b)
print("a * b =", a*b)
print("a / b =", a/b)
print("a - b =", a-b)