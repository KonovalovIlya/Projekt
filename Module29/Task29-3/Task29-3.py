import functools
import time
from datetime import datetime


def timer(func):
    @functools.wraps(func)
    def wrapped(*arg, **kwarg):
        start = time.time()
        print('Запускается {name}. Дата и время запуска: {datetime} '.format(
            name=func.__name__,
            datetime=datetime.utcnow()
        ))
        func()
        stop = time.time() - start
        return('Завершение {name}, время работы = {time}'.format(
            name=func.__name__,
            time=stop
        ))
    return wrapped


def log_methods(form):
    if form == "b d Y - H:M:S":
        decorator = timer
    @functools.wraps(decorator)
    def dec(cls):
        for i in dir(cls):
            if not i.startswith('__'):
                a = getattr(cls, i)
                b = decorator(a)
                setattr(cls, i, b)
        return cls
    return dec


@log_methods("b d Y - H:M:S")
class A:
    # def __init__(self):
    #     print(1)

    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")


    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


# d = A()
my_obj = B()
# print(my_obj)
# print(d)
my_obj.test_sum_1()
my_obj.test_sum_2()


