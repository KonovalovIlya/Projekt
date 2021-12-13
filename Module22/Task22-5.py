import os

def safe_function(text):
    path_ = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ').split()
    path_ = '/'.join(path_)
    if not os.path.isfile(os.path.abspath(path_)):
        file_name = input('Введите имя файла: ') + '.txt'
        path_ = os.path.join(path_, file_name)
        if os.path.isfile(path_):
            if input('Вы действительно хотите перезаписать файл?').upper() == 'ДА':
                file = open(path_, 'w')
                file.write(text)
                file.close()
                print('Файл успешно перезаписан!')
            else:
                safe_function(text)
        else:
            file = open(file_name, 'w')
            file.write(text)
            file.close()
            print('Файл успешно сохранён!')
    else:
        print('Не верно указан каталог')
        safe_function(text)


text = input('Введите текст: ')
safe_function(text)