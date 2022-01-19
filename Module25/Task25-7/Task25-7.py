class Stek:
    __stek_list = []

    def add_to_stek(self, data):
        self.__stek_list.append(data)

    def rem_from_stek(self):
        self.__stek_list.pop(len(self.__stek_list)-1)


class TaskManager:
    __manager_dict = {}

    def add_task(self, task, priority):
        if self.__manager_dict.get(priority) is None:
            self.__manager_dict[priority] = task
        elif task in self.__manager_dict.get(priority):
            pass
        else:
            self.__manager_dict[priority] = ', '.join([self.__manager_dict.get(priority), task])

    def remove_task(self, data):
        for i, j in self.__manager_dict.items():
            if data in j:
                j = j.replace(data, '', 1)
                if j.startswith(', '):
                    j = j.replace(', ', '', 1)
                self.__manager_dict[i] = j

    def __str__(self):
        string = str()
        for i, j in self.__manager_dict.items():
            string = ''.join([str(i), ': ', j, '\n', string])
        l = sorted(string.split('\n'))
        l.pop(0)
        string = '\n'.join(l)
        return string
        # return '{}: {}'.format(i, j )

manager = TaskManager()

manager.add_task("сделать уборку", 4)

manager.add_task("помыть посуду", 4)

manager.add_task("отдохнуть", 1)

manager.add_task("поесть", 2)

manager.add_task("сдать дз", 2)
print(manager)
# manager.__str__()
manager.remove_task("поесть")

print(manager)
# manager.__str__()