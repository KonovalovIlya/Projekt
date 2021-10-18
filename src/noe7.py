def magic_years(number_1, number_2):
    for year in range(number_1, number_2+1):
        symbol_1 = year // 1000
        symbol_2 = year // 100 % 10
        symbol_3 = year // 10 % 10
        symbol_4 = year % 10
        if symbol_1 == symbol_2 == symbol_3:
            print(year)
        elif symbol_2 == symbol_3 == symbol_4:
            print(year)
        elif symbol_1 == symbol_2 == symbol_4:
            print(year)
        elif symbol_1 == symbol_3 == symbol_4:
            print(year)


number_1 = int(input())
number_2 = int(input())

magic_years(number_1, number_2)
