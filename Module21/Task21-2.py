def merge(data_a, data_b, item = 0):
    if isinstance(data_a, dict):
        data_a_ = tuple(data_a.items())
        if item == min(len(data_a), len(data_b)) -1:
            return ((*data_a_[item], data_b[item]),)
        merged_data = merge(data_a, data_b, item + 1)
        return ((*data_a_[item], data_b[item]),) + (*merged_data,)
    elif isinstance(data_b, dict):
        b_ = tuple(data_b.items())
        if item == min(len(data_a), len(data_b)) -1:
            return ((data_a[item], *b_[item]),)
        merged_data = merge(data_a, data_b, item + 1)
        return ((data_a[item], *b_[item]),) + (*merged_data,)
    else:
        if item == min(len(data_a), len(data_b)) -1:
            return ((data_a[item], data_b[item]),)
        merged_data = merge(a, data_b, item + 1)
        return ((data_a[item], data_b[item]),) + (*merged_data,)
    
    
string = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
tuple_ = (10, 20, 30, 40, 50)
merged = merge(tuple_, string)
print(merged)
for item in merged:
    print(item)
