def extract(collection, list_ = []):
    for i in collection:
        if not isinstance(i, int):
            extract(i, list_)
        else:
            list_.append(i)
    return list_


print(extract([1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]))