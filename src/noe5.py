def min_divisor(number):
    for divider in range(2, number + 1):
        if number % divider == 0:
            return divider
            break
        else:
            return number


number = int(input('Введите число: '))
result = min_divisor(number)
print(f'Минимальный делитель {result}')