# Пользователь вводит число N. Напишите программу, которая генерирует последовательность из квадратов чисел
# от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так далее). Реализацию напишите тремя способами:
# класс-итератор, функция-генератор и генераторное выражение.
class Iterator:
    def __init__(self, number):
        self.count = 0
        self.value = 1
        self.limit = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            res = self.value ** 2
            self.value += 1
            self.count += 1
            return res
        else:
            raise StopIteration


def gen_sq_func(number):
    for i in range(1, number + 1):
        yield i ** 2


iterator = Iterator(10)
for i in iterator:
    print(i)
print('_______________________')
for i in gen_sq_func(10):
    print(i)
print('_______________________')
number = 10
gen = (i**2 for i in range(1, number + 1))
for i in gen:
    print(i)
