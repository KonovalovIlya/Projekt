import random

number_max = int(input('Введите максимальное число: '))
number_all = set(list(range(1, number_max + 1)))
number_goal = random.randint(1, number_max)
while True:
    number_search = input('Нужное число есть среди вот этих чисел: ')
    if number_search == 'Помогите!':
        print('Артём мог загадать следующие числа: {}'.format(number_all.intersection(number_search)))
        break
    number_search = {int(n) for n in number_search.split()}
    if number_goal in number_search and len(number_search) > 1:
        number_all = number_all.intersection(number_search)
        print('Ответ Артёма: Да')
    elif number_goal == number_search:
        print('Угадал')
        break
    else:
        print('Ответ Артёма: Нет')
        number_all = number_all.difference(number_search)

