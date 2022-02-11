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
#
# \\Точка с координатамии гетеры и сетеры
#
# class Tochka:
#     __name = ''
#     __x = 0
#     __y = 0
#     def set_name(self, name):
#         self.__name = name
#
#     def set_x(self, x):
#         if isinstance(x, int):
#             self.__x = x
#         else:
#             raise Exception('Координата точки должна быть целым числом')
#
#     def set_y(self, y):
#         if isinstance(y, int):
#             self.__y = y
#         else:
#             raise Exception('Координата точки должна быть целым числом')
#
#     def __init__(self, name, x = 0, y = 0):
#         self.set_name(name)
#         self.set_x(x)
#         self.set_y(y)
#
#     def get_name(self):
#         return self.__name
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#     def __str__(self):
#         return  'Координаты точки {}: {}, {}'.format(self.get_name(), self.get_x(), self.get_y())
#
#
# t = Tochka('t', 5, 7)
# t2 = Tochka('t2', 3, 9)
# print(t.__str__())
# print(t2.__str__())
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# Задача 1. Юниты
#
# Есть базовый класс «Юнит», который определяется количеством здоровья (хитпоинты). У Юнита есть действие
# «получить урон» (базовый класс получает 0 урона).
#
# Также есть два дочерних класса:
#
# Солдат: получает урон, равный переданному значению.
# Обычный гражданин: получает урон, равный двукратному переданному значению.
# Реализуйте родительский и дочерние классы и их методы, используя принцип полиморфизма (а также инкапсуляции и
# наследования, конечно же).
#
# class Unit:
#     def __init__(self, health):
#         self.__health = health
#
#     def hit(self, hit):
#         self.__health -= 0
#
#
# class Soldier(Unit):
#     def __init__(self, health):
#         super().__init__(health)
#         self.set_health(health)
#
#     def set_health(self, number):
#          self.__health = number
#
#     def get_health(self):
#         return self.__health
#
#     def hit(self, hit):
#         health = self.get_health()
#         health -= hit
#         self.set_health(health)
#
#     def __str__(self):
#         return 'У солдата осталось {} здоровья'.format(self.get_health())
#
#
# class Civilian(Unit):
#     def __init__(self, health):
#         super().__init__(health)
#         self.set_health(health)
#
#     def set_health(self, number):
#         self.__health = number
#
#     def get_health(self):
#         return self.__health
#
#     def hit(self, hit):
#         health = self.get_health()
#         health -= hit*2
#         self.set_health(health)
#
#     def __str__(self):
#         return 'У гражданского осталось {} здоровья'.format(self.get_health())
#
#
# s = Soldier(health=10)
# c = Civilian(health=10)
# s.hit(4)
# c.hit(4)
# print(s.__str__())
# print(c.__str__())
#
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#
#Итераторы
# # l = [10, 20, 30]
# # i = iter(l)
# # while True:
# #     try:
# #         print(next(i))
# #     except StopIteration:
#         pass

# Бесконечный итератор
# class СountIterator:
#     count = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         vol = self.count
#         self.count += 1
#         return self.count
#
#
# my_iter = СountIterator()
# for i_elem in my_iter:
#     print(i_elem)
# Случайная сумма
# import random
#
#
# class RandomSum:
#     def __init__(self, number):
#         self.count = 0
#         self.elem_1 = round(random.uniform(0, 1), 2)
#         self.elem_2 = round(random.uniform(0, 1), 2) + self.elem_1
#         self.limit = number
#
#     def __iter__(self):
#         self.count = 0
#         self.elem_1 = round(random.uniform(0, 1), 2)
#         self.elem_2 = round(random.uniform(0, 1), 2) + self.elem_1
#         return self
#
#
#     def __next__(self):
#         if self.count < self.limit:
#             self.elem_1 = self.elem_2
#             self.elem_2 = round(random.uniform(0, 1), 2) + self.elem_1
#             self.count += 1
#             return self.elem_2
#         else:
#             raise StopIteration
#
#
# iter = RandomSum(10)
# for i in iter:
#     print(i)
# print('abra-kadabra')
# for i in iter:
#     print(i)
#
# Генератор
# def gen():
#     c = 0
#     while True:
#         yield c
#         c+=1
#
#
# for i in gen():
#     print(i)
#
# Генератор простых чисел
# def IsPrime(n):
#     if n == 0:
#         return False
#     if n == 1:
#         return True
#     d = 2
#     while n % d != 0:
#         d += 1
#     return d == n
#
# def g_p(number):
#     for i in range(1, number+1):
#         if IsPrime(i):
#             yield i
#
#
# for i in g_p(11):
#     print(i)
#
# ФУНКЦИИ КАК ОБЪЕКТЫ.
# def func_1(x):
#
#     return x + 10
#
# def func_2(func, num):
#     res = func(num)
#     return res*res
#
#
# print(func_1(9))
# print(func_2(func_1, 9))
# import time
#
#
# def timer(func):
#     started = time.time()
#     func()
#     stopped = time.time()
#     time_res = stopped-started
#     return time_res
#
# def sq():
#     num = 100
#     res = 0
#     for _ in range(num + 1):
#         res += sum(i**2 for i in range(10000))
#     return res
#
# print(timer(sq))
#
# ДЕКОРАТОРЫ
#
#
# def decorator(func):
#     def wrapped_func(*arg, **kwarg):
#         func(*arg, **kwarg)
#         func(*arg, **kwarg)
#     return wrapped_func
#
# @decorator
# def greeting(name):
#     print('Привет, {name}!'.format(name=name))
#
#
# greeting('Tom')
#
# import time
#
#
# def timer(func):
#     def wrapped_func(*arg, **kwarg):
#         started = time.time()
#         res = func(*arg, **kwarg)
#         stopped = time.time()
#         time_res = stopped-started
#         print('Func rabotala {} sec'.format(time_res))
#         return res
#     return wrapped_func
#
# @timer
# def sq():
#     num = 100
#     res = 0
#     for _ in range(num + 1):
#         res += sum(i**2 for i in range(10000))
#     return res
#
# my_t = sq()
# print(my_t)
#
#
# def bread(func):
#     def wrapped_func():
#         f = func()
#         return '\t< / ----------\ >\n\t{func}\n\t< \______ / >'.format(func = f)
#     return wrapped_func
#
# def ingred(func):
#     def wrapped_func():
#         f = func()
#         return '\t#помидоры#\n\t{func}\n\t~салат~'.format(func=f)
#     return wrapped_func
#
#
# @bread
# @ingred
# def sandwich():
#     return '--ветчина--'
#
# print(sandwich())
#
# PLAGINS = dict()
#
#
# def register(func):
#     PLAGINS[func.__name__] = func
#     return func
#
# @register
# def hello(name):
#     return 'Hello, {}!'.format(name)
#
# @register
# def baye(name):
#     return 'Goodbaye, {}!'.format(name)
#
# print(PLAGINS)
# print(hello('Tom'))
