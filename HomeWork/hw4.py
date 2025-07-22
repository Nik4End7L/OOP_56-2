class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle: Width = {self.width}, Height = {self.height}"

    def __add__(self, other):
        new_width = self.width + other.width
        new_height = self.height + other.height
        return Rectangle(new_width, new_height)

r1 = Rectangle(5, 10)
r2 = Rectangle(3, 7)

r3 = r1 + r2
print(r3)