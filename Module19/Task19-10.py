s = input()
d = {i: s.count(i) for i in s}
d_v = [j for j in d.values()]
print(d_v)
if d_v.count(1) > 1:
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')
