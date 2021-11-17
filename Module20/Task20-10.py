def zip_custom(a,b):
    zipp = ((a[i], b[i]) for i in range(min(len(a), len(b))))
    return zipp


string = 'abcd'
tuple_ = (10, 20, 30, 40)
ziip = zip_custom(string, tuple_)
print(ziip)
for item in ziip:
    print(item)
