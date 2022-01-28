def Q(list_):
    res = list_ - list_[-1] + (list_ - list_[-2])
    print(res)

Q([1, 1])