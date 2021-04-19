cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort()
print(cars)


cars = ['Bmw', 'mercedes benz', 'Volvo', 'general motors', 'tesla', 'audi']
cars.sort()
print(cars)

cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort(reverse=True)
print(cars)


mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
print("sorted() qaytargan ro'yhat: ", sorted(mehmonlar))
print("Asl ro'yhat o'zgarmay qoldi: ", mehmonlar)

print(sorted(mehmonlar, reverse=True))


ages = [65, 23, 43, 21, 56, 76, 12]
ages.sort()
print(ages)
print(sorted(ages, reverse=True))


sonlar = [1, 2, 3, 4, 5, 40, 30, 20, 10]
sonlar.reverse()
print(sonlar)

fruits = ['lemon', 'banana', 'pear', 'apple', 'grapefruit', 'orange', 'melon']
fruits.reverse()
print(fruits)
print("Elementlar soni: ", len(fruits)) # len(fruits) ro'yxat uzunligini qaytaradi


sonlar = list(range(0,11))
print(sonlar)


juft_sonlar = list(range(0,11,2))
toq_sonlar = list(range(1,11,2))

print("Juft sonlar: ", juft_sonlar)
print("Toq sonlar: ", toq_sonlar)

narhlar = [10500, 9500, 12900, 3200, 95000, 120]
arzon = min(narhlar)
qimmat = max(narhlar)
jami = sum(narhlar)
print("Eng arzon narh:", arzon, ". Eng qimmat narh:", qimmat, ". Jami:", jami)


cars = ['bmw', 'mercedes benz', 'general motors', 'volvo', 'tesla', 'audi']
my_cars = cars[0:3] # 0-indeskdan boshlab 3 ta element ajratib olamiz
print(my_cars)

# print(cars[2:5]) # 2-3-4-elementlarni ajratib olamiz (5 kirmaydi)
print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi

sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
sonlar2 = sonlar # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
sonlar2.append(6)
sonlar2.append(7)
print("Bu sonlar ro'yxati: ", sonlar)
print("Bu sonlar2 ro'yxati: ", sonlar2)

sonlar2 = sonlar[:]
sonlar2.append(6)
sonlar2.append(7)
print("Bu sonlar ro'yxati: ", sonlar)
print("Bu sonlar2 ro'yxati: ", sonlar2)


toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard') # o'zgarmas ro'yxat
print(toys[0])
print(toys[-1])
print(toys[2:5])

toys = list(toys)  # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
Ro'yxatga o'zgartirishlar kiritamiz
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqueen'
toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
print(toys)


# -----------------------------------------
# HOMEWORK

# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar = ["O'zbekiston", 'Amerika', 'Malayziya', 'Saudiya Arabistoni', 'Turkiya']
print(davlatlar)

# Ro'yxatning uzunligini konsolga chiqaring
print(len(davlatlar))

# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(sorted(davlatlar))

# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(sorted(davlatlar, reverse=True))

# Asl ro'yxatni qaytadan konsolga chiqaring
print(davlatlar)

# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse()
print(davlatlar)

# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
sonlar = list(range(120, 1200))
print(sonlar)

# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
print(sum(sonlar))

# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
print(max(sonlar) - min(sonlar))

# Ro'yxatdagi elementlar sonini hisoblang
print(len(sonlar))

# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(sonlar[:20])
print(sonlar[530:550])
print(sonlar[-20:])

# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['palov', 'mastava', 'blinchik', 'qaymoq', 'manti', "sariyog'"]

# nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]

# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove('palov')
nonushta.remove('mastava')
nonushta.remove('manti')
nonushta.append('tuxum')
nonushta.append('sut')

# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(nonushta)
print(taomlar)

# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
print(nonushta)
nonushta[0] = "qaymoq va non"