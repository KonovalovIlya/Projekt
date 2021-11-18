def power(n):

    if n == 1:
        return str(n)
    p = power(int(n)-1)
    return ''.join([str(n), p])



int_num = int(input('Введите числo: '))
d = power(int_num)
print(sorted(d))

