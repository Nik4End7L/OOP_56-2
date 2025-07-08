# # Наследование

# # Родительский|Супер класс
# class Hero:

# 	def __init__(self, name, lvl, age, hp):
# 		self.name = name
# 		self.lvl = lvl
# 		self.age = age
# 		self.hp = hp

# 	def action(self):
# 		return print(f'Base action.')

# # Дочерний класс
# class MageHero(Hero):

# 	def __init__(self, name, lvl, hp, age, mp):
# 		super().__init__(name, lvl, age, hp)
# 		self.mp = mp
	
# 	def rest(self):
# 		return print('Я Отдыхаю.')

# 	def action(self):
# 		return(print('==============='))

# hero = MageHero('Hero1', 100, 26, 1000, 100)
# hero.action()

# # AdolfArtist -- Верблюжая нотация.
# # nik_end_l -- змеиная нотация.

class Animal:
	def action(self):
		return print(f'Animal')

class Swim(Animal):
	def action(self):
		return print(f'swim')
class Fly(Animal):
	def action(self):
		return print(f'fly')
class Duck(Fly, Swim):
	pass

donald_duck = Duck()
donald_duck.action()
# mro() -- что первое то и покажет.

