import functools


def counter(func):
    @functools.wraps(func)
    def wrapped(*args, count = 0):
        func(*args)

        with open('counter', 'a') as file:
            file.write('1\n')
        with open('counter', 'r') as file:
            for i in file:
                count += 1
        print('Функция вызывалась {} раз'.format(count))

    return wrapped


@counter
def test():
    print('<Тут что-то происходит...>')






test()
test()
test()