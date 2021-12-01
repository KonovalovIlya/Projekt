def order(number_):
    if number_ == 1:
        return (number_,)
    number_ordered = order(number_-1)
    return (*number_ordered,) + (number_,)


number = int(input('Введите число: '))
result = order(number)
print(result)
