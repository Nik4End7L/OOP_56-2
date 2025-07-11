# Инкапсуояция, Абстракция.
import random

class BankAccount:

	# Атрибут класса
	__def_pass = 'admin'

	def __init__(self, login, balance, password):
		# Атрибуты объекта класса
		self.login = login
		self._balance = balance # Защищенный атрибут
		self.__password = password # Приватный атрибут

	def get_user(self):
		return print(f'{self.user}')

	def __generate_default_pass(self):
		self.__password = self.__def_pass

	def reset_pass(self):
		self.__generate_default_pass()
		return print('Password reset!')

john = BankAccount('John', 4700, 43214321)
print(john._BankAccount__password)
john.reset_pass()
print(john._BankAccount__password)
# print(john._BankAccount__password) # досутачлись
# print(dir(john))

from abc import ABC, abstractmethod

# Абстрактный класс
class Animal(ABC):

	@abstractmethod
	def step(self):
		pass

	@abstractmethod
	def make_sound(self):
		pass


class Dog(Animal):
	
	def __init__(self, nickname):
		self.nickname = nickname

	def step(self):
		return print(f'Step.')

	def make_sound(self):
		return print(f'{self.nickname} Gaf Gaf.')

sharik = Dog('Sharik')
sharik.make_sound()