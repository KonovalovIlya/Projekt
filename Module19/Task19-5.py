def dict_rev(string_):
  dict_ = {
    string_.count(symbol): set(j_symbol
                            for j_symbol in string_
                            if string_.count(symbol) == string_.count(j_symbol))
    for symbol in string_
  }
  return dict_


text = input('Введите текст: ')
dict_1 = {
    symbol: text.count(symbol)
    for symbol in text
}
print('Оригинальный словарь частот:')
for key in sorted(dict_1):
    print(key, '-', dict_1[key])

dict_2 = dict_rev(text)
print('Инвертированный словарь частот:')
for key in sorted(dict_2):
    print(key, '-', sorted(dict_2[key]))