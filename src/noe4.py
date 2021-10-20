card_list_old = []
card_list_new = []
card_number = int(input('Кол-во видеокарт: '))
for number in range(1, card_number + 1):
    card_seria = int(input(f'{number} Видеокарта: '))
    card_list_old.append(card_seria)

for card_seria in card_list_old:
    if card_seria < 3090:
        card_list_new.append(card_seria)
print(f'Старый список видеокарт: {card_list_old}')
print(f'Новый список видеокарт: {card_list_new}')
