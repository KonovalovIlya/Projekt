tuple_ = (1,2,3,4,6,5,4,3,2,2,1)

string = str(tuple_).replace('(', '', 1).replace(')', '', 1).split(', ')
string = ''.join(string)
if string.isdigit():
    print(tuple(sorted(tuple_)))
else:
    print(tuple_)
