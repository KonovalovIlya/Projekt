shop = [
    ['каретка', 1200], ['шатун', 1000], ['седло', 300],
    ['педаль', 100], ['седло', 1500],['рама', 12000],
    ['обод', 2000], ['шатун', 200], ['седло', 2700]
]
staff = input('Введите название детали: ')
staff_amount = 0
staff_price = 0
for price_list in shop:
   staff_amount += price_list.count(staff)
   if price_list.count(staff) > 0:
       staff_price += price_list[1]
print('Количество на складе', staff_amount)
print('Общая стоимость', staff_price)
