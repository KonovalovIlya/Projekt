country_all = int(input('Кол-во стран: '))
country_dict = {}
for country_number in range(1, country_all + 1):
    country_info = input('{} страна: '.format(country_number))
    country_info = country_info.split()
    country_dict[country_number] = {country_info[0]: country_info[1:]}
    # 2 страна: Германия Берлин Лейпциг Мюнхен
print(country_dict)
while True:
    city_number = 1
    city = input('{} город: '.format(city_number))
    for n in range(1, len(country_dict) + 1):
        for country in country_dict[n]:
            if city in country_dict[n][country]:
                print('Город {0} расположен в стране {1}'.format(city, country))
    else:
        print('По городу {} данных нет.'.format(city))
        break
    city_number = 1
#
# 2 город: Мюнхен
# Город Мюнхен расположен в стране Германия.
#
# 3 город: Рим
# По городу Рим данных нет.
