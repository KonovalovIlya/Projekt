SHIFT = 25


def cesar_cipher(string_, shift_):
    cipher_list = [
                   (alphabet[(alphabet.index(symbol) + shift_) % len(alphabet)] if symbol in alphabet
                    else alphabet_2[(alphabet_2.index(symbol) + shift_) % len(alphabet_2)] if symbol in alphabet_2
                    else symbol)
                   for symbol in string_
    ]
    return cipher_list


def shift(list_):
    shift_ = 3
    string_i = ''
    for word_ in list_:
        if word_.find('(') > -1:
            word_1 = word_
            word_ = ''
            for symbol in word_1:
                if symbol == '(':
                    symbol = '`'
                word_ += symbol
        for _ in range(shift_):
            word_ = ''.join([word_[-1:], word_[:-1]])
        string_i = ' '.join([string_i, word_])
        if word_.endswith('/'):
            shift_ += 1
    return string_i


alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

string_1 = ''
string = input('Введите текст: ').split()
for word in string:
    string = cesar_cipher(word, SHIFT)
    string_1 = ' '.join([string_1, ''.join(string)])

string_1 = shift(string_1.split())
print(string_1)
