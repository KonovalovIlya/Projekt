import random

tuple_ = tuple(random.randint(0, 10) for _ in range(10))
number = int(input())

if tuple_.count(number) >= 2:
    tuple_1 = tuple_[tuple_.index(number) : tuple_.index(number, tuple_.index(number) + 1, len(tuple_)) + 1]
elif tuple_.count(number) == 1:
    tuple_1 = tuple_[tuple_.index(number):]
elif not number in tuple_:
    tuple_1 = ()
print(tuple_1)