#ООП 56-2

class Hero:

	#Конструктор класса
	def __init__(self, name, lvl, hp):
		#Атрибуты класса
		self.name = name
		self.lvl = lvl
		self.hp = hp

	#Метод класса
	def introduce(self):
		return print(f'Hello, my name is {self.name}')

#Обькт | Экземпляр класса
# kirito = Hero('Kirito', 20, 99)

# kirito.introduce()
# asuna.introduce()
# print(kirito.name, kirito.lvl)
# print(asuna.name, asuna.lvl)


asuna = Hero('Asuna', 12, 48)
some_text = 'Some text'


# print(type(asuna))
# print(type(some_text))