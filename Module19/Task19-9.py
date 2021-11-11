HIGHT = 0
tree = dict()
peoples = int(input('Введите количество человек: '))
print('Введите имена в виде имя_потомка имя_родителя')
for pair_names in range(1, peoples):
    pair = input('{} пара: '.format(pair_names)).split()
    if not pair[1] in tree.keys():
        tree[pair[1]] = HIGHT
    else:
        tree[pair[1]] = tree[pair[1]]
    tree[pair[0]] = tree[pair[1]] + 1
print('Высота каждого члена семьи:')
for family_member in sorted(tree.keys()):
    print(family_member, tree[family_member])
