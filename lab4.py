class rectangle(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
	def Area(self):
		print(self.width * self.height)
	def Perimeter(self):
		return (self.width + self.height) * 2
	def Properties(self):
		print(self.width)
		print(self.height)

r = rectangle(5,6)
r.Area()
r.Perimeter()
r.Properties()

class person():
	def __init___(self, name, age, city, gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender