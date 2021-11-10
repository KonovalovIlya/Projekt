# Введите количество человек: 9
# 1 пара: Alexei Peter_I
# 2 пара: Anna Peter_I
# 3 пара: Elizabeth Peter_I
# 4 пара: Peter_II Alexei
# 5 пара: Peter_III Anna
# 6 пара: Paul_I Peter_III
# 7 пара: Alexander_I Paul_I
# 8 пара: Nicholaus_I Paul_I
#
# “Высота” каждого члена семьи:
# Alexander_I 4
# Alexei 1
# Anna 1
# Elizabeth 1
# Nicholaus_I 4
# Paul_I 3
# Peter_I 0
# Peter_II 2
# Peter_III 2
tree = dict()
peoples = int(input('Введите количество человек: '))
print('Введите имена в виде имя_потомка имя_родителя')
hight = 0
for pair_names in range(1, peoples):
    pair = input('{} пара: '.format(pair_names)).split()
    if tree[pair[0]] = hight + 1
    tree[pair[1]] = hight
for i in tree:
    print(i, tree[i])