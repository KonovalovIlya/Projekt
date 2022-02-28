import math
from typing import List


class Square:
    def __init__(self, side : int) -> None:
        self.side = side

    def perimeter(self) -> float:
        return self.side * 4

    def square(self) -> float:
        return self.side**2


class Triangle:
    def __init__(self, bottom : int, height : int) -> None:
        self.bottom = bottom
        self.height = height

    def perimeter(self) -> float:
        side = math.sqrt((self.bottom/2)**2 + self.height**2)
        return side * 2 + self.bottom

    def square(self) -> float:
        return (self.bottom * self.height) / 2


class Cube:
    def __init__(self, sides : List) -> None:
        self.sides = sides

    def square(self) -> float:
        return self.sides[0].square() * len(self.sides)


class Pyramid:
    def __init__(self, sides: List['Triangle, Triangle, Triangle, Triangle, Square']) -> None:
        self.sides = sides

    def square(self) -> float:
        return self.sides[0].square() * (len(self.sides) - 1) + self.sides[4].square()


tri1 = Triangle(4, 5)
tri2 = Triangle(4, 5)
tri3 = Triangle(4, 5)
tri4 = Triangle(4, 5)
p1 = Square(4)
s1 = Square(4)
s2 = Square(4)
s3 = Square(4)
s4 = Square(4)
s5 = Square(4)
s6 = Square(4)
pyramid = Pyramid([tri1, tri2, tri3, tri4, p1])
cube = Cube([s1, s2, s3, s4, s5, s6])
print(cube.square())
print(pyramid.square())
