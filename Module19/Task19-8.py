# Пример реализации:
# Введите максимальное число: 10
#
# Нужное число есть среди вот этих чисел: 1 2 3 4 5
# Ответ Артёма: Да
#
# Нужное число есть среди вот этих чисел: 2 4 6 8 10
# Ответ Артёма: Нет
#
# Нужное число есть среди вот этих чисел: Помогите!
# Артём мог загадать следующие числа: 1 3 5
#
import numbers
import random

number_max = int(input('Введите максимальное число: '))
number_all = set(list(range(1, number_max + 1)))
number_goal = set(random.randint(1, number_max) for _ in range(random.randint(1, number_max // 2)))
print(number_goal)
while True:
    number_search = input('Нужное число есть среди вот этих чисел: ')
    if number_search == 'Помогите!':
        print('Артём мог загадать следующие числа: {}'.format(number_goal))
        break
    number_search = {int(n) for n in number_search.split()}
    j = number_search.intersection(number_goal)
    if number_goal in number_search.intersection(number_goal):
        print('Ответ Артёма: Да')
    else:
        print('Ответ Артёма: Нет')


