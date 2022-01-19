# Автомобиль имеет координаты своего положения и угол, описывающий направление движения. Он может быть изначально
# поставлен в любую точку с любым направлением (конструктор), может проехать в выбранном направлении определённое
# расстояние и может повернуть, то есть изменить текущее направление на любое другое (передаём привет математике и
# формулам).
#
# Реализуйте класс автомобиля, а также класс, который будет описывать автобус. Кроме того, что имеется у автомобиля,
# у автобуса должны быть поля, содержащие число пассажиров и количество полученных денег, изначально равные нулю. Также
# должны быть методы «войти» и «выйти», изменяющие число пассажиров. Наконец, метод move должен быть переопределён, чтобы
# увеличивать количество денег в соответствии с количеством пассажиров и пройденным расстоянием.
import math


class Vehicle:
    direction_dict = {
        1: 60,
        2: 30,
        3: 0,
        4: 330,
        5: 300,
        6: 270,
        7: 240,
        8: 210,
        9: 180,
        10: 150,
        11: 120,
        12: 90,
    }
    def __init__(self, x, y, direction):
        self.__position = x, y
        self.__direction = direction

    def set_position(self, x, y):
        self.__position = x, y

    def get_position(self):
        return self.__position

    def move(self):
        move_range = 10
        direction = self.direction_dict[self.__direction]
        direction /= 57.2958
        y = move_range * math.sin(direction)
        x = move_range * math.cos(direction)
        self.set_position(x, y)

    def change_direction(self, direction):
        self.__direction = direction

    def __str__(self):
        return 'Координаты равны {}'.format(self.get_position())

car = Vehicle(0, 0, 2)
print(car)
car.move()
print(car)
car.change_direction(11)
car.move()
print(car)
