# FUNKSIYAGA RO'YXAT UZATISH
def bahola(ismlar):
	baholar = {}
	while ismlar:
		ism = ismlar.pop()
		baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
		baholar[ism] = baho # ism bu lug'atni kaliti
	return baholar
talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar) 
print(baholar)
print(talabalar)# natija [] 

# ASL RO'YXATGA O'ZGARTIRISH KIRITISHNING OLDINI OLISH 
talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar[:])
print(baholar)
print(talabalar)#Natija ['ali', 'vali', 'hasan', 'husan']
