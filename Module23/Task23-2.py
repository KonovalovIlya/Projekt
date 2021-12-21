import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    try:
        return x / y
    except ZeroDivisionError:
        print("V pervoi funkcii delenie na nol")


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    try:
        return x / y
    except ZeroDivisionError:
        print("Vo vtoroi funkcii delenie na nol")


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
        print('Ne podhodyashi tip dannih dlya sortirovki')
file.close()
file_2 = open('result.txt', 'a')
for i in my_list:
    try:
        file_2.write(str(i))
        file_2.write('\n')
    except TypeError:
        print('Tip dannih ne stroka')
file_2.close()

