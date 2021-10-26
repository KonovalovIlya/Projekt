number = int(input('Сколько чисел: '))
list_1 = []
list_2 = []
count = 0
answer = ''
for _ in range(number):
    list_1.append(int(input('Введите число: ')))
list_2.extend(list_1)
list_2.reverse()
if list_1 != list_2:
    while list_1 != list_2:
        list_1.insert(number, list_1[count])
        list_2.insert(0+count, list_1[count])
        count += 1
    for i in range(count):
        answer = str(list_2[i]) + ' ' + answer
    print(count)
    print(answer)
else:
    print('Последовательность Симметрична')

