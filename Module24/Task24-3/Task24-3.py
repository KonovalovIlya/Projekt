# На координатной плоскости рисуются окружности, у каждой окружности следующие параметры: координаты X и Y центра
# окружности и значение R ― это радиус окружности. По умолчанию центр находится в (0, 0), а радиус равен 1.
#
# Реализуйте класс «Окружность», который инициализируется по этим параметрам. Круг также может:
#
# Находить и возвращать свою площадь.
# Находить и возвращать свой периметр.
# Увеличиваться в K раз.
# Определять, пересекается ли он с другой окружностью.
import math


class Circle:

    def __init__(self, x = 0, y = 0, r = 1):
        self.x = x
        self.y = y
        self.r = r

    def circle_square(self):
        self.s = math.pi * self.r**2
        return self.s

    def circle_perimetr(self):
        self.p = math.pi * (self.r * 2)
        return self.p

    def go_biger(self, number):
        self.r *= number

    def collision(self, circle_2):
        res = math.sqrt((self.x - circle_2.x)**2 + (self.y - circle_2.y)**2)
        if res > self.r + circle_2.r:
            print('Не пересекаютя')
        else:
            print('Пересекаются')


circle_1 = Circle(3, 2, 4)
circle_2 = Circle(-2, -1, 3)
print(circle_1.circle_square())
print(circle_2.circle_square())
print(circle_1.circle_perimetr())
print(circle_2.circle_perimetr())
circle_1.collision(circle_2)
circle_1.go_biger(3)
circle_2.go_biger(2)
print(circle_1.r)
print(circle_2.r)
circle_1.collision(circle_2)
