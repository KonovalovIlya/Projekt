def f_wish_list(film, list_1, list_2):
    true_check = False
    for i_film in list_2:
        if i_film == film:
            true_check = True
            list_1.append(film)
            start()
    if film == 'End':
        print(list_1)
    elif not true_check:
        print('Такого фильма нет')
        start()


def start():
    wish_film = input('Какой фильм хотите посмотреть: ').title()
    f_wish_list(wish_film, wish_list, films)


films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня'
]
wish_list = []
start()
