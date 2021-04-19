mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yhati (matnlar)
narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yhati
sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar ro'yhati
ismlar = [] # bo'sh ro'yhat

print("Birinchi meva: ", mevalar[0])
print("Ikkinchi meva: ", mevalar[1])

print("Birinchi meva: ", mevalar[0].title())
print("Ikkinchi meva: ", mevalar[1].upper())

print(narhlar[0] + narhlar[1])

car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
print(car_models[-1]) # Listning oxirgi elementiga -1 bilan murojaat qilamiz


narhlar = [12000, 18000, 10900, 22000]

narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
narhlar[2] = 15000 # 2-qiymatni 15000 ga o'zgartiramiz
narhlar[3] = narhlar[3] + 3000 # 4-qiymatga 3000 qo'shamiz

print(narhlar)

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
mevalar.append('tarvuz')
print(mevalar)


cars = []

cars.append('Lacetti')
cars.append('Nexia 3')
cars.append('Cobalt')

print(cars)

cars = ['Lacetti', 'Nexia 3', 'Cobalt']

cars.insert(0, 'Malibu') # 1-o'ringa yangi qiymat qo'shamiz
cars.insert(2, 'Damas') # 3-o'ringa yangi qiymat qo'shamiz
print(cars)

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]

del mevalar[1] # del yordamida 2-element ni o'chirib tashlaymiz
print(mevalar)


mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
mevalar.remove('shaftoli') # ro'yhatdan shaftolini o'chirdik

print(mevalar)

hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
hayvonlar.remove('mushuk') # ro'yhatda 2 ta mushuk bor, ulardan birinchisi o'chadi

print(hayvonlar)

bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3) # ro'yhatdan banan ni sug'urib olamiz

print("Men " + mahsulot + " sotib oldim")
print("Olinmagan mahsulotlar: ", bozorlik)



HOME WORK
ismlar = ['Shohruh', 'Sultonqul', 'Xasan', 'Sherali']
print('Salom' + ismlar[0] + 'bugun choyxona bormi?')
print(ismlar[1] + 'choyxonaga boramizmi?')


sonlar = [100, 270, -75, 155.2, 112_500_00, -58]

# print(sonlar[1] ** 2)
# print(sonlar[4] / 3)

sonlar[0] = sonlar[0] + sonlar[3]
del sonlar[3] 
print(sonlar)

t_shaxslar = ['Imom Buhoriy', 'AT-Termiziy', 'Zamaxshariy', 'Behbudiy']
z_shaxslar = ['Bill Gates', 'Ilon Mask', 'Tim Kuk', 'Shavkat Mirziyoyev']

print(f'Men tarixiy shaxslardan {t_shaxslar[0]} bilan, zamonaviy shaxslardan {z_shaxslar[0]} bilan suhbat qilishni xohlardim')
a = t_shaxslar.pop(1)
b = z_shaxslar.pop(3)
print(a + ' buyuk hadisshunos olim,', b + " O'zbekiston Respublikasining Prezidenti")


friends = []

friends.append('Fazliddin')
friends.append('Shohruh')
friends.append('Sultonqul')
friends.append('Sherali')
friends.append('Xasan')
friends.remove('Sherali')
friends.insert(0, 'Mahmud')
friends.insert(-1, 'Baxtiyor')
friends.insert(2, 'Ravshan')

print(friends)

mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(2))
print(mehmonlar)


