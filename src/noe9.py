word = list(input('Введите слово: '))
word_string = ''
word_reversed_string = ''
for symbol in word:
    word_string += symbol
word_reversed = word[-1:-len(word)-1:-1]
for symbol in word_reversed:
    word_reversed_string += symbol
if word_reversed_string == word_string:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
