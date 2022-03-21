from typing import List
from functools import reduce


def func(a, b):
    res = a*b
    return res


res = 1
floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]

names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]

numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

# Каждое число из списка floats возводится в третью степень и округляется до трёх знаков после запятой.
print(list(map(lambda x: round(x**3, 3), floats)))
# Из списка names берутся только те имена, в которых есть хотя бы пять букв.
print(list(filter(lambda x: len(x) >= 5, names)))
# Берётся произведение всех чисел из списка numbers.
print(reduce(func, numbers))
