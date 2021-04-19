# 09 FOR TAKRORLASH OPERATORI
mehmonlar = ['Ali', 'Vali', 'Xasan', 'Husan', 'Olim']

for mehmon in mehmonlar:
	print(mehmon)

for mehmon in mehmonlar:
	print(f"Salom {mehmon}, sizni 20 dekabr kuni nahorgi oshga taklif qilamiz!")
	print("Hurmat bilan, Falonchiyevlar oilasi")

# for YORDAMIDA SONLI RO'YXATLAR BILAN ISHLASH
sonlar = list(range(1,11))
for son in sonlar:
	print(f"{son} ning kvadrati {son**2} ga teng")

dostlar = []
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5):
	dostlar.append(input(f"{n+1}-eng yaqin do'stingizni kiriting: "))
print(dostlar)

# ----------------------------------
# HOMEWORK

# # Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# # Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni 
# # chiqaring (n o'rniga kod necha marta takrorlanganini yozing)

friends = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
for name in friends:
	print(f"Assalom alaykum, {name}. Sahifamizga xush kelibsiz!")
print(f"Kod {len(friends)} marta takrorlandi")

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
toq_sonlar = list(range(11, 100, 2))
for son in toq_sonlar:
	print(son**3)

# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. 
# Natijani konsolga chiqaring.
kinolar = []
print("5 ta eng sevimli kinolaringiz qaysilar? ")
for k in range(5):
	kinolar.append(input(f"{k+1}-kino: "))
print(kinolar)

# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan 
# odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.

javob = int(input("Bugun necha kishi bilan uchrashdingiz? "))
odamlar = []
for n in range(javob):
	odamlar.append(input(f"{n+1}-uchrashgan odamingiz kim edi?"))
print(odamlar)
