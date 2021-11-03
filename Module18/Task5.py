LENGTH = 8
CAP_SYM = 1
NUMS = 3

while True:
    password = input('Введите пароль: ')
    count_upper = 0
    count_digit = 0
    for symbol in password:
        if symbol.isupper():
            count_upper += 1
        if symbol.isdigit():
            count_digit += 1
    if len(password) < LENGTH:
        print('Пароль должен состоять минимум из восьми символов, '
              '\nв нём должна быть хотя бы одна большая буква и хотя бы три цифры.'
              )
    elif count_upper < CAP_SYM:
        print('Пароль должен состоять минимум из восьми символов, '
              '\nв нём должна быть хотя бы одна большая буква и хотя бы три цифры.'
              )
    elif count_digit < NUMS:
        print('Пароль должен состоять минимум из восьми символов, '
              '\nв нём должна быть хотя бы одна большая буква и хотя бы три цифры.'
              )
    else:
        print('Привет!')
        break
# пароль должен состоять минимум из восьми символов,
# в нём должна быть хотя бы одна большая буква и хотя бы три цифры.