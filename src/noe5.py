films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', \
         'Город грехов', 'Мементо', 'Отступники', 'Деревня']

wl = []
for film in films:
    wf = input('Какой фильм хотите посмотреть: ')
    if film == wf:
        wl.append(film)
        
    else:
        print('Такого фильма нет')
print(wl)