def zip_custom(a,b, i = 0):
    if isinstance(a, dict):
        a_ = tuple(a.items())
        if i == min(len(a), len(b)) -1:
            return ((*a_[i], b[i]),)
        zipp = zip_custom(a,b, i+1) 
        return ((*a_[i], b[i]),) + (*zipp,)
    elif isinstance(b, dict):
        b_ = tuple(b.items())
        if i == min(len(a), len(b)) -1:
            return ((a[i], *b_[i]),)
        zipp = zip_custom(a,b, i+1) 
        return ((a[i], *b_[i]),) + (*zipp,)
    else:
        if i == min(len(a), len(b)) -1:
            return ((a[i], b[i]),)
        zipp = zip_custom(a,b, i+1) 
        return ((a[i], b[i]),) + (*zipp,)
    
    
string = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
tuple_ = (10, 20, 30, 40, 50)
ziip = zip_custom(tuple_, string)
print(ziip)
for item in ziip:
    print(item)
