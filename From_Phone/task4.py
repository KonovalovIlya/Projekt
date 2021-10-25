def guest_in():
    if  len(guests) < 6:
        name = input('Имя: ')
        guests.append(name)
        print('Привет', name)
    else:
        print('Очень жаль, но мест нет')
    start()
def guest_out():
    name = input('Имя: ')
    guests.remove(name)
    start()
def start():
    print(guests)
    answer = input('Пришел новый гость или кто-то ушел: ')
    if answer == 'пришел':
        guest_in()
    elif answer == 'ушел':
        guest_out()
    elif answer == 'пора спать':
        print('Все легли спать')


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

start()
