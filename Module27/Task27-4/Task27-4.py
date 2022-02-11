import functools

def debug(func):
    @functools.wraps(func)
    def wrapped(*arg, **kwarg):
        if arg:
            if kwarg:
                print('Вызывается {func_name}({arg}, {kwarg})'.format(
                    func_name=func.__name__,
                    arg=arg,
                    kwarg=kwarg
                ))
                res = func(*arg, **kwarg)
                print('{func_name} вернула значение {value}'.format(
                    func_name=func.__name__,
                    value=res
                ))
                return res
            else:
                print('Вызывается {func_name}({arg})'.format(
                    func_name=func.__name__,
                    arg=arg,
                ))
                res = func(*arg)
                print('{func_name} вернула значение {value}'.format(
                    func_name=func.__name__,
                    value=res
                ))
                return res
        elif not arg:
            print('Вызывается {func_name}({kwarg})'.format(
                func_name=func.__name__,
                kwarg=kwarg
            ))
            res = func(*arg, **kwarg)
            print('{func_name} вернула значение {value}'.format(
                func_name=func.__name__,
                value=res
            ))
            return res
    return wrapped

@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


print(greeting("Том"))
print(greeting("Миша", age=100))
print(greeting(name="Катя", age=16))
