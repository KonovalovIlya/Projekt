word_count = int(input('Введите количество пар слов: '))
dict_1 = {}
for n in range(word_count):
    string_1 = input('{} пара: '.format(n+1)).title().split(' - ')
    dict_1[string_1[0]] = string_1[1]
while True:
    string_2 = input('Введите слово: ').title()
    if string_2 in dict_1.keys():
        print('Синоним:', *dict_1[string_2],)
    elif string_2 in dict_1.values():
        for key in dict_1.keys():
            if string_2 == dict_1[key]:
                print('Синоним:', key)
    else:
        print('Такого слова в словаре нет.')