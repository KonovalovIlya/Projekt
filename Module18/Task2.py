string = 'Надо отнести кольцо в Мордор'
len_word_max = 0
word_max = ''
for word in string.split():
    if len(word) > len_word_max:
        len_word_max = len(word)
        word_max = word
print('Самое длинное слово: {0}. Его длина: {1}'.format(word_max, len_word_max))