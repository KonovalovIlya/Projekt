import re


text = ['9999999999', '999999-999', '99999x9999']

for i in text:
    pattern = re.search(r'\b[8, 9]\d{9}\b', i)
    if pattern:
        if pattern.group() == i:
            print('{num} номер: всё в порядке'.format(num=text.index(i) + 1))
    else:
        print('{num} номер: не подходит'.format(num=text.index(i) + 1))