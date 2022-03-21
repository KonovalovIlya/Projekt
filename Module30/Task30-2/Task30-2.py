import timeit


res: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print('res', res)
res_2 = timeit.timeit('list(map(lambda x: str(x) + "-", list(range(100))))', number=10000)
print('res_2', res_2)
res_3 = timeit.timeit('[str(i) + "-" for i in range(100)]', number=10000)
print('res_3', res_3)
