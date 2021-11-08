def staff_sum_price(string_):
    pac_price_all = 0
    for pac in range(len(store[string_])):
        pac_price = store[string_][pac]['quantity'] * store[string_][pac]['price']
        pac_price_all += pac_price
    return pac_price_all


def staff_sum(string_):
    pac_all = 0
    for pac in range(len(store[string_])):
        pac_all += store[string_][pac]['quantity']
    return pac_all



goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for staff in goods:
    staff_amount = staff_sum(goods[staff])
    staff_price = staff_sum_price(goods[staff])
    print('{0} - {1} шт, стоимость {2} руб'.format(staff, staff_amount, staff_price))
