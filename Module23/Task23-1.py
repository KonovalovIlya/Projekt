# Есть файл people.txt, в котором построчно хранится N имён пользователей.
#
# Напишите программу, которая берёт количество символов в каждой строке файла и в качестве ответа выводит
# общую сумму. Если в какой-либо строке меньше трёх символов (не считая литерала \n), то вызывается ошибка
# и сообщение, в какой именно строке ошибка возника. Программа при этом не завершается и обрабатывает все имена файла.
#
# Также при желании можно вывести все ошибки в отдельный файл errors.log.

def f(file):
    line_count = 0
    s_count = 0
    for string in file:
        line_count += 1
        line_length = len(string)
        if string.endswith('\n'):
            line_length -= 1
            try:
                if line_length < 4:
                    raise BaseException()
            except BaseException:
                print('Длина {} строки меньше 4-х символов'.format(line_count))
                with open('errors.log', 'a', encoding='UTF-8') as errors:
                    errors.write('Длина {} строки меньше 4-х символов\n'.format(line_count))
        s_count += line_length
    print(s_count)


text = open('people.txt', 'r')
f(text)
text.close()
