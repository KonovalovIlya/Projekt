import functools
from collections.abc import Callable


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    @functools.wraps(decorator)
    def wrap(*args, **kwargs):
        print('Переданные арги и кварги в декоратор: {args_kwargs}'.format(
            args_kwargs=args
        ))
        return decorator(args)
    return wrap


@decorator_with_args_for_any_decorator
def decorated_decorator(*args, **kwargs) -> Callable:
    def dec(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrap(*args, **kwargs):
            func(*args, **kwargs)
            return
        return wrap
    return dec


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)

# Результат:
# Переданные арги и кварги в декоратор: (100, 'рублей', 200, 'друзей') {}
# Привет, Юзер 101
