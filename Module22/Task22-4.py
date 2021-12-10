import os

def search(cur_path):
    for i_elem in os.listdir(cur_path):
        path_ = os.path.join(cur_path, i_elem)

        if os.path.isfile(path_):
            path_
        if os.path.isdir(path_):
            result = search(path_)
    return list_


catalog = 'Module21\Task21-1'
out = search_function(catalog)
if out:
    print(out)
else:
    print('Такого ключа нет')