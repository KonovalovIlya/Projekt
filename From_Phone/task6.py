def enter_number():
    number = 1
    while number != 0:
        number = int(input('Введите числа в список: '))
        list_1.append(number)
    list_1.remove(0)
def lists_merge():
    list_1.extend(list_2)
    for index in list_1:
        if list_1.count(index) > 1:
            for _ in range(list_1.count(index) - 1):
                list_1.remove(index)


list_1 = []
list_2 = []
enter_number()
print('Первый список', list_1)
enter_number()
print('Второй список', list_2)
lists_merge()
print('Новый Первый список', list_1)