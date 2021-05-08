# YANA input()
ism = input('Ismingiz nima? ')
savol = f'Assalom aleykum, {ism.title()}jon aka. Yoshingiz nechchida? '
yosh = int(input(savol))
if yosh>25:
	print('qarib qobsiz((')


# Sonlar va input()
ism = input('Ismingiz nima? ')
savol = f"Assalom aleykum, {ism.title()}jon aka. Yoshingiz nechchida? "
yosh = input(savol)
yosh = int(yosh) # yosh ni butun songa o'tkazamiz
height = input("Bo'yingiz necha metr? ")
height = float(height)# bo'yni o'nlik songa o'tkazamiz


# while TSIKLI BILAN TANISHAMIZ
son = 1 # son ga 1 qiymatini beramiz
while son<=5:# toki son 5 dan kichik yoki teng ekan...
	print(son, end=' ')# son ni konsolga chiqaramiz,
	son = son + 1 # yoki s+=1 deyishimiz ham mumkin!!!
 

# while va input()
print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan sonni kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
qiymat = ''
while qiymat != 'exit':
	qiymat = input(savol)
	if qiymat != 'exit':
		print(float(qiymat)**2) 


# Ishora (flag)
print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
ishora = True
while ishora:
	qiymat = input(savol)
	if qiymat == 'stop':
		ishora = False
	else:
		print(float(qiymat)**2)


# BREAK OPERATORI
print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
while True: # abadiy tsikl
    qiymat = input(savol)
    if qiymat == 'exit':
        break # tsiklni to'xtatish
    else:
        print(float(qiymat)**2)

sonlar = list(range(1,11))
for son in sonlar:
	if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
		break
	else:
		print(f"{son} ning kvadrati {son**2} ga teng")
	

# CONTINUE OPERATORI
sonlar = list(range(1,11))
for son in sonlar:
	if son == 5: # agar son 5 ga teng bo'lsa uni o'tkazib keyingisi davom etadi
		continue
	else:
		print(f"{son} ning kvadrati {son**2} ga teng")
	
son = 0
while son<10:
	son += 1 # 0 ga 1 ni qo'shib toki 10 bo'lmagunigacha
	if son%2 != 0: # juft bo'lmagan sonlarni, 
		continue # tashab ketamiz
	else:
		print(son)


# ABADIY TSIKL TUZOG'I

infinite loop
son = 0
while son<10:
    if son%2!=0:
        continue
    else:
        print(son) # bu kod abadiy,sababi biz sonning qiymatini o'zgartirishni esdan chiqardik(son+=1)

son = 0
while son<10:
    if son%2!=0:
        continue
    else:
        print(son)
    son += 1 # Bu kod ham abadiy davom etadi, lekin nima uchun?

son = 0
while son<10:
	son += 1
	if son%2!=0:
		continue
	else:
		print(son)# Yuqoridagi kodda esa xato shart tufayli (son>0) kod abadiy aylanadi.

