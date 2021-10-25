def list_count(number, list_, list__):
    list_.extend(list__)
    count = list_.count(number)
    return count
def list_filter(number, list_, count):
    for _ in range(count):
        list_.remove(number)


list_first = [1, 5, 3]
list_second = [1, 5, 1, 5]
list_therd = [1, 3, 1, 5, 3, 3]
number_1 = 5
number_2 = 3
count_5 = list_count(number_1, list_first, list_second)
print(f'Количество цифр 5 при первом объединении: {count_5}')
list_filter(number_1, list_first, count_5)
count_3 = list_count(number_2, list_first, list_therd)
print(f'Количество цифр 3 при втором объединении: {count_3}')
print(list_first)
