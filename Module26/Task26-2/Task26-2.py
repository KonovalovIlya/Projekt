def gen(number):
    for x in list_1:
        for y in list_2:
            result = x * y
            if result == number:
                yield (x, y)


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

for i in gen(to_find):
    print(i)