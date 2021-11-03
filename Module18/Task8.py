def shift(string, string_1):
    count = 0
    shift = int(input('Шаг: '))
    for _ in range(len(string)):
        if shift > 0 and string != string_1:
            string = ''.join([string[shift:], string[:shift]])
            count += 1
        elif shift < 0 and string != string_1:
            string = ''.join([string[:shift], string[shift:]])
            count += 1
    if string == string_1:
        print('Первая строка получается из второй со сдвигом {count}.'.format(count = count))
    else:
        print('Вторую строку нельзя получить из первой с помощью циклического сдвига.')


string = input('1-я строка: ')
string_1 = input('2-я строка: ')

shift(string, string_1)
