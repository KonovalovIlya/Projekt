import random

list_1 = [round(random.uniform(5.0, 10.0), 2) for _ in range(20)]
list_2 = [round(random.uniform(5.0, 10.0), 2) for _ in range(20)]
list_3 = [(list_1[i] if list_1[i] > list_2[i] else list_2[i]) for i in range(20)]
print('Первая команда: ', list_1)
print('\nВторая команда: ', list_2)
print('\nПобедители', list_3)
print(len(list_3))
        