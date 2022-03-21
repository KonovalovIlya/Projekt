import collections


def can_be_poly(data):
    if not False in map(lambda x : x <= 2, collections.Counter(data).values()):
            return True
    else:
            return False


print(can_be_poly('ababc'))

print(can_be_poly('abbbc'))
