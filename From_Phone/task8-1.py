def player_out(list_1, number, list_2):
    for i in range(number):
        print(list_1[i])
    for j in range(number):
        if j != number - 1:
            list_2.append(list_2[0])
            list_2.remove(list_2[0])
        else:
            n = list_2[0]
    return n


players_number = int(input('Сколько игроков: '))
counting_rhime = input('Напишите считалку: ')
counting_rhime_list = []
word = ''
for sym in counting_rhime:
    if sym != ' ':
        word += sym
    elif sym == ' ':
        counting_rhime_list.append(word)
        word = ''
counting_rhime_list.append(word)
out = len(counting_rhime_list)
print('Значит выбывает тот кто будет', out)
players_list = list(range(1, players_number + 1))
while len(players_list) > 1:
    print('начало отсчета с ', players_list[0])
    print('В игре', sorted(players_list))
    number_out = player_out(counting_rhime_list, out, players_list)
    print('Выбывает игрок под номером', number_out)
    players_list.remove(number_out)
print('Остался игрок под номером', players_list[0])
