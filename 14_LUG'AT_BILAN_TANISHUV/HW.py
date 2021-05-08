# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson 
#haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). 
#Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :
#    Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan

otam = {'ismi':'fahriddin', 'yosh':54, 't_yil':1967, 'shahri':'Qarshi'}
onam = {'ismi':'nargiza', 'yosh':50, 'shahri':'Qarshi', 'manzil':'Roguzar'}
ukam = {'ismi':'mahmud', 'yosh':26, 'shahri':'Qarshi'}
print(f"Otamning ismi {otam['ismi'].title()}, {otam['t_yil']}-yilda {otam['shahri']}da tug'ilgan")
print(f"Onamning ismi {onam['ismi'].title()}, yoshi {onam['yosh']} da, {onam['manzil']} mahallasida yashaydi")
print(f"Ukam {ukam['ismi'].title()}, {ukam['shahri']}da tug'ilgan, yoshi {ukam['yosh']} da")


# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom juftligi bo'lsin. 
#Kamida uch kishining sevimli taomini konsolga chiqaring: --> Alining sevimli taomi osh

taomlar = {
	'onam':'chechevitsa', 
	'mahmud':'palov', 
	'mumam':"go'sht", 
	'Manzura xolam':'manti', 
	'Bohodir':'mastava'
}
print(f"Onamning sevimli taomi {taomlar['onam'].title()},\
 Mahmudning sevimli taomi {taomlar['mahmud']},\
 xolamning sevimli taomi {taomlar['Manzura xolam']}.")


# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z 
#(atamani) kiriting (masalan integer, float, string, if, else va hokazo) va 
#har birining qisqacha tarjimasini yozing.

python = {
	'integer':'butun son',
	'float':"o'nlik son",
	'string':'matn',
	'if':'agar sharti',
	'else':'aks holda sharti',
	'dictionary':"lug'at",
	'for':'uchun tsikli',
	'in':'ichida',
	'variable':"o'zgaruvchi",
	'list':"ro'yhat"
}

# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi 
#lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunday so'z mavjud emas" 
#degan xabarni chiqaring.
kalit = input("Kalit so'zni kiriting: ").lower()
print(python.get(kalit, "Bunday so'z mavjud emas"))

# Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli 
#ko'rinishda chiqaring.
if kalit in python:
	print(f"{kalit.title()} so'zi {python.get(kalit)} deb tarjima qilinadi.")
else:
	print("Bunday so'z mavjud emas")

# boshqa varianti
tarjima = python.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")






