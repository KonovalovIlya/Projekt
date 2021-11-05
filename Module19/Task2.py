country_all = int(input('Кол-во стран: '))
country_dict = {}

for country_number in range(1, country_all + 1):
    country_info = input('{} страна: '.format(country_number))
    country_info = country_info.split()
    country_dict[country_number] = {country_info[0]: country_info[1:]}

city_number = 0

while True:
    city_number += 1
    true_chek = False
    city = input('{} город: '.format(city_number))
    for n in country_dict:
        for country in country_dict[n]:
            if city in country_dict[n][country]:
                true_chek = True
                print('Город {0} расположен в стране {1}'.format(city, country))
    if not true_chek:
        print('По городу {} данных нет.'.format(city))
        break
