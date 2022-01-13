# Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:
#
# Имя.
# Возраст.
# Список детей.
# И он может:
#
# Сообщить информацию о себе.
# Успокоить ребёнка.
# Покормить ребёнка.
#
#
# У ребёнка есть:
#
# Имя.
# Возраст (должен быть меньше возраста родителя хотя бы на 16 лет).
# Состояние спокойствия.
# Состояние голода.
# Реализация состояний на ваше усмотрение! Это может быть и простой «флаг», и словарь состояний,
# и что-нибудь ещё интереснее!
import random


class Parent:
    names_list = ['Вася', 'Петя', 'Коля', 'Дима', 'Саша', 'Женя']
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.babys = [Baby(random.choice(self.names_list), random.randint(3,15)) for i in range(2)]

    def info(self):
        print('Имя: {}, Возраст: {}, Список детей: {}'.format(self.name, self.age, [i.name for i in self.babys]))

    def baby_calm_down(self, baby):
        baby.calm -= 50

    def give_eat(self, baby):
        baby.hungry -= 30


class Baby:
    def __init__(self, name, age, calm = 0, hungry = 10):
        self.name = name
        self.age = age
        self.calm = calm
        self.hungry = hungry

    def info(self):
        print('Имя: {}, Возраст: {}, Эмоциональное состояние: {}, Сытость: {}'.format(
            self.name, self.age, self.calm, self.hungry)
        )

    def stress(self, parent):
        while self.calm != 100:
            if self.age < 10:
                self.calm += 2
            elif self.age >= 10:
                self.calm += 1
            if self.calm == 50:
                print('{} расстроен.'.format(self.name))
                if input('Хотите его успокоить? ').lower() == 'да':
                    parent.baby_calm_down(self)
                    print('Эмоциональное состояние {}: {}'.format(self.name, self.calm))
                else:
                    continue
            if self.calm == 70:
                print('{} плачет.'.format(self.name))
                if input('Хотите его успокоить? ').lower() == 'да':
                    parent.baby_calm_down(self)
                    print('Эмоциональное состояние {}: {}'.format(self.name, self.calm))
                else:
                    continue
            if self.calm == 100:
                print('{} в истерике.'.format(self.name))
                for _ in range(3):
                    answer = input('Хотите его успокоить? ').lower()
                    if answer == 'да':
                        parent.baby_calm_down(self)
                        print('Эмоциональное состояние {}: {}'.format(self.name, self.calm))
                else:
                    print('Все...')

    def more_hungry(self, parent):
        while self.hungry != 100:
            if self.age < 10:
                self.hungry += 2
            elif self.age >= 10:
                self.hungry += 1
            if self.hungry == 50:
                print('{} голоден.'.format(self.name))
                if input('Хотите его накормить? ').lower() == 'да':
                    parent.give_eat(self)
                    print('Голод {}: {}'.format(self.name, self.hungry))
                else:
                    continue
            if self.hungry == 70:
                print('{} очень голоден.'.format(self.name))
                if input('Хотите его накормить? ').lower() == 'да':
                    parent.give_eat(self)
                    print('Голод {}: {}'.format(self.name, self.hungry))
                else:
                    continue
            if self.hungry == 100:
                print('{} ща коньки отбросит.'.format(self.name))
                for _ in range(3):
                    answer = input('Хотите его накормить? ').lower()
                    if answer == 'да':
                        parent.give_eat(self)
                        print('Голод {}: {}'.format(self.name, self.hungry))
                else:
                    print('Все...')







dad = Parent('Ivan', 39)
dad.info()
baby_1 = dad.babys[0]
baby_2 = dad.babys[1]
baby_1.info()
baby_2.info()
# baby_1.stress(dad)
baby_2.more_hungry(dad)