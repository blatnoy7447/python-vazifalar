# Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. 
#Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab 
#qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)

# Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi 
#foydalanuvchi haqida yig'ilgan ma'lumotlarni chiroyli qilib chiqarsin 
#(masalan: "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).

# Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat qiling.

class User:
	"""Ijtimoiy tarmoq foydalanuvchisi User class"""
	def __init__(self, name, username, email, tyil):
		"""Foydalanuvchining xususiyatlari"""
		self.name = name
		self.username = username
		self.email = email
		self.tyil = tyil

	def get_name(self):
		"""Ismini qaytaradi"""
		return self.name

	def get_username(self):
		"""Nikini qaytaradi"""
		return self.username

	def get_email(self):
		"""Emailini qaytaradi"""
		return self.email

	def get_age(self, yosh):
		"""Yoshini qaytaradi"""
		return yosh-self.tyil

	def tanishtir(self):
		print(f"Ismi: {self.name}, Foydalanuvchi: {self.username}, Email: {self.email}, "
			  f"Tug'ilgan yili: {self.tyil}")

user1 = User('Maruf Yuldashev', 'blatnoy7447', 'cool.backstreet@gmail.com', 1990)
user2 = User('Mahmud Yuldashev', 'Makhmudali', 'makhmudyuldoshev@gmail.com', 1995)
user3 = User('Farruh Sultonov', 'farruhchik', 'farruh@mail.ru', 1992)
print(user3.get_age(2021))
user1.tanishtir()
print(user2.get_email())




