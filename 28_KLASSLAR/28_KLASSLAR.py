# KLASS YARATISH
class Talaba:
	"""Talaba nomli klass yaratamiz"""
	def __init__(self,ism,familiya,tyil):
		"""Talabaning xususiyatlari"""
		self.ism = ism
		self.familiya = familiya
		self.tyil = tyil
	# KLASSGA METODLAR QO'SHAMIZ
	# Klassimiz istalgancha metodlardan iborat bo'lishi mumkin:

	def get_name(self):
		"""Talabaning ismini qaytaradi"""
		return self.ism

	def get_lastname(self):
		"""Talabaning familiyasini qaytaradi"""
		return self.familiya

	def get_fullname(self):
		"""Talabaning ism-familiyasini qaytaradi"""
		return f"{self.ism} {self.familiya}"

	# ARGUMENT QABUL QILUVCHI METODLAR
	def get_age(self,yil):
		"""Talabaning yoshini qaytaradi"""
		return yil-self.tyil

	def tanishtir(self):
		print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tug'ilganman.")


talaba1 = Talaba('Alijon', 'Valiyev', 2000)
print(talaba1.ism)
print(talaba1.familiya)


# KLASSDAN BIR NECHTA OBYEKTLAR YARATISH
talaba2 = Talaba("Olim","Olimov",1995)
talaba3 = Talaba("Husan","Akbarov",2004)
print(talaba3.ism)

# OBYEKTNING METODLARIGA MUROJAT QILAMIZ
talaba4 = Talaba("Hasan","Akbarov",2004)
talaba4.tanishtir()
print(talaba1.get_fullname())
print(talaba3.get_age(2021))


# pass OPERATORI
class User:
	def __init__(self, name, username, email):
		self.name = name
		self.username = username
		self.email = email

	def describe():
		pass

	def get_email():
		pass



		