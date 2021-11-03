string = input('Введите текст: ')
word = ''
string_r = ''
for symbol in string:
    if symbol.isalpha():
        word += symbol
    else:
        string_r = ''.join([string_r, word[::-1], symbol])
        word = ''
print(string_r)