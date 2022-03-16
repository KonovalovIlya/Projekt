import functools
from collections.abc import Callable


def decorator_with_args_for_any_decorator(*args):
    def dec(decorator):
        @functools.wraps(decorator)
        def wrap(*args, **kwargs):
            print('Переданные арги и кварги в декоратор: {args_kwargs}'.format(
                args_kwargs=args
                # kwargs=**kwargs
            ))
            decorator(arg)
            return
        return wrap
    return dec


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs): # отсюда уже сами!


    def dec(func):
        @functools.wraps(func)
        def wrap(*args, **kwargs):

            func(*args, **kwargs)
        return wrap
    return dec


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)

# Результат:
# Переданные арги и кварги в декоратор: (100, 'рублей', 200, 'друзей') {}
# Привет, Юзер 101
