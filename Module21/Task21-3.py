def fibonachchi(number, number_all = (0, 1)):
    if len(number_all) == number+1:
        return number_all[-1]
    number_out = fibonachchi(number, number_all + (number_all[-2] + number_all[-1],))
    return number_out


position = int(input('Введите позицию числа в списке: '))
result = fibonachchi(position)
print(result)
