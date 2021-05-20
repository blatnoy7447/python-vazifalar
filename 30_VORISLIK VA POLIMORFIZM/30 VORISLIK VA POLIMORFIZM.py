# SUPER KLASS 
class Shaxs:
	"""Shaxslar haqida ma'lumot"""
	def __init__(self, ism, familiya, passport, tyil):
		self.ism = ism
		self.familiya = familiya
		self.passport = passport
		self.tyil = tyil

	def get_info(self):
		"""Shaxs haqida ma'lumot"""
		info = f"{self.ism} {self.familiya}. "
		info += f"Passport:{self.passport}, {self.tyil}-yilda tug'ilgan"
		return info

	def get_age(self, yil):
		"""Shaxsning yoshini qaytaruvchi metod"""
		return yil - self.tyil
inson = Shaxs("Hasan", "Alimov", "FB001122", 1995)
# print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda")


# VORIS KLASS
class Talaba(Shaxs):
	"""Talaba klassi"""
	def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
		"""Talabaning xususiyatlari"""
		super().__init__(ism, familiya, passport, tyil)
		# VORIS KLASSGA XOS XUSUSIYATLAR VA METODLAR
		self.idraqam = idraqam
		self.bosqich = 1
		self.manzil = manzil

	def get_id(self):
		"""Talabaning ID raqami"""
		return self.idraqam

	def get_bosqich(self):
		"""Talabaning o'qish bosqichi"""
		return self.bosqich
	# POLIMORFIZM — SUPER KLASS METODLARINI QAYTA YOZISH
	def get_info(self):
		"""Talaba haqida ma'lumot"""
		info = f"{self.ism} {self.familiya}. "
		info += f"{self.get_bosqich()}-bosqich. ID raqami:{self.idraqam}"
		return info


# OBYEKT ICHIDA OBYEKT
class Manzil:
	"""Manzil saqlash uchun klass"""
	def __init__(self,uy,kocha,shahar,viloyat):
		self.uy = uy
		self.kocha = kocha
		self.shahar = shahar
		self.viloyat = viloyat

	def get_manzil(self):
		"""Manzilni ko'rish"""
		manzil = f"{self.viloyat} viloyati, {self.shahar} shahri, "
		manzil += f"{self.kocha} ko`chasi, {self.uy}-uy"
		return manzil
		
# talaba1 = Talaba("Alijon", "Valiyev", "FA0001122", 2000)
# print(talaba1.get_info())
# print(talaba1.get_age(2021))

# talaba2 = Talaba("Olim", "Alimov", "AA0002233", 1999, "N000012")
# print(f"{talaba2.get_info()}. ID raqami:{talaba2.get_id()}")
# print(f"{talaba2.get_bosqich()}-bosqich talabasi")
# print(talaba2.get_info())

talaba_manzil = Manzil(9,"Ozod-diyor","Qarshi","Qashqadaryo")
talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012",talaba_manzil)
print(talaba.manzil.get_manzil())
print(talaba.manzil.shahar)








