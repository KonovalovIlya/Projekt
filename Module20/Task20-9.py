# Сколько записей вносится в протокол? 9
# Записи (результат и имя):
# 1 запись: 69485 Jack
# 2 запись: 95715 qwerty
# 3 запись: 95715 Alex
# 4 запись: 83647 M
# 5 запись: 197128 qwerty
# 6 запись: 95715 Jack
# 7 запись: 93289 Alex
# 8 запись: 95715 Alex
# 9 запись: 95715 M
#
# Итоги соревнований:
# 1 место. qwerty (197128)
# 2 место. Alex (95715)
# 3 место. Jack (95715)

dict_length = int(input('Сколько записей вносится в протокол? '))
dict_player_info = {}
max_score = 0
print('Записи (результат и имя):')
for number in range(dict_length):
    player_info = input('{} запись: '.format(number)).split()
    if int(player_info[0]) > max_score:
        dict_player_info[player_info[1]] = (player_info[0])
        max_score = int(player_info[0])
print(dict_player_info)
# dict_player_info = [[i, j] for i, j in dict_player_info.items()]
# print(dict_player_info)
# for i, j in enumerate(dict_player_info):
#     if j[1].index(max(j)) == 0:
#         dict_player_info.insert(0, j)
#     elif j[1].index(max(j)) == 0 :
#         dict_player_info.insert(0, j)
#             win_list.insert(len(win_list), tuple((i, max(j))))
#     if j.index(max(j)) == 1:
#         win_list.insert(1, tuple((i, max(j))))
#     if j.index(max(j)) == 2:
#         win_list.insert(2, tuple((i, max(j))))
# print(win_list)