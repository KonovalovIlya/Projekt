# Один буддист-программист решил создать свой симулятор жизни, в котором нужно набрать 500 очков кармы (это константа),
# чтобы достичь просветления.
#
# Каждый день вызывается специальная функция one_day(), которая возвращает количество кармы от 1 до 7 и может с
# вероятностью 1 к 10 выкинуть одно из исключений:
#
# KillError
# DrunkError
# CarCrashError
# GluttonyError
# DepressionError
# Напишите такую программу. Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении кармы
# до уровня константы. Исключения обработайте и запишите в
import random

class KillError(Exception):
    pass
class DrunkError(Exception):
    pass
class CarCrashError(Exception):
    pass
class GluttonyError(Exception):
    pass
class DepressionError(Exception):
    pass

KARMA = 500

def one_day():
    errors = [
        KillError('Буддист помер'),
        DrunkError('Буддист напился'),
        CarCrashError('Буддист помер в автокатастрофе'),
        GluttonyError('Буддист помер с голода'),
        DepressionError('Буддист помер от депрессии'),
    ]
    # try:
    score = random.randint(1,7)
    if random.choices((False, True), (1, 1 / 10))[0]:
        raise random.choice(errors)
    return score
    # except KillError:
    #     print('Буддист помер')
    # except DrunkError:
    #     print('Буддист напился')
    # except CarCrashError:
    #     print('Буддист помер в автокатастрофе')
    # except GluttonyError:
    #     print('Буддист помер с голода')
    # except DepressionError:
    #     print('Буддист помер от депрессии')


karma_cur = 0
while karma_cur != KARMA:
    karma_cur += one_day()
    print(karma_cur)