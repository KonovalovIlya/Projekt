# import os
#
# def search(cur_path, file_name, list_=[]):
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         if file_name == i_elem:
#             return list_.append(path)
#         if os.path.isdir(path):
#             result = search(path, file_name)
#     else:
#         result = None
#     return *list_,
#
#
# put = 'C:/Users/Топлог/PycharmProjects/SkillBox/Projekt/'
# file = 'task4.py'
# out = search(put, file)
# for i in out:
#     data = open(i, 'r', encoding='UTF-8')
#     for j in data:
#         print(j)
# print(out)

# import os
#
# def search(cur_path, file_name):
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#         if file_name == i_elem:
#             return path
#         if os.path.isdir(path):
#             result = search(path, file_name)
#             if result:
#                 break
#     else:
#         result = None
#     return result
#
#
# put = 'C:/Users/Топлог/PycharmProjects/SkillBox/Projekt/'
# file = 'numbers.txt'
# summ = 0
# out = search(put, file)
# for i in open(out, 'r'):
#     summ += int(i)
# answer = open('answer.txt', 'w')
# answer.write(str(summ))
# answer.close()


# Работа с файлами, путями.
# import os
#
# def search(cur_path, list_=[]):
#     for i_elem in os.listdir(cur_path):
#         path = os.path.join(cur_path, i_elem)
#
#         if i_elem.endswith('.py'):
#             list_.append(path)
#         if os.path.isdir(path):
#             result = search(path)
#     return list_
#
# dismis = ['.git', '.idea', '.gitignore', 'readme.md']
# put = 'C:/Users/Топлог/PycharmProjects/SkillBox/Projekt/'
# out = search(put)
# print(out)
# for i in out:
#     data = open(i, 'r', encoding='UTF-8').read()
#     script = open('script.txt', 'a', encoding='UTF-8')
#     script.write('\n')
#     script.write(data)
#     script.write('\n')
#     script.write('*' * 40)
#     script.write('\n')
#     script.close()

# 23 урок Ошибки и исключения

BRUCE_WILLIS = 42

input_data = input('Введите строку: ')
try:
    leeloo = int(input_data[4])
except ValueError:
    print('невозможно преобразовать к числу')
except IndexError:
    print('выход за границы списка')

try:
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except:
    print('остальные исключения')
