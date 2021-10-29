def is_vowel(symbol):
    vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
    for vowel in vowels:
        if symbol == vowel:
            return True
            
            
string = input('Введите текст: ')
list_vowel = [symbol for symbol in string if is_vowel(symbol)]
print(list_vowel)
print('Длина списка', len(list_vowel))
