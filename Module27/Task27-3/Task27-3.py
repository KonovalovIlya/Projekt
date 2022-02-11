# Реализуйте декоратор logging, который будет отвечать за логирование функций. На экран выводится название функции
# и её документация. Если во время выполнения декорируемой функции возникла ошибка, то в файл function_errors.log
# записываются названия функции и ошибки.
#
# Также постарайтесь сделать так, чтобы программа не завершалась после обнаружения первой же ошибки, а обрабатывала
# все декорируемые функции и сразу записывала все ошибки в файл.
#
# Дополнительно: запишите дату и время возникновения ошибки, используя модуль datetime.
#
import datetime


def logging(func):
    def wrapped():
        print('Выполняется функция {func}\nДокументация к функции: {doc}'.format(
            func=func.__name__,
            doc=func.__doc__
        ))

        return func()

    return wrapped

@logging
def test():
    """ Тест декоратора """
    print('<Тут что-то происходит...>')


try:
    test(1)
except TypeError:
    with open('function_errors.log', 'w', encoding='UTF-8') as file:
        file.write('Время - {h}:{m}:{s}\tДата - {date}\nНазвание ошибки: {name}\nОписание ошибки: {str}'.format(
            h=datetime.datetime.now().time().hour,
            m=datetime.datetime.now().time().minute,
            s=datetime.datetime.now().time().second,
            date=datetime.datetime.now().date(),
            name=TypeError.__name__,
            str=TypeError.__doc__
        ))
    print('OSHIBKA')