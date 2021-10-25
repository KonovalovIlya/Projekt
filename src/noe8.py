string = ['1','2','3','4','5']
string_new = []
k = 2
c = 0
symbol = ''
print(string)
while c != 10:
    if k > 1:
        for symbol in string:
            if symbol != string[-k]:
                string_new.append(symbol)
            else:
                break
        for k_ in range(1, k + 1):
            symbol = string[-k_]
            string_new.insert(0, symbol)
    else:
        for symbol in string:
            if symbol != string[-1]:
                string_new.append(symbol)
            else:
                string_new.insert(0, symbol)
    string = string_new
    print(string)
    string_new = []
    c += 1
