# У вас есть файл с протоколом регистраций пользователей на сайте — registrations.txt
#
# Каждая строка содержит: ИМЯ ИМЕЙЛ ВОЗРАСТ, разделённые пробелами.
#
# Например:
#
# Василий test@test.ru 27
#
#
#
# Напишите программу, которая проверяет данные из файла для каждой строки:
#
# Присутствуют все три поля.
# Поле имени содержит только буквы.
# Поле «Имейл» содержит @ и . (точку).
# Поле «Возраст» является числом от 10 до 99.
# В результате проверки сформируйте два файла:
#
# registrations_good.log — для правильных данных, записывать строки как есть,
# registrations_bad.log — для ошибочных, записывать строку и вид ошибки.
# Для валидации строки данных напишите функцию, которая может выдавать исключения:
#
# НЕ присутствуют все три поля: IndexError.
# Поле имени содержит НЕ только буквы: NameError.
# Поле «Имейл» НЕ содержит @ и .(точку): SyntaxError.
# Поле «Возраст» НЕ является числом от 10 до 99: ValueError.

def good_or_bad_f(string):
    list_ = []
    try:
        if not len(string.split()) >= 3:
            raise IndexError('НЕ присутствуют все три поля')
    except IndexError:
        list_.append(IndexError('НЕ присутствуют все три поля'))
    else:
        try:
            if not string.split()[0].isalpha():
                raise NameError('Поле имени содержит НЕ только буквы')
        except NameError:
            list_.append(NameError('Поле имени содержит НЕ только буквы'))
        try:
            if not '@' in string.split()[1] or not '.' in string.split()[1]:
                raise SyntaxError('Поле «Имейл» НЕ содержит @ и .(точку)')
        except SyntaxError:
            list_.append(SyntaxError('Поле «Имейл» НЕ содержит @ илиwe .(точку)'))
        try:
            if not int(string.split()[2]) in range(10, 99):
                raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')
        except ValueError:
            list_.append(ValueError('Поле «Возраст» НЕ является числом от 10 до 99'))
    if list_ == []:
        return string
    else:
        return string, list_


with open('registrations.txt', 'r', encoding='UTF-8') as reg_file:
    for string in reg_file:
        reg_is = good_or_bad_f(string)
        if reg_is == string:
            with open('registrations_good.log', 'a', encoding='UTF-8') as good_reg:
                good_reg.write(reg_is)
        else:
            with open('registrations_bad.log', 'a', encoding='UTF-8') as bad_reg:
                for i in reg_is:
                    bad_reg.write(str(i))
                    bad_reg.write('\n')
                bad_reg.write('-'*19)
                bad_reg.write('\n')
