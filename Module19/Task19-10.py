string = input()
dict_ = {i: string.count(i) for i in string}
dict_values = [value for value in dict_.values()]
print(dict_values)
if dict_values.count(1) > 1:
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')
