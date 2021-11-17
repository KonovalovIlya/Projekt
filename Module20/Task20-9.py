MIN_LENGTH = 3
WINNERS = 3


def sorted_custom(list_):
    return list_[1][0] * 100 - list_[1][1]


players = int(input('Сколько игроков в игре: '))
while players < MIN_LENGTH:
    print('Минимальное кол-во игроков - 3.')
    players = int(input('Сколько игроков в игре: '))
length = int(input('Сколько записей вносится в протокол? '))
player_info = {}
print('Записи (результат и имя):')
for number in range(length):
    string = input('{} запись: '.format(number + 1)).split()
    while len(string) != 2:
        print('Данные введены неверно.')
        string = input('{} запись: '.format(number + 1)).split()
    score, name = string
    score = int(score)
    if name in player_info:
        if score > player_info.get(name)[0]:
            player_info[name] = score, number
    else:
        player_info[name] = score, number
player_info = sorted(list((i, j) for i, j in player_info.items()) , key = sorted_custom, reverse = True)
print('\nИтоги соревнований:')
for position in range(WINNERS):
    print('{position}-е место. {name} ({score})'.format(
        position = position + 1,
        name = player_info[position][0],
        score = player_info[position][1][0]
    ))
