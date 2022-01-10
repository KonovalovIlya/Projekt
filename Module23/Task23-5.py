total_summ = 0
calc = open('calc.txt', 'r')
for string in calc:
    # try:
        if string.endswith('\n'):
            string = string[:-1]
        a = int(string.split()[0])
        b = int(string.split()[2])
        if string.split()[1] == '+':
            res = a + b
        elif string.split()[1] == '-':
            res = a - b
        elif string.split()[1] == '*':
            res = a * b
        try:
            if string.split()[1] == '/':
               res = a / b
            elif string.split()[1] == '//':
                res = a // b
            elif string.split()[1] == '%':
                res = a % b
        except ZeroDivisionError:
            print('Ошибка деления на ноль')
        try:
            if not int(res):
                raise ValueError()
            total_summ += res
        except ValueError:
            print('Нельзя привести к числовому типу')
print(total_summ)