phonebook = dict()
while True:
    if len(phonebook) == 0:
        print('Здесь пока нет контактов')
    print('Что нужно делать: «Поиск человека по фамилии» или «Добавить контакт»?')
    operation = input().lower()
    if operation == 'поиск человека по фамилии' or operation == 'поиск':
        surname = input('Введите фамилию контакта: ').upper()
        for i, j in phonebook.items():
            if surname in i:
                print(*i, '-', j)
            else:
                print('Ничего не найдено')
    elif operation == 'добавить контакт':
        contact_id = input('Введите имя и фамилию контакта: ').upper().split()
        contact_phone_number = int(input('Введите номер телефона: '))
        phonebook[(contact_id[0], contact_id[1])] = contact_phone_number