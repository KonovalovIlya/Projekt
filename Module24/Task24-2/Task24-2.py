# Реализуйте модель с именем Student, содержащую поля: «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).
# Затем создайте список из десяти студентов и отсортируйте его по возрастанию среднего балла. Выведите результат на экран.
import random
class Student:

    def __init__(self, name, group, score):
        self.name = name
        self.group = group
        self.score = score
        self.grade_point_average = self.average_score()

    def average_score(self):
        m = 0
        for j in self.score.values():
            m += j
        m = int(m / len(self.score))
        return m

    def info(self):
        print('Имя: {}, Группа: {}, Успеваемость: {}, Средний балл: {}'.format(
            self.name,
            self.group,
            self.score,
            self.grade_point_average
            )
        )


class Group:
    names_list = ['Вася', 'Петя', 'Коля', 'Дима', 'Саша', 'Женя']
    def __init__(self, group):
        self.students = [
            Student(
                random.choice(self.names_list), group,
                {'Русский язык': random.randint(1,5), 'Литература': random.randint(1,5), 'История': random.randint(1,5)}
            ) for _ in range(10)
        ]
    def info(self):
        for i in self.students:
            i.info()

    def sort(self):
        sort = True
        while sort:
            sort = False
            for i in range(len(self.students)-1):
                if self.students[i].grade_point_average < self.students[i + 1].grade_point_average:
                    self.students[i], self.students[i + 1] = self.students[i + 1], self.students[i]
                    sort = True


g_2 = Group('g_2')
g_2.info()
g_2.sort()
print()
g_2.info()
