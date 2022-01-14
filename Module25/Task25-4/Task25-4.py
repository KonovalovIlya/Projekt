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
    def salary_out(self):
        pass


class Manager(Employee):
    def __init__(self,name, surname, age):
        super(Manager, self).__init__(name, surname, age)

    def get_name(self):
        return self.__name

    def salary_out(self):
        self.salary = 13000

    def __str__(self):
        return 'Зарплата управляющего {} - {}'.format(self.get_name(), self.salary)


class Agent(Employee):
    def __init__(self,name, surname, age, plan):
        super(Agent, self).__init__(name, surname, age)
        self.plan = plan

    def get_name(self):
        return self.__name

    def salary_out(self):
        self.salary = 5000 + self.plan/100*5

    def __str__(self):
        return 'Зарплата агента {} - {}'.format(self.get_name(), self.salary)


class Worker(Employee):
    def __init__(self, name, surname, age, hours):
        super(Worker, self).__init__(name, surname, age)
        self.hours = hours

    def get_name(self):
        return self.__name

    def salary_out(self):
        self.salary = 100 * self.hours

    def __str__(self):
        return 'Зарплата рабочего {} - {}'.format(self.get_name(), self.salary)


persona_1 = Manager('Ваня', 'Иванов', 20)
persona_1.salary_out()
persona_2 = Manager('Петя', 'Петров', 21)
persona_2.salary_out()
persona_3 = Manager('Коля', 'Николаев', 22)
persona_3.salary_out()
persona_4 = Agent('Саша', 'Александров', 23, 10e6)
persona_4.salary_out()
persona_5 = Agent('Боря', 'Борисов', 24, 10e5)
persona_5.salary_out()
persona_6 = Agent('Мирон', 'Миронов', 25, 15e5)
persona_6.salary_out()
persona_7 = Worker('Матвей', 'Матвеев', 26, 120)
persona_7.salary_out()
persona_8 = Worker('Леша', 'Алексеев', 27, 110)
persona_8.salary_out()
persona_9 = Worker('Дима', 'Дмитриев', 28, 130)
persona_9.salary_out()
list = [
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
for i in list:
    print(i.__str__())