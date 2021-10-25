number = int(input('Введите число: '))

number_list = []

for numbers in range(1, number + 1):
    if numbers % 2 != 0:
        number_list.append(numbers)
print(number_list)
