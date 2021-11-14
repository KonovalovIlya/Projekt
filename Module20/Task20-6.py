import random


list_ = [random.randint(0, 9) for _ in range(10)]
list_1 = []
for i, j in enumerate(list_):
    if not i % 2 == 0:
        list_1.append((list_[i-1], list_[i]))
list_[:] = list_1
print(list_)

list_ = [random.randint(0, 9) for _ in range(10)]
list_1 = []
for i, j in enumerate(list_):
    if not i % 2 == 0:
        list_.insert(i-1, (list_[i-1], j))
        list_.pop(i)
sorted(list_)
list_ = list_[:9]
print(list_)
# print(list_1)
