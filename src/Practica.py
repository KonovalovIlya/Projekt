# # import os
# #
# # def search(cur_path, file_name, list_=[]):
# #     for i_elem in os.listdir(cur_path):
# #         path = os.path.join(cur_path, i_elem)
# #         if file_name == i_elem:
# #             return list_.append(path)
# #         if os.path.isdir(path):
# #             result = search(path, file_name)
# #     else:
# #         result = None
# #     return *list_,
# #
# #
# # put = 'C:/Users/Топлог/PycharmProjects/SkillBox/Projekt/'
# # file = 'task4.py'
# # out = search(put, file)
# # for i in out:
# #     data = open(i, 'r', encoding='UTF-8')
# #     for j in data:
# #         print(j)
# # print(out)
#
# # import os
# #
# # def search(cur_path, file_name):
# #     for i_elem in os.listdir(cur_path):
# #         path = os.path.join(cur_path, i_elem)
# #         if file_name == i_elem:
# #             return path
# #         if os.path.isdir(path):
# #             result = search(path, file_name)
# #             if result:
# #                 break
# #     else:
# #         result = None
# #     return result
# #
# #
# # put = 'C:/Users/Топлог/PycharmProjects/SkillBox/Projekt/'
# # file = 'numbers.txt'
# # summ = 0
# # out = search(put, file)
# # for i in open(out, 'r'):
# #     summ += int(i)
# # answer = open('answer.txt', 'w')
# # answer.write(str(summ))
# # answer.close()
#
#
# # Работа с файлами, путями.
# # import os
# #
# # def search(cur_path, list_=[]):
# #     for i_elem in os.listdir(cur_path):
# #         path = os.path.join(cur_path, i_elem)
# #
# #         if i_elem.endswith('.py'):
# #             list_.append(path)
# #         if os.path.isdir(path):
# #             result = search(path)
# #     return list_
# #
# # dismis = ['.git', '.idea', '.gitignore', 'readme.md']
# # put = 'C:/Users/Топлог/PycharmProjects/SkillBox/Projekt/'
# # out = search(put)
# # print(out)
# # for i in out:
# #     data = open(i, 'r', encoding='UTF-8').read()
# #     script = open('script.txt', 'a', encoding='UTF-8')
# #     script.write('\n')
# #     script.write(data)
# #     script.write('\n')
# #     script.write('*' * 40)
# #     script.write('\n')
# #     script.close()
#
# # 23 урок Ошибки и исключения
# #
# # BRUCE_WILLIS = 42
# #
# # input_data = input('Введите строку: ')
# # try:
# #     leeloo = int(input_data[4])
# # except ValueError:
# #     print('невозможно преобразовать к числу')
# # except IndexError:
# #     print('выход за границы списка')
# #
# # try:
# #     result = BRUCE_WILLIS * leeloo
# #     print(f'- Leeloo Dallas! Multi-pass № {result}!')
# # except:
# #     print('остальные исключения')
#
# # \\Точка с координатамии счетчиком точек
#
# # class Tochka:
# #     count = 0
# #     def __init__(self, name, x = 0, y = 0):
# #         self.name = name
# #         self.x = x
# #         self.y = y
# #         Tochka.count += 1
# #
# #     def info(self):
# #         print('Координаты точки {}: {}, {}'.format(self.name, self.x, self.y))
# #
# #
# # t = Tochka('t', 5, 7)
# # t2 = Tochka('t2', 3, 9)
# # t.info()
# # t2.info()
# # print(Tochka.count)
#
# # ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# # \\Весёлая ферма
# # Для игры «Весёлая ферма» необходимо прописать два класса: класс «Картошка» и класс «Грядка картошки».
# #
# # У картошки есть её номер в грядке, а также стадия зрелости. Она может предоставлять информацию о своей зрелости и расти.
# # Всего у картошки может быть четыре стадии зрелости.
# #
# # Грядка с картошкой содержит список картошки, которая на ней растёт, и может, собственно, взращивать всю эту картошку,
# # а также предоставлять информацию о зрелости всей картошки на своей территории.
# #
# # Реализуйте оба класса и проверьте их работу: создайте экземпляр грядки из пяти картошек и три раза взрастите грядку.
# #
# # class Kartoshka:
# #     staddii_zrelosti = {0: 'Pusto', 1: 'Rostok', 2: 'Zelenaya', 3: 'Sozrela'}
# #
# #     def __init__(self, nomer):
# #         self.nomer = nomer
# #         self.zrelost = 0
# #
# #
# #     def rost(self):
# #         if self.zrelost < 3:
# #             self.zrelost += 1
# #         self.info()
# #
# #
# #     def info(self):
# #         print('Kartoshka {} - {}'.format(self.nomer, Kartoshka.staddii_zrelosti[self.zrelost]))
# #
# #     def sozrela(self):
# #         if self.zrelost == 3:
# #             return True
# #         return False
# #
# #
# # class Gradka:
# #     def __init__(self, colvo):
# #         self.kartoshki = [Kartoshka(nomer) for nomer in range(1, colvo+1)]
# #
# #     def virashivanie(self):
# #         print('Kartoshka rastet')
# #         for i_kartoshka in self.kartoshki:
# #             i_kartoshka.rost()
# #     def vse_sozrelo(self):
# #         if not all([i_kartoshka.sozrela() for i_kartoshka in self.kartoshki]):
# #                 print('Kartoshka eshe ne sozrela')
# #         else:
# #             print('Vsya kortoshka sozrela')
# #
# #
# # moya_gryadka = Gradka(5)
# # moya_gryadka.vse_sozrelo()
# # for _ in range(3):
# #     moya_gryadka.virashivanie()
# # ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# #
# # \\Точка с координатамии гетеры и сетеры
# #
# # class Tochka:
# #     __name = ''
# #     __x = 0
# #     __y = 0
# #     def set_name(self, name):
# #         self.__name = name
# #
# #     def set_x(self, x):
# #         if isinstance(x, int):
# #             self.__x = x
# #         else:
# #             raise Exception('Координата точки должна быть целым числом')
# #
# #     def set_y(self, y):
# #         if isinstance(y, int):
# #             self.__y = y
# #         else:
# #             raise Exception('Координата точки должна быть целым числом')
# #
# #     def __init__(self, name, x = 0, y = 0):
# #         self.set_name(name)
# #         self.set_x(x)
# #         self.set_y(y)
# #
# #     def get_name(self):
# #         return self.__name
# #
# #     def get_x(self):
# #         return self.__x
# #
# #     def get_y(self):
# #         return self.__y
# #
# #     def __str__(self):
# #         return  'Координаты точки {}: {}, {}'.format(self.get_name(), self.get_x(), self.get_y())
# #
# #
# # t = Tochka('t', 5, 7)
# # t2 = Tochka('t2', 3, 9)
# # print(t.__str__())
# # print(t2.__str__())
# # ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# # Задача 1. Юниты
# #
# # Есть базовый класс «Юнит», который определяется количеством здоровья (хитпоинты). У Юнита есть действие
# # «получить урон» (базовый класс получает 0 урона).
# #
# # Также есть два дочерних класса:
# #
# # Солдат: получает урон, равный переданному значению.
# # Обычный гражданин: получает урон, равный двукратному переданному значению.
# # Реализуйте родительский и дочерние классы и их методы, используя принцип полиморфизма (а также инкапсуляции и
# # наследования, конечно же).
# #
# # class Unit:
# #     def __init__(self, health):
# #         self.__health = health
# #
# #     def hit(self, hit):
# #         self.__health -= 0
# #
# #
# # class Soldier(Unit):
# #     def __init__(self, health):
# #         super().__init__(health)
# #         self.set_health(health)
# #
# #     def set_health(self, number):
# #          self.__health = number
# #
# #     def get_health(self):
# #         return self.__health
# #
# #     def hit(self, hit):
# #         health = self.get_health()
# #         health -= hit
# #         self.set_health(health)
# #
# #     def __str__(self):
# #         return 'У солдата осталось {} здоровья'.format(self.get_health())
# #
# #
# # class Civilian(Unit):
# #     def __init__(self, health):
# #         super().__init__(health)
# #         self.set_health(health)
# #
# #     def set_health(self, number):
# #         self.__health = number
# #
# #     def get_health(self):
# #         return self.__health
# #
# #     def hit(self, hit):
# #         health = self.get_health()
# #         health -= hit*2
# #         self.set_health(health)
# #
# #     def __str__(self):
# #         return 'У гражданского осталось {} здоровья'.format(self.get_health())
# #
# #
# # s = Soldier(health=10)
# # c = Civilian(health=10)
# # s.hit(4)
# # c.hit(4)
# # print(s.__str__())
# # print(c.__str__())
# #
# # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# #
# #Итераторы
# # # l = [10, 20, 30]
# # # i = iter(l)
# # # while True:
# # #     try:
# # #         print(next(i))
# # #     except StopIteration:
# #         pass
#
# # Бесконечный итератор
# # class СountIterator:
# #     count = 0
# #
# #     def __iter__(self):
# #         return self
# #
# #     def __next__(self):
# #         vol = self.count
# #         self.count += 1
# #         return self.count
# #
# #
# # my_iter = СountIterator()
# # for i_elem in my_iter:
# #     print(i_elem)
# # Случайная сумма
# # import random
# #
# #
# # class RandomSum:
# #     def __init__(self, number):
# #         self.count = 0
# #         self.elem_1 = round(random.uniform(0, 1), 2)
# #         self.elem_2 = round(random.uniform(0, 1), 2) + self.elem_1
# #         self.limit = number
# #
# #     def __iter__(self):
# #         self.count = 0
# #         self.elem_1 = round(random.uniform(0, 1), 2)
# #         self.elem_2 = round(random.uniform(0, 1), 2) + self.elem_1
# #         return self
# #
# #
# #     def __next__(self):
# #         if self.count < self.limit:
# #             self.elem_1 = self.elem_2
# #             self.elem_2 = round(random.uniform(0, 1), 2) + self.elem_1
# #             self.count += 1
# #             return self.elem_2
# #         else:
# #             raise StopIteration
# #
# #
# # iter = RandomSum(10)
# # for i in iter:
# #     print(i)
# # print('abra-kadabra')
# # for i in iter:
# #     print(i)
# #
# # Генератор
# # def gen():
# #     c = 0
# #     while True:
# #         yield c
# #         c+=1
# #
# #
# # for i in gen():
# #     print(i)
# #
# # Генератор простых чисел
# # def IsPrime(n):
# #     if n == 0:
# #         return False
# #     if n == 1:
# #         return True
# #     d = 2
# #     while n % d != 0:
# #         d += 1
# #     return d == n
# #
# # def g_p(number):
# #     for i in range(1, number+1):
# #         if IsPrime(i):
# #             yield i
# #
# #
# # for i in g_p(11):
# #     print(i)
# #
# # ФУНКЦИИ КАК ОБЪЕКТЫ.
# # def func_1(x):
# #
# #     return x + 10
# #
# # def func_2(func, num):
# #     res = func(num)
# #     return res*res
# #
# #
# # print(func_1(9))
# # print(func_2(func_1, 9))
# # import time
# #
# #
# # def timer(func):
# #     started = time.time()
# #     func()
# #     stopped = time.time()
# #     time_res = stopped-started
# #     return time_res
# #
# # def sq():
# #     num = 100
# #     res = 0
# #     for _ in range(num + 1):
# #         res += sum(i**2 for i in range(10000))
# #     return res
# #
# # print(timer(sq))
# #
# # ДЕКОРАТОРЫ
# #
# #
# # def decorator(func):
# #     def wrapped_func(*arg, **kwarg):
# #         func(*arg, **kwarg)
# #         func(*arg, **kwarg)
# #     return wrapped_func
# #
# # @decorator
# # def greeting(name):
# #     print('Привет, {name}!'.format(name=name))
# #
# #
# # greeting('Tom')
# #
# # import time
# #
# #
# # def timer(func):
# #     def wrapped_func(*arg, **kwarg):
# #         started = time.time()
# #         res = func(*arg, **kwarg)
# #         stopped = time.time()
# #         time_res = stopped-started
# #         print('Func rabotala {} sec'.format(time_res))
# #         return res
# #     return wrapped_func
# #
# # @timer
# # def sq():
# #     num = 100
# #     res = 0
# #     for _ in range(num + 1):
# #         res += sum(i**2 for i in range(10000))
# #     return res
# #
# # my_t = sq()
# # print(my_t)
# #
# #
# # def bread(func):
# #     def wrapped_func():
# #         f = func()
# #         return '\t< / ----------\ >\n\t{func}\n\t< \______ / >'.format(func = f)
# #     return wrapped_func
# #
# # def ingred(func):
# #     def wrapped_func():
# #         f = func()
# #         return '\t#помидоры#\n\t{func}\n\t~салат~'.format(func=f)
# #     return wrapped_func
# #
# #
# # @bread
# # @ingred
# # def sandwich():
# #     return '--ветчина--'
# #
# # print(sandwich())
# #
# # PLAGINS = dict()
# #
# #
# # def register(func):
# #     PLAGINS[func.__name__] = func
# #     return func
# #
# # @register
# # def hello(name):
# #     return 'Hello, {}!'.format(name)
# #
# # @register
# # def baye(name):
# #     return 'Goodbaye, {}!'.format(name)
# #
# # print(PLAGINS)
# # print(hello('Tom'))
# #
# # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# # Абстрактные классы и примеси
# from abc import ABC, abstractmethod
#
#
# class Transport(ABC):
#     def __init__(self, color: str, speed: int) -> None:
#         self.__color = color
#         self.__speed = speed
#
#     @abstractmethod
#     def move(self, ground: str) -> None:
#         pass
#
#     def alarm(self) -> None:
#         print('Би-Би-П')
#
# class Mixin():
#     def play_music(self):
#         print('Играет музыка')
#
# class Car(Transport, Mixin):
#     def __init__(self, color: str, speed: int) -> None:
#         super().__init__(color, speed)
#         self.__color = color
#         self.__speed = speed
#
#     def get_color(self) -> str:
#         return self.__color
#
#     def get_speed(self) -> int:
#         return self.__speed
#
#     def __str__(self):
#         return 'Цвет {}, скорость {}.'.format(self.get_color(), self.get_speed())
#
#     def move(self, ground: str) -> None:
#         pass
#
#
#
# car = Car('red', 50)
# car.play_music()
# print(car)
#
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# Контекст-менеджер из библиотеки.
# import time
# from contextlib import contextmanager
# from collections.abc import Iterator
#
#
# @contextmanager
# def timer() -> Iterator:
#     start = time.time()
#     try:
#         yield
#     finally:
#         print(time.time() - start)
#
#
# with timer() as t1:
#     print('Первая часть')
#     val_1 = 100 * 1000 ** 10000
#
# with timer() as t2:
#     print('Вторая часть')
#     val_2 = 200 * 2000 ** 20000
# #
# import os
# from contextlib import contextmanager
# from collections.abc import Iterator
#
# @contextmanager
# def in_dir(path: str):
#     yield os.path.join(path)
#
#
# with in_dir('C:\\') as dir_:
#
#     print(os.listdir(dir_))
#
# Декораторы с аргументами:
# def repit(amount):
#     def do(func):
#         def wrapped(*arg, **kwarg):
#             for _ in range(amount):
#                 func()
#         return wrapped
#     return do
#
# @repit(amount=4)
# def func():
#     print('Hello')
#
# func()
#
# Декораторы классов:
# import time
# import functools
# from datetime import datetime
# def class_decorator(cls):
#     @functools.wraps(cls)
#     def wrapped(*arg, **kwarg):
#         instance = cls(*arg, **kwarg)
#         print('Время создания {}'.format(datetime.utcnow()))
#         print('Методы класса: {}'.format(dir(cls)))
#         return instance
#     return wrapped
#
# @class_decorator
# class ClassName:
#     def __init__(self):
#         pass
#
#     def mrthod_1(self):
#         pass
#
#     def mrthod_2(self):
#         pass
#
#
# instance_1 = ClassName()
# time.sleep(2)
# instance_2 = ClassName()
#
# import functools
#
# def decorator(data):
#     print(data.__name__)
#     print(data.__annotations__)
#     print(data.__doc__)
#
# def logging(decorator):
#     @functools.wraps(decorator)
#     def decorate(cls):
#         for i_method in dir(cls):
#             if i_method.startswith('__') is False:
#                 cur_method = getattr(cls, i_method)
#                 decorate_method = decorator(cur_method)
#                 setattr(cls, i_method, decorate_method)
#         return cls
#     return decorate
#
# @logging(decorator)
# class ClassName:
#     def __init__(self) -> None:
#         """Privet"""
#         pass
#
#     def method_1(self, uno, duo) -> None:
#         """Privet"""
#         pass
#
#     def method_2(self, *arg, **kwarg) -> None:
#         """Privet"""
#         pass
#
#
# a = ClassName()
#
#|||||||||||||||||||||||||||||||||||||||||||||||||||
# Пространство имён и области видимости
#
# def for_dict(data):
#     for l in data:
#         for i, j in enumerate(l):
#             if i == 1:
#                 return l[j]
#
# grades = [
#     {'name': 'Kenneth', 'score': 3}, {'name': 'Bebe', 'score': 41}, {'name': 'Joyce', 'score': 24},
#     {'name': 'Richard', 'score': 37}, {'name': 'Marian', 'score': 44}, {'name': 'Jana', 'score': 45},
#     {'name': 'Sarah', 'score': 90}, {'name': 'Eddie', 'score': 2}, {'name': 'Mary', 'score': 63},
#     {'name': 'Ronald', 'score': 15}, {'name': 'David', 'score': 44}, {'name': 'Richard', 'score': 78},
#     {'name': 'Warren', 'score': 7}, {'name': 'Alyssa', 'score': 13}, {'name': 'Lloyd', 'score': 52},
#     {'name': 'Vanessa', 'score': 6}, {'name': 'Karen', 'score': 40}, {'name': 'James', 'score': 54},
#     {'name': 'Annie', 'score': 87}, {'name': 'Glenn', 'score': 9}, {'name': 'Bruce', 'score': 68},
#     {'name': 'Ramona', 'score': 64}, {'name': 'Jeannie', 'score': 22}, {'name': 'Aaron', 'score': 3},
#     {'name': 'Ronnie', 'score': 47}, {'name': 'William', 'score': 94}, {'name': 'Sandra', 'score': 40},
# ]
#
# for_dict(grades)
# print(sorted(grades, key= lambda elem: elem))
# |||||||||||||||||||||||||||||||||||||||||||||||||||||
# Регулярные выражения.
# import re
#
#
# text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'
# # Определить, начинается ли текст с шаблона wo.
# print(re.match(r'wo', text))
# # Найти первое упоминание шаблона wo в тексте.
# print(re.search(r'wo', text))
# # Определить содержимое найденной по шаблону подстроки из пункта 2.
# print(re.search(r'wo', text).group())
# # Найти позицию, с которого начинается первое упоминание шаблона wo.
# print(re.search(r'wo', text).start())
# # Найти позицию, на которой заканчивается первое упоминание шаблона wo.
# print(re.search(r'wo', text).end())
# # Получить список из каждого упоминания шаблона wo в тексте.
# print(re.findall(r'wo', text))
# # Заменить в тексте все совпадения по шаблону wo на слово «ЗАМЕНА».
# print(re.sub('wo', 'ЗАМЕНА', text))
# import re
#
#
# text = 'How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?'
# print(re.findall(r'\\wwood\+\?,', text))
# import re
#
#
# text = 'Even if they are djinns, I will get djinns that can outdjinn them.'
# pattern = r'\b[aeiouAEIOU]\w*'
# res_2 = re.findall(r'\b[^ aeiouAEIOU]\w+', text)
# res = re.findall(pattern, text)
# print(res_2)
# print(res)
# import re
#
#
# text = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
#
# res = re.findall(r'\d{2,2}-\d{2,2}-\d{4,4}', text)
# print(res)
# |||||||||||||||||||||||||||||||||||||||||
# Запросы
# import requests
# import json
#
#
# req_1 = requests.get('https://swapi.dev/api/people/3/')
# data = json.loads(req_1.text)
# print(data)