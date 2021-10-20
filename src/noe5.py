def f_wish_list(wish_film, wish_list):
    true_check = False
    for film in films:
        if film == wish_film:
            wish_list.append(film)
            true_check = True
            start()
    if wish_film == 'End':
        print(wish_list)
    elif true_check != True:
        print('Такого фильма нет')
        start()

def start():
    wish_film = input('Какой фильм хотите посмотреть: ').title()
    f_wish_list(wish_film, wish_list)


films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', \
         'Город грехов', 'Мементо', 'Отступники', 'Деревня']
wish_list = []
start()
