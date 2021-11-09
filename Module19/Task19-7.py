orders = int(input('Введите кол-во заказво: '))
order_dict = {}
for number in range(1, orders + 1):
    order = input('{} заказ: '.format(number)).split()
    if order[0] in order_dict.keys() and not order[1] in order_dict[order[0]].keys():
        order_dict[order[0]][order[1]] = int(order[2])
    elif order[0] in order_dict.keys() and order[1] in order_dict[order[0]].keys():
        order_dict[order[0]][order[1]] += int(order[2])
    else:
        order_dict[order[0]] = {order[1]: int(order[2])}
for client in sorted(order_dict.keys()):
    print('{}:'.format(client))
    for pizza in sorted(order_dict[client].keys()):
        print('\t{0}: {1}'.format(pizza, order_dict[client][pizza]))
