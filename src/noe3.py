def number_count(n):
    count = 0
    while n != 0:
        count += 1
        n //= 10
    return count

def number_summ(n):
    count = 0
    while n != 0:
        count += n % 10
        n //= 10
    return count


number = int(input('Введите число: '))
if number > 0:
    number_count(number)
    number_summ(number)
    print(f'Количество цыфр {number_count(number)}')
    print(f'Сумма цыфр {number_summ(number)}')
    print(f'Разность суммы и кол-ва цифр {number_summ(number) - number_count(number)}')
else:
    print('Ошибка ввода')

