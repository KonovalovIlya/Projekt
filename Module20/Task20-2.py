def sort(data):
    return is_prime(data)


def is_prime(data_):
    list_ = []
    if isinstance(data_, list):
        for n, j in enumerate(data_):
            if n < 2:
                pass
            elif n == 2:
                list_.append(j)
            elif n % 2 == 0:
                pass
            else:
                list_.append(j)
    elif isinstance(data_, str):
        for n, j in enumerate(data_):
            if n < 2:
                pass
            elif n == 2:
                list_.append(j)
            elif n % 2 == 0:
                pass
            else:
                list_.append(j)
    elif isinstance(data_, set):
        for n, j in enumerate(data_):
            if n < 2:
                pass
            elif n == 2:
                list_.append(j)
            elif n % 2 == 0:
                pass
            else:
                list_.append(j)
    elif isinstance(data_, tuple):
        for n, j in enumerate(data_):
            if n < 2:
                pass
            elif n == 2:
                list_.append(j)
            elif n % 2 == 0:
                pass
            else:
                list_.append(j)
    elif isinstance(data_, dict):
        for n, j in enumerate(data_):
            if n < 2:
                pass
            elif n == 2:
                list_.append({j: data_.get(j)})
            elif n % 2 == 0:
                pass
            else:
                list_.append({j: data_.get(j)})
    return list_


data = {9649: 0, 9661: 1, 9677: 2, 9679: 3, 9689: 4, 9697: 5}

new_data = sort(data)
print(new_data)