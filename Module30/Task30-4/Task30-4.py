import math

def is_prime(x):
    return all(x % y != 0 for y in range(2, int(math.sqrt(x)) + 1))

res_1 = list(filter(lambda x: all (x % y != 0 for y in range (2, int (math.sqrt (x)) + 1)), list(range(2, 1000))))
print(res_1)

res_2 = (list(filter(is_prime, list(range(2, 1000)))))
print(res_2)
