friends = int(input('Кол-во друзей: '))
debts = int(input('Кол-во расписок: '))
debts_list = []
balance = []
for i_friends in range(friends):
    balance.append(list(range(i_friends+1, i_friends+2)))
    balance[i_friends].append(0)
for number in range(debts):
    debts_list.append(list(range(number,-number)))
    hum_for = int(input('Кому: '))
    hum_from = int(input('От кого: '))
    summ = int(input('Сколько: '))
    debts_list[number].insert(number, hum_for)
    debts_list[number].insert(number + 1, hum_from)
    debts_list[number].insert(number + 2, summ)
for i in range(friends):
    for i_2 in range(debts):
        if debts_list[i_2][0] == balance[i][0]:
            balance[i][1] -= debts_list[i_2][2]
        if debts_list[i_2][1] == balance[i][0]:
            balance[i][1] += debts_list[i_2][2]
print('Баланс друзей')
for number in range(friends):
    print(balance[number][0], ':', balance[number][1])
