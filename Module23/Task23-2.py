import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    try:
        return x / y
    except ZeroDivisionError:
        print("В первой функции деление на ноль")


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    try:
        return x / y
    except ZeroDivisionError:
        print("Во второй функции деление на ноль")


my_list = []
file = open('coordinates.txt', 'r')
for line in file:
    nums_list = line.split()
    res1 = f(int(nums_list[0]), int(nums_list[1]))
    res2 = f2(int(nums_list[0]), int(nums_list[1]))
    number = random.randint(0, 100)
    try:
        my_list.append(sorted([res1, res2, number]))
    except TypeError:
        print('Не подходящий тип данных для сортировки')
file.close()
file_2 = open('result.txt', 'a')
for i in my_list:
    try:
        file_2.write(str(i))
        file_2.write('\n')
    except TypeError:
        print('Тип данных не строка')
file_2.close()

