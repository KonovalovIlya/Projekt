number = int(input('Сколько чисел: '))
list_1 = []
count = 0
for _ in range(number):
    list_1.append(int(input('Введите число: ')))
while list_1 != list_1[::-1]:
    list_1.insert(number, list_1[count])
    count += 1
print(count)
print(list_1[number::])
