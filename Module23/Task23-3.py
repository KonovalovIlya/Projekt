import random


summ_total = 0
errors = [TypeError, TabError, TimeoutError, FileExistsError, FileNotFoundError]
with open('File.txt', 'a') as file_:
    while summ_total < 777:
        number = input('Ведите число: ')
        if random.choices((False, True), (1, 1/13))[0]:
            raise random.choice(errors)
        file_.write(number)
        file_.write('\n')
        summ_total += int(number)
