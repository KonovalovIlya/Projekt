import itertools

res = itertools.product(list(range(10)), repeat=4)
for i in res:
    print(i)