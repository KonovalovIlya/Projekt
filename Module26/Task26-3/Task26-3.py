import os


def gen_files_path(cur_path, dir_name):
    # start = 'C:\\'
    try:
        for i in os.listdir(cur_path):
            if i.startswith('$') or  i.startswith('.'):
                pass
            else:
                path = os.path.join(cur_path, i)
                if os.path.isdir(path):
                    if i == dir_name:
                        r = gen(path)
                        print(list(r))

                    res = gen_files_path(path, dir_name)




    except PermissionError:
        pass



def gen(cur_path):
    for j in os.listdir(cur_path):
        yield j





dir_name = 'Module22'
cur_path = 'C:/Users/Топлог/PycharmProjects/SkillBox'
a = gen_files_path(cur_path, dir_name)
