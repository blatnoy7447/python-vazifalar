# Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. 
#Bu xususiyat parametr sifatida uzatilmasin va obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])

# Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.

class Shaxs:

	def __init__(self, ism, familiya, passport, tyil):
		self.ism = ism
		self.familiya = familiya
		self.passport = passport
		self.tyil = tyil

	def get_info(self):
		
		info = f"{self.ism} {self.familiya}. "
		info += f"Passport:{self.passport}, {self.tyil}-yilda tug'ilgan"
		return info

	def get_age(self, yil):
		return yil - self.tyil

# inson = Shaxs("Hasan", "Alimov", "FB001122", 1995)
# print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda")

class Fan():

	def __init__(self, nomi):
		self.nomi = nomi
		self.talabalar = []

	def add_student(self, talaba):
		self.talabalar.append(talaba)

	def get_students(self):
		return [talaba.get_info() for talaba in self.talabalar]


class Talaba(Shaxs):
	
	def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
		
		super().__init__(ism, familiya, passport, tyil)
		self.idraqam = idraqam
		self.bosqich = 1
		self.manzil = manzil
		self.fanlar = []

	def get_id(self):
		return self.idraqam

	def get_bosqich(self):
		return self.bosqich
	
	def get_info(self):
		info = f"{self.ism} {self.familiya}. "
		info += f"{self.get_bosqich()}-bosqich. ID raqami:{self.idraqam}"
		return info

	def fanga_yozil(self, fan):
		self.fanlar.append(fan)


class Manzil:
	
	def __init__(self,uy,kocha,shahar,viloyat):
		self.uy = uy
		self.kocha = kocha
		self.shahar = shahar
		self.viloyat = viloyat

	def get_manzil(self):
		
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
talaba3_manzil = Manzil(10,"Qilichev","Qarshi","Qashqadaryo")
talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012",talaba_manzil)
talaba3 = Talaba("Usmonjon","Shamsiyev","BB112299",2001,"2220012",talaba3_manzil)
# print(talaba.manzil.get_manzil())
# print(talaba.manzil.shahar)

matematika = Fan("Oliy matematika")
adabiyot = Fan("Ona tili va Adabiyot")
matematika.add_student(talaba)
adabiyot.add_student(talaba3)

adab_talabalar = adabiyot.get_students()
mat_talabalar = matematika.get_students()
print(adab_talabalar)
print(mat_talabalar)
print(talaba.manzil.get_manzil())









