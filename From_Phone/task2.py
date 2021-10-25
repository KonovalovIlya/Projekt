def list_merge_sorted(list_):
    for number in list_:
        if list_.count(number) > 1:
            list_.remove(number)
        print(sorted(list_))


class_first = list(range(160, 176, 2))
class_second = list(range(162, 180, 3))
class_first.extend(class_second)

list_merge_sorted(class_first)
