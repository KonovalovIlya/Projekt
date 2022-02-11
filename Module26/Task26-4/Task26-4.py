# class Q:
#     def __init__(self, list_):
#         self.list_ = list_[:]
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.list_ == [1,1]:
#             q = self.list_[-self.list_[-1]] + self.list_[-self.list_[-2]]
#             self.list_.append(q)
#             return q
#         else:
#             return self.list_
from typing import List


def Q(list_: List, range_: int)->List:
    if list_ == [1,1]:
        for _ in range(range_):
            q = list_[-list_[-1]] + list_[-list_[-2]]
            list_.append(q)
            yield q
    else:
            yield list_


d=Q([1, 2], 10)
print(list(d))
