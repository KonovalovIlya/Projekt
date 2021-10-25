def player_out(number):
    for i in range(number):
        if i != number - 1:
            players_list.append(players_list[0])
            players_list.remove(players_list[0])
        else:
            n = players_list[0]
        return n


players_number = int(input('Сколько игроков: '))
out = int(input('Число в считалке: '))
print('Значит выбывает тот кто будет', out)
players_list = list(range(1, players_number + 1))
while len(players_list) > 1:
    print('начало отсчета с ', players_list[0])
    print('В игре', sorted(players_list))
    number_out = player_out(out)
    print('Выбывает игрок под номером', number_out)
    players_list.remove(number_out)
print('Остался игрок под номером', players_list[0])
