def cesar_cipher(symbol):
    if symbol in alfabet:
        if alfabet[alfabet.index(symbol)] < alfabet[30]:
            result = alfabet[alfabet.index(symbol) + 3]
        elif alfabet[alfabet.index(symbol)] == alfabet[30]:
            result = alfabet[0]
        elif alfabet[alfabet.index(symbol)] == alfabet[31]:
            result = alfabet[1]
        elif alfabet[alfabet.index(symbol)] == alfabet[32]:
            result = alfabet[2]
        else:
            result = alfabet[3]
        return result
    else:
        return symbol


alfabet = [
        'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
        'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'
]
k = 4
string = input('Введите текст: ')
string_2 = [cesar_cipher(symbol) for symbol in string]
print(*string_2,)
