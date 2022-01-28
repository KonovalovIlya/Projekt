import os


def gen_files_path(cur_path, dir_name):
    # start = 'C:\\'
    for i in os.listdir(cur_path):
        path = os.path.join(cur_path, i)
        if os.path.isdir(path) and i == dir_name:
            for j in os.listdir(path):
                    yield os.path.join(i, j)
        elif os.path.isdir(path):
            cur_path = path
            res = gen_files_path(cur_path, dir_name)

        else:
            pass







dir_name = 'Module22'
cur_path = 'C:\\'
# a = gen_files_path(start, t)
for i in gen_files_path(cur_path, dir_name):
        print(i)