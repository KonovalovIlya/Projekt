# Мы продолжаем писать игру «Весёлая ферма» и теперь необходимо её немного модернизировать. Всё-таки кому-то же нужно
# собирать урожай, и для этого нам понадобится садовник, который имеет:
#
# Имя.
# Грядку с растением, за которым он ухаживает (в нашем случае пока только грядка с картошкой).
#
#
# И может:
#
# Ухаживать за грядкой.
# Собирать с неё урожай (количество картошки ― пустой список).
#
#
# Модернизируйте программу, используя новый класс «Садовник».
#
# Проверьте работу программы, создав грядку из пяти картошек и отдав эту грядку садовнику. Пусть поухаживает за грядкой
# и соберёт урожай (а, может быть, даже и не один).
#
class Potato:
    size = {0: 'Пусто', 1: 'Росток', 2: 'Маленькая', 3: 'Отличный размер'}

    def __init__(self, number, size = 0):
        self.number = number
        self.size = size

    def grows(self):
        if self.size < 3:
            self.size += 1
        self.info()

    def info(self):
        print('Картошка {} - {}'.format(self.number, Potato.size[self.size]))

    def good(self):
        if self.size == 3:
            return True
        return False


class PotatoGarden:
    def __init__(self, number):
        self.potatoes = [Potato(number) for number in range(1, number + 1)]

    def cultivation(self):
        print('Картошка растет')
        for i_potato in self.potatoes:
            i_potato.grows()

    def is_all_good(self, worker):
        if not all([i_potato.good() for i_potato in self.potatoes]):
                print('Картошка еще не созрела')
        else:
            print('Вся картошка созрела')
            worker.gathering()

class GardenWorker:
    potato_taken = []
    def __init__(self, name, garden):
        self.name = name
        self.garden = garden

    def cultivation(self):
        print('Садовник ухаживает за грядкой')
        self.garden.cultivation()

    def gathering(self):
        print('Садовник собирает уражай')
        for _ in range(len(self.garden.potatoes)):
            self.potato_taken.append('Картошка')
        print('Садовник собрал {} картошек'.format(len(self.garden.potatoes)))


potato_garden_1 = PotatoGarden(5)
worker = GardenWorker('Ivan', potato_garden_1)
potato_garden_1.is_all_good(worker)
for _ in range(3):
    potato_garden_1.cultivation()
potato_garden_1.is_all_good(worker)
