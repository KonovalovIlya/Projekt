list_ = [1, 0, 2, 0, 4, 0, 2, 0, 1]
print(list_)
for i in range(len(list_) - 1):
    for j in range(len(list_) - 1):
        if list_[j] == 0:
            list_[j], list_[j + 1] = list_[j + 1], list_[j]
list_[-(list_.count(0)):]=[]
print(list_)