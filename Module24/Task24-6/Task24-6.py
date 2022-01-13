# Для одной игры необходимо реализовать механику магии, где при соединении двух элементов получается новый. У нас есть
# четыре базовых элемента: «Вода», «Воздух», «Огонь», «Земля». Из них как раз и получаются новые: «Шторм», «Пар»,
# «Грязь», «Молния», «Пыль», «Лава».
#
# Вот таблица преобразований:
#
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава
#
# Напишите программу, которая реализует все эти элементы. Каждый элемент необходимо организовать как отдельный класс.
# Если результат не определён, то возвращается None.
#
# Примечание: сложение объектов можно реализовывать через магический метод __add__, вот пример использования:
#
# class Example_1:
#
#     def __add__(self, other):
#         return Example_2()
#
#
# class Example_2:
#     answer = 'сложили два класса и вывели'
#
#
# a = Example_1()
# b = Example_2()
# c = a + b
# print(c.answer)

# Дополнительно: придумайте свой элемент (или элементы), а также реализуйте его взаимодействие с остальными элементами.

class Water:
    def __add__(self, other):
        if other.__class__ == Air().__class__:
            return Storm()
        elif other.__class__ == Fire().__class__:
            return Steam()
        elif other.__class__ == Earth().__class__:
            return Mud()
        else:
            return None

class Air:
    def __add__(self, other):
        if other.__class__ == Water().__class__:
            return Storm()
        elif other.__class__ == Fire().__class__:
            return Lightning()
        elif other.__class__ == Earth().__class__:
            return Dust()
        else:
            return None

class Fire:
    def __add__(self, other):
        if other.__class__ == Air().__class__:
            return Lightning()
        elif other.__class__ == Water().__class__:
            return Steam()
        elif other.__class__ == Earth().__class__:
            return Lava()
        else:
            return None

class Earth:
    def __add__(self, other):
        if other.__class__ == Air().__class__:
            return Dust()
        elif other.__class__ == Water().__class__:
            return Mud()
        elif other.__class__ == Fire().__class__:
            return Lava()
        else:
            return None

class FireStorm:
    a = 'FireStorm'

class Storm:
    a = 'Storm'
    def __add__(self, other):
        if other.__class__ == Lava().__class__:
            return FireStorm()
        else:
            return None

class Steam:
    a = 'Steam'

class Mud:
    a = 'Mud'

class Lightning:
    a = 'Lightning'

class Dust:
    a = 'Dust'

class Lava:
    a = 'Lava'

water = Water()
air = Air()
fire = Fire()
earth = Earth()
g = water + air
print(g.a)
