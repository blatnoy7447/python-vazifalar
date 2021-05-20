class Talaba:
	"""Talaba nomli class yaratamiz"""
	def __init__(self, ism, familiya, tyil):
		"""Talabaning xususiyatlari"""
		self.ism = ism
		self.familiya = familiya
		self.tyil = tyil
		self.bosqich = 1

	def get_info(self):
		return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi"

talaba1 = Talaba('Alijon', 'Valiyev', 2000)
# print(talaba1.get_info())

# STANDART QIYMATNI O'ZGARTIRISH
talaba1.bosqich = 2
# print(talaba1.bosqich)
	

class Talaba:
	"""Talaba nomli class yaratamiz"""
	def __init__(self, ism, familiya, tyil):
		"""Talabaning xususiyatlari"""
		self.ism = ism
		self.familiya = familiya
		self.tyil = tyil
		self.bosqich = 1

	def get_info(self):
		return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi"

	def set_bosqich(self, bosqich):
		"""Talabaning kursini yangilovchi metod"""
		self.bosqich = bosqich

	def update_bosqich(self):
		"""Talabaning bosqichini 1 taga ko'paytirish"""
		self.bosqich += 1

talaba1 = Talaba('Alijon', 'Valiyev', 2000)
# talaba1.set_bosqich(3)
# print(talaba1.get_info())
# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())

# talaba1.update_bosqich()
# print(talaba1.get_info())

# talaba1.update_bosqich()
# print(talaba1.get_info())


# OBYEKTLAR O'RTASIDA MUNOSABAT
class Fan():
	"""Fan nomli class yaratamiz"""
	def __init__(self, nomi):
		self.nomi = nomi
		self.talabalar_soni = 0
		self.talabalar = []

	def add_student(self, talaba):
		"""Fanga talabalar qo'shish"""
		self.talabalar.append(talaba)
		self.talabalar_soni += 1

	def get_students(self):
		return [talaba.get_info() for talaba in self.talabalar]#self.talabalar ichidagi har bir talaba uchun get_info() metodini bajar 

matematika = Fan("Oliy matematika")
talaba1 = Talaba("Alijon", "Valiyev", 2000)
talaba2 = Talaba("Hasan", "Alimov", 2001)
talaba3 = Talaba("Akrom", "Boriyev", 2001)

matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)

mat_talabalar = matematika.get_students()
print(matematika.talabalar_soni)
print(mat_talabalar)

















# Talaba klassimizni yangilaymiz
class Talaba:
	"""Talaba nomli klass yaratamiz"""
	def __init__(self, ism, familiya, tyil):
		"""Talabaning xususiyatlari"""
		self.ism = ism
		self.familiya = familiya
		self.tyil = tyil
		self.bosqich = 1

	def set_bosqich(self, yangi_bosqich):
		"""Talabaning kursini yangilovchi metod"""
		self.bosqich = yangi_bosqich

	def update_bosqich(self):
		"""Talabanining bosqichini 1taga ko'paytirish"""
		self.bosqich += 1

	def get_info(self):
		"""Talaba haqida ma'lumot"""
		return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi"

	def get_name(self):
		"""Talabaning ismini qaytaradi"""
		return self.ism

	def get_lastname(self):
		"""Talabaning familiyasini qaytaradi"""
		return self.familiya

	def get_fullname(self):
		"""Talabaning ism-familiyasini qaytaradi"""
		return f"{self.ism} {self.familiya}"

	def get_age(self,yil):
		"""Talabaning yoshini qaytaradi"""
		return yil - self.tyil


class Fan():
	"""Fan nomli klass"""
	def __init__(self, nomi):
		self.nomi = nomi
		self.talabalar_soni = 0
		self.talabalar = []

	def add_student(self, talaba):
		"""Fanga talabalar qo'shish"""
		self.talabalar.append(talaba)
		self.talabalar_soni += 1

	def get_name(self):
		"""Fan nomi"""
		return self.nomi

	def get_students(self):
		"""Fanga yozilgan talabalar haqida ma'lumot"""
		return [x.get_info() for x in self.talabalar]

	def get_students_num(self):
		"""Fanga yozilgan talabalar soni"""
		self.talabalar_soni

# print(dir(Talaba))
talaba1 = Talaba("Alijon", "Valiyev", 2000)






def see_methods(klass):
	return [method for method in dir(klass) if method.startswith('__') is False]

# print(see_methods(Talaba))

# print(see_methods(talaba1))

# __dict__ METODI
# print(talaba1.__dict__.keys())














