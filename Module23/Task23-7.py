total_summ = 0
for_seek = 0
with open('calc_2.txt', 'r') as calc:
    lines = calc.readlines()
    for line in lines:
        if line.endswith('\n'):
            lines[lines.index(line)] = line[:-1]
            line = line[:-1]
        if not line.split()[1] in ['+', '-', '*', '/', '//', '%']:
            print('Обнаружена ошибка в строке: {} Хотите исправить?'.format(line))
            if input() == 'Да':
                line_new = input()
                index = lines.index(line)
                lines.pop(index)
                lines.insert(index, line_new)
with open('calc_2.txt', 'w') as calc:
    for line in lines:
        calc.write(line)
        calc.write('\n')
with open('calc_2.txt', 'r') as calc:
    for string in calc:
        a = int(string.split()[0])
        b = int(string.split()[2])
        if string.split()[1] == '+':
            res = a + b
        elif string.split()[1] == '-':
            res = a - b
        elif string.split()[1] == '*':
            res = a * b
        elif string.split()[1] == '/':
           try:
               res = a / b
           except ZeroDivisionError:
               print('Ошибка деления на ноль')
        elif string.split()[1] == '//':
            try:
                res = a // b
            except ZeroDivisionError:
                print('Ошибка деления на ноль')
        elif string.split()[1] == '%':
            try:
                res = a % b
            except ZeroDivisionError:
                print('Ошибка деления на ноль')
        total_summ += res
print(total_summ)


