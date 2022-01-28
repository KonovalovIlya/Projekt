import os

def size_function(cur_path, size_dir = 0):
    for i_elem in os.listdir(cur_path):
        path_ = os.path.join(cur_path, i_elem)
        if os.path.isfile(path_):
            size_dir += os.path.getsize(path_)
        if os.path.isdir(path_):
            result = size_function(path_)
            size_dir += result
    return size_dir


catalog = 'C:/Users/Топлог/PycharmProjects/SkillBox/Projekt'
out = size_function(catalog)
if out:
    out = int(out / 1024)
    print('Размер каталога {} KB'.format(out))
else:
    print('Ошибка')
