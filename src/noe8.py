string = ['1','2','3','4','5']
k = 1
c = 0
symbol = ''
print(string)
while c != 10:
    delete_item = len(string)
    if k > 1:
        for _ in range(k):
            symbol = string[len(string) - 1]
            string.insert(0, symbol)
            string.__delitem__(delete_item)
    else:
        symbol = string[len(string) - 1]
        string.insert(0, symbol)
        string.__delitem__(delete_item)
    print(string)
    c += 1