def cesar_cipher(string, shift):
    cipher_list = [
                   (alphabet[(alphabet.index(symbol) + shift) % len(alphabet)] if symbol in alphabet else symbol)
                   for symbol in string
    ]
    return cipher_list



alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
k = 3
string = input('Введите текст: ')
string_2 = cesar_cipher(string, k)
print(*string_2,)
