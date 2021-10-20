word = list(input('Введите слово: '))
symbols_counts = []
count_unique= 0
for counts in range(len(word)):
    symbols_counts.append(0)
for index in range(len(word)):
    for index_1 in range(len(word)):
        if word[index] == word[index_1]:
            symbols_counts[index] += 1
for number in symbols_counts:
    if number == 1:
        count_unique += 1
print(f'Уникальных букв {count_unique}')
