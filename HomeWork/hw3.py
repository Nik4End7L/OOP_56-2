
# Инкапсуляция
class Student:
	def __init__(self, name, grade, password, ):
		self.name = name
		self._grade = grade
		self.__password = password

	def change_password(self, new_pass):
		self.__password = new_pass

	def get_info(self):
		return print(f'Name: {self.name}, Grade: {self._grade}')


# Абстракции
from abc import ABC, abstractmethod

class Vehicle(ABC):
	@abstractmethod
	def move(self):
		pass

	@abstractmethod
	def stop(self):
		pass

class Car(Vehicle):
	def move(self):
		return print(f'Car is Moving.')
	def stop(self):
		return print(f'Car stopped.')
class Bike(Vehicle):
	def move(self):
		return print(f'Bike is moving.')
	def stop(self):
		return print(f'Bike stopped.')


# Примеры
studentsc = Student("S.C", '1st Course', "********")
studentsc.get_info()
studentsc.change_password("********A.A")

print(studentsc._Student__password)

Shevrolet = Car()
Shevrolet.move()
Shevrolet.stop()

bike = Bike()
bike.move()
bike.stop()

