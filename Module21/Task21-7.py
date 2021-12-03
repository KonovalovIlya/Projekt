def sum_(collection, list_ = [], summary = 0):
    for i in collection:
        if not isinstance(i, int):
            sum_(i, list_)
        else:
            list_.append(i)
    for i in list_:
        summary += i
    return summary


print('Ответ', sum_([[1, 2, [3]], [1], 3]))
