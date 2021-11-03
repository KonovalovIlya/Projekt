string = input('Введиите строку: ')
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2d1'
string_1 = ''
while string != '':
    string_1 = ''.join([string_1, string[0], str(len(string) - len(string.strip(string[0])))])
    string = string.strip(string[0])
print(string_1)
