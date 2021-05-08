# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. 
#Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

print("Mahsulotlarni kiritamiz: ")
buyurtma = []
n=1
while True:
	savol = f"{n}-mahsulotni kiriting:"
	savol += "(to'xtatish uchun 'exit' yozing): "
	qiymat = input(savol)
	mahsulot = buyurtma.append(qiymat)
	if qiymat == 'exit':
		break
	else:
		n+=1
		continue
print(f"{buyurtma}")

#yoki...
savat = []
while True:
	mahsulot = input("Savatga mahsulot qo'shing: ")
	savat.append(mahsulot)
	javob = input("Yana qo'shasizmi? (ha/yo'q): ")
	if javob != 'ha':
		break
print(f"{savat}")


# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. 
#Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
mahsulotlar = {}
while True:
	mahsulot = input("Mahsulotni kiriting: ")
	narh = input(f"{mahsulot.title()}ning narhini kiriting: ")
	mahsulotlar[mahsulot] = narh
	javob = input("Yana mahsulot qo'shasizmi?(ha/yo'q): ")
	if javob != "ha":
		break
print(mahsulotlar)


# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi 
#mahsulotlar bilan solishtiring (tayyor ro'yxat ishlatishingiz mumkin). 
#Agar mahsulot e-bozorda mavjud bo'lsa mahsulot narhini chiqaring, 
#aks holda "Bizda bu mahsulot yo'q" degan xabarni ko'rsating.
buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}
while buyurtmalar:
	buyurtma = buyurtmalar.pop() # buyurtmalarni sug'urib olib
	if buyurtma in mahsulotlar.keys(): # usha buyurtmalar mahsulotlarni(kalitlari bilan solishtirish) ichida bo'lsa
		narh = mahsulotlar[buyurtma] # usha mahsulotlarni kaliti(ya'ni mahsulotlar['olma'] bu 20000 degani)
		print(f"{buyurtma.title()} - {narh} so'm")
	else:
		print(f"Bizda {buyurtma} yo'q")


