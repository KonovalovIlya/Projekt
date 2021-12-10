summ = 0
numbers = open('numbers.txt', 'w')
numbers.write('  2\n 2\n2\n   2')
numbers.close()
numbers = open('numbers.txt', 'r')
for string in numbers:
    for symbol in string:
        if symbol.isdigit():
            summ += int(symbol)
numbers.close()
answer = open('answer.txt', 'w')
answer.write(str(summ))
answer.close()