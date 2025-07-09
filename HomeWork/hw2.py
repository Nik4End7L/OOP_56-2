class Transport:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self):
        print(f'Transport is moving.')

class Car(Transport):
    def __init__(self, name, speed, wheels):
        super().__init__(name, speed)
        self.wheels = wheels

    def move(self):
        super().move()
        print(f'{self.name} is driving {self.wheels} wheels.')

class Plane(Transport):
    def __init__(self, name, speed, wings):
        super().__init__(name, speed)
        self.wings = wings

    def move(self):
        super().move()
        print(f'{self.name} is flying {self.speed}.')

class Boat(Transport):
    def __init__(self, name, speed, oars):
        super().__init__(name, speed)
        self.oars = oars

    def move(self):
        super().move()
        print(f'{self.name} is sailing using {self.oars}.')


transport = Transport('Legs', '3m/s')
transport.move()

vehicle = Car('Shevrolet', '373km/h', 'Rally')
vehicle.move()
my_plane = Plane('SU-57', '2.450km/h', 'NotRightTriangle')
my_plane.move()
my_boat = Boat('Submarine', '10km/h', 'alloy oars')
my_boat.move()