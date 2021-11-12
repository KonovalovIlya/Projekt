# Напишите функцию, которая принимает на вход кортеж и какой-то случайный элемент
# (его можно вводить с клавиатуры). Функция должна возвращать новый кортеж, начинающийся
# с первого появления элемента в нём и заканчивающийся вторым его появлением включительно.
#
# Если элемента нет вовсе — вернуть пустой кортеж. Если элемент встречается только один раз,
# то вернуть кортеж, который начинается с него и идёт до конца исходного.
import random

# tuple_ = tuple(random.randint(0, 10) for _ in range(10))
tuple_ = (1, 2, 3, 4, 5, 2, 6, 7)
number = int(input())
tuple_1 = ()
l = []
df = tuple_.index(number)
fd = tuple_[tuple_.index(number) + 1:].index(number) + df + 2
if tuple_.count(number) >= 2:
    tuple_1 = tuple_[df : fd]
elif tuple_.count(number) == 1:
    tuple_1 = tuple_[tuple_.index(number):]
elif not number in tuple_:
    tuple_1 = ()
print(tuple_1)