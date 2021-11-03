ip_adress = input('Введите IP: ') 
for number in ip_adress.split('.'):
    if not number.isdigit():
#128.16.35.a4
        print('{number} - не целое число'.format(number = ip_adress))
        break
    elif not number <= '255':
#Введите IP: 240.127.56.340
        print('{number} превышает 255'.format(number = number))
        break
    elif not len(ip_adress.split('.')) == 4:
#Введите IP: 34.56.42,5
        print('Адрес - это четыре числа, разделённые точками')
        break
else:
        print('IP-адрес корректен')

