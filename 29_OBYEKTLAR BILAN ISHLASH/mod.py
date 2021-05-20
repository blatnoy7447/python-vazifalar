class Dog:

	def __init__(self, name):
		self.name = name
		self.breed = 'beagle'
		self.location = 'qarshi'
		self.gav()

	def gav(self):
		print(f'GAV! GAV! GAV! I am {self.name}')
