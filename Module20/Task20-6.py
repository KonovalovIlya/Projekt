import random


list_ = [random.randint(0, 9) for _ in range(10)]
list_01 = []
for i in range(1, len(list_), 2):
    list_01.append((list_[i-1], list_[i]))
list_[:] = list_01
print(list_)

list_1 = [random.randint(0, 9) for _ in range(10)]
list_1 = [(list_1[i-1], j) for i, j in enumerate(list_1) if not i % 2 == 0]
print(list_1)
