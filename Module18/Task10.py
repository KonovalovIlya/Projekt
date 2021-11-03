SHIFT = 25

def cesar_cipher(string, shift):
    cipher_list = [
                   (alphabet[(alphabet.index(symbol) + shift) % len(alphabet)] if symbol in alphabet
                    else alphabet_2[(alphabet_2.index(symbol) + shift) % len(alphabet_2)] if symbol in alphabet_2
                    else symbol)
                   for symbol in string
    ]
    return cipher_list
def shift(list_):
    shift = 3
    string_i = ''
    for word in list_:
        if word.find('(') > -1:
            word_1 = word
            word = ''
            for symbol in word_1:
                if symbol == '(':
                    symbol = '`'
                word += symbol
        for _ in range(shift):
            word = ''.join([word[-1:], word[:-1]])
        string_i = ' '.join([string_i, word])
        if word.endswith('/'):
            shift += 1
    return string_i


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

string_2 = ''
string = input('Введите текст: ').split()
for word in string:
    string_1 = cesar_cipher(word, SHIFT)
    string_2 = ' '.join([string_2, ''.join(string_1)])

string_3 = shift(string_2.split())
print(string_3)
