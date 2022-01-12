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
#
# BRUCE_WILLIS = 42
#
# input_data = input('Введите строку: ')
# try:
#     leeloo = int(input_data[4])
# except ValueError:
#     print('невозможно преобразовать к числу')
# except IndexError:
#     print('выход за границы списка')
#
# try:
#     result = BRUCE_WILLIS * leeloo
#     print(f'- Leeloo Dallas! Multi-pass № {result}!')
# except:
#     print('остальные исключения')

# \\Точка с координатамии счетчиком точек

# class Tochka:
#     count = 0
#     def __init__(self, name, x = 0, y = 0):
#         self.name = name
#         self.x = x
#         self.y = y
#         Tochka.count += 1
#
#     def info(self):
#         print('Координаты точки {}: {}, {}'.format(self.name, self.x, self.y))
#
#
# t = Tochka('t', 5, 7)
# t2 = Tochka('t2', 3, 9)
# t.info()
# t2.info()
# print(Tochka.count)

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# \\Весёлая ферма
# Для игры «Весёлая ферма» необходимо прописать два класса: класс «Картошка» и класс «Грядка картошки».
#
# У картошки есть её номер в грядке, а также стадия зрелости. Она может предоставлять информацию о своей зрелости и расти.
# Всего у картошки может быть четыре стадии зрелости.
#
# Грядка с картошкой содержит список картошки, которая на ней растёт, и может, собственно, взращивать всю эту картошку,
# а также предоставлять информацию о зрелости всей картошки на своей территории.
#
# Реализуйте оба класса и проверьте их работу: создайте экземпляр грядки из пяти картошек и три раза взрастите грядку.
#
# class Kartoshka:
#     staddii_zrelosti = {0: 'Pusto', 1: 'Rostok', 2: 'Zelenaya', 3: 'Sozrela'}
#
#     def __init__(self, nomer):
#         self.nomer = nomer
#         self.zrelost = 0
#
#
#     def rost(self):
#         if self.zrelost < 3:
#             self.zrelost += 1
#         self.info()
#
#
#     def info(self):
#         print('Kartoshka {} - {}'.format(self.nomer, Kartoshka.staddii_zrelosti[self.zrelost]))
#
#     def sozrela(self):
#         if self.zrelost == 3:
#             return True
#         return False
#
#
# class Gradka:
#     def __init__(self, colvo):
#         self.kartoshki = [Kartoshka(nomer) for nomer in range(1, colvo+1)]
#
#     def virashivanie(self):
#         print('Kartoshka rastet')
#         for i_kartoshka in self.kartoshki:
#             i_kartoshka.rost()
#     def vse_sozrelo(self):
#         if not all([i_kartoshka.sozrela() for i_kartoshka in self.kartoshki]):
#                 print('Kartoshka eshe ne sozrela')
#         else:
#             print('Vsya kortoshka sozrela')
#
#
# moya_gryadka = Gradka(5)
# moya_gryadka.vse_sozrelo()
# for _ in range(3):
#     moya_gryadka.virashivanie()
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def sort(list):
    sort = True
    while sort:
        sort = False
        for i in range(len(list) - 1):
            if list[i] < list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                sort = True
    return list

print(sort([1,5,8,3,9,4,1,3,6]))