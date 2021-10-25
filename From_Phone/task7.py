list_size_roll = []
list_size_feet = []
print('Введите кол-во роликов: ', end='')
amount_roll = int(input())
for number in range(amount_roll):
    print(' Введите размер', number + 1, '-й пары', end=' ')
    size_roll = int(input())
    list_size_roll.append(size_roll)
print('Введите кол-во человек: ', end='')
amount_people = int(input())
for number in range(amount_people):
    print('Введите размер ноги', number + 1, '-го человека', end=' ')
    size_feet = int(input())
    list_size_feet.append(size_feet)
count = 0
for i_feet in list_size_feet:
    for i_roll in list_size_roll:
        if i_roll >= i_feet:
            count += 1
            list_size_roll.remove(i_roll)
        else:
            continue
print('Наибольшее кол-во людей, которые могут взять ролики:', count)