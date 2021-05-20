# Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar 
#(model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)

# Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing
#get_info() metodi avto haqida to'liq ma'lumotni matn ko'rinishida qaytarsin

# Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
#update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin
class Avto:

	def __init__(self, make, model, rang, korobka, narh):
		self.make = make
		self.model = model
		self.rang = rang
		self.korobka = korobka
		self.narh = narh
		self.km = 0

	def get_info(self):
		"""Avto haqida malumotlarni qaytaradi"""
		return (f"Ishlab chiqaruvchi:{self.make}, "
				f"Rangi:{self.rang}, Model:{self.model}, "
				f"Korobka:{self.korobka}, Narhi:{self.narh}, Kilometr:{self.km}")

	def get_make(self):
		"""Avtoning kompaniyasini qaytaradi"""
		return self.make

	def get_model(self):
		"""Avtoning modelini qaytaradi"""
		return self.model

	def get_color(self):
		"""Avtoning rangini qaytaradi"""
		return self.rang

	def get_gear(self):
		"""Avtoning uzatmalar qutisini qaytaradi"""
		return self.korobka

	def get_price(self):
		"""Avtoning narhini qaytaradi"""
		self.narh = narh

	def set_km(self, km):
		"""Avtoning kilometrini qaytaradi"""
		self.km = km

	def update_km(self):
		"""Avtoning kilometrini yangilovchi metod"""
		self.km += 10

avto1 = Avto("GM", "Malibu", "Qora", "Avtomat", 33000)
avto2 = Avto("Kia", "K5", "Oq", "Avtomat", 37000)
avto3 = Avto("GM", "Lacetti", "Qizil", "Mexanika", 12500)
avto4 = Avto("Mers", "AMG GT I", "Yashil", "Robot", 303000)
avto1.set_km(1250)
# print(avto1.get_info())
avto2.update_km()
# print(avto2.get_info())

# Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring 
#(salon nomi, manzili, sotuvdagi avtomobillar va hokazo)

# Avtosalonga yangi avtomobillar qo'shish uchun metod yozing

# Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing

# dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan va Pythondagi 
#turli klass va obyektlarning xususiyatlari va metodlarini toping (dir(str), dir(int) va hokazo)
class AvtoSalon:

	def __init__(self, salon_nomi, manzili):
		self.salon_nomi = salon_nomi
		self.manzili = manzili
		self.cars = []
		self.avtolar_soni = 0

	def add_car(self, car):
		self.cars.append(car)
		self.avtolar_soni += 1

	def get_cars(self):
		return [car.get_info() for car in self.cars]
		

avtosalon1 = AvtoSalon("Luxury Motors", "Toshkent")
avtosalon2 = AvtoSalon("Avenue Motors", "Toshkent")

avtosalon1.add_car(avto1)
avtosalon2.add_car(avto2)
avtosalon1.add_car(avto3)
avtosalon2.add_car(avto4)

luxury_cars = avtosalon1.get_cars()
avenue_cars = avtosalon2.get_cars()
# print(avtosalon1.avtolar_soni)
# print(luxury_cars)
# print(avtosalon2.avtolar_soni)
# print(avenue_cars)

# print(dir(Avto))
# print(dir(avto1))
# print(avto1.__dict__)

def see_methods(klass):
	return [method for method in dir(klass) if method.startswith('__') is False]

print(see_methods(Avto))
print(see_methods(avto1))
print(see_methods(AvtoSalon))
