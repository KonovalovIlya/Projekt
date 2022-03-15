import functools

class Ex1:
    def get(self, data = ''):
        if data == '//':
            return example
        else:
            return None



def callback(path):
    def dec(func):
        @functools.wraps(func)
        def wrapped(*arg, **kwarg):
           return func()
        return wrapped
    return dec

@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

app = Ex1()
route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')


