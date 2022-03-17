import functools


def count(cls):
    another_cls = None
    if cls != another_cls:
        another_cls = cls
        return another_cls
    else:
        return  cls


def singleton(cls):
    @functools.wraps(cls)
    def wrap(*args, **kwargs):
        count(cls)
        return
    return wrap


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)

# Результат:
# 1986890616688
# 1986890616688
# True