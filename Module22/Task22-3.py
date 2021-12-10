def is_alpha_function(data, count_alpha = 0):
    if len(data) == 1 and data.isalpha():
        return 1
    elif len(data) == 1 and not data.isalpha():
        return 0
    for item in data:
        rec = is_alpha_function(item, count_alpha)
        count_alpha += rec
    return count_alpha


zen = open('zen.txt', 'r')
is_alpha = 0
is_word = 0
is_string = 0
set_ = set()
list_ = []
for string in zen:
    is_string += 1
    is_alpha += is_alpha_function(string)
    list_ += [
        item if item.isalpha() or "'" in item else ''.join(j for j in item if j.isalpha())
        for item in string.split()
    ]
    set_.update(string)
list_ = [item for item in list_ if len(item) > 0]
is_word += len(list_)
dict_ = {i: 0 for i in sorted(set_) if i.isalpha()}
zen.seek(0)
for string in zen:
    for symbol in string:
        if symbol in dict_.keys():
            dict_[symbol] += 1
is_rare = (j for j, k in dict_.items() if k == min(dict_.values()))
print('Кол-во строк: {string}\nКол-во слов: {word}\nКол-во букв: {alpha}\nСамая редкие буквы: {rare}'.format(
        string= is_string,
        word= is_word,
        alpha= is_alpha,
        rare= (*is_rare,)
    )
)
zen.close()
