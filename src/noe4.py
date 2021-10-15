CONSTANTA = '.'

def number_reverted(number):
    part_1 = 0
    part_2 = 0
    symbol_all = 0
    for symbol in number:
        symbol_all += 1
    for symbol in number:
        if symbol != CONSTANTA:
            part_1 += 1
        else:
            break
    part_2 = part_1 - symbol_all
    part_1_1 = ''
    part_1_1 += number[part_1-1::-1]
    part_2_1 = ''
    part_2_1 += number[symbol_all:part_2:-1]
    number = part_1_1 + CONSTANTA + part_2_1
    return float(number)


number_1 = input('Введите пераое число: ')
number_2 = input('Введите второе число: ')

number_1_reverted = number_reverted(number_1)
number_2_reverted = number_reverted(number_2)

print(f'Первое число наоборот {number_1_reverted}')
print(f'Второе число наоборот {number_2_reverted}')
print(f'Сумма {number_1_reverted + number_2_reverted}')
