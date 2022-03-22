# Реализуйте иерархию классов, описывающих служащих в компании. На самом верху иерархии — класс Person, который
# описывает человека именем, фамилией и возрастом. Все атрибуты этого класса являются приватными.
#
# Далее идёт класс Employee и производные от него классы Manager, Agent и Worker.
#
# Класс «Работник» должен иметь метод расчёта заработной платы, переопределённый в каждом из производных классов.
# Заработная плата Manager постоянна и равна 13000, заработная плата Agent определяется как оклад 5000 + 5% объёма
# продаж, который хранится в специальном поле класса Agent, и заработная плата Worker определяется как 100 * число
# отработанных часов, которое также хранится в отдельном поле.
#
# В основной программе создайте список из девяти объектов: первые три — Manager, следующие три — Agent и последние
# три — Worker. Выведите на экран величину заработной платы всех девяти служащих.
class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age


class Employee(Person):

    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.set_name(name)
        self.set_surname(surname)
        self.set_age(age)
        self.__salary = 0
        self.__dolzhnost = ''

    def set_name(self, data):
        self.__name = data

    def set_surname(self, data):
        self.__surname = data

    def set_age(self, data):
        self.__age = data

    def set_dolzhnost(self, string):
        self.__dolzhnost = string

    def set_salary(self, number):
        self.__salary = number

    def salary_out(self):
        self.set_salary(0)

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def __str__(self):
        return '{} {} {} - зарплата {}'.format(self.__dolzhnost, self.get_name(), self.get_surname(), self.__salary)


class Manager(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.set_dolzhnost('Управляющицй')

    def salary_out(self):
        self.set_salary(13000)


class Agent(Employee):
    def __init__(self, name, surname, age, plan):
        super().__init__(name, surname, age)
        self.plan = plan
        self.set_dolzhnost('Агент')

    def salary_out(self):
        self.set_salary(5000 + self.plan/100*5)


class Worker(Employee):
    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.hours = hours
        self.set_dolzhnost('Рабочий')

    def salary_out(self):
        self.set_salary(100 * self.hours)


persona_1 = Manager('Ваня', 'Иванов', 20)
persona_2 = Manager('Петя', 'Петров', 21)
persona_3 = Manager('Коля', 'Николаев', 22)
persona_4 = Agent('Саша', 'Александров', 23, 10e6)
persona_5 = Agent('Боря', 'Борисов', 24, 10e5)
persona_6 = Agent('Мирон', 'Миронов', 25, 15e5)
persona_7 = Worker('Матвей', 'Матвеев', 26, 120)
persona_8 = Worker('Леша', 'Алексеев', 27, 110)
persona_9 = Worker('Дима', 'Дмитриев', 28, 130)
list_ = [
    persona_1,
    persona_2,
    persona_3,
    persona_4,
    persona_5,
    persona_6,
    persona_7,
    persona_8,
    persona_9
]
for i in list_:
    i.salary_out()
    print(i.__str__())
