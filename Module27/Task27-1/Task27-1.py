def how_are_you(func):
    def wrapped():
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        return func()
    return wrapped

@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()