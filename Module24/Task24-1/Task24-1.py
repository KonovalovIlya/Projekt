# Вы работаете в команде разработчиков мобильной игры, и вам досталась вот такая часть от ТЗ заказчика:
#
# Есть два юнита, каждый из них называется «Воин». Каждому устанавливается здоровье в 100 очков. Они бьют друг друга в
# случайном порядке. Тот, кто бьёт, здоровья не теряет. У того, кого бьют, оно уменьшается на 20 очков от одного удара.
# После каждого удара надо выводить сообщение, какой юнит атаковал и сколько у противника осталось здоровья. Как только
# у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
#
# Реализуйте такую программу.
import random


class Warrior:
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health

    def attack(self, damage = 20):
        return damage

    def get_hit(self, damage = 20):
        self.health = self.health - damage
        if self.health <= 0:
            self.health = 0

    def info(self):
        print('Здоровье: {}'.format(self.health))


warrior_1 = Warrior('warrior_1')
warrior_2 = Warrior('warrior_2')

while True:
    attacker = random.choice([warrior_1, warrior_2])
    print('Атакует {}'.format(attacker.name))
    if attacker == warrior_1:
        damaged = warrior_2
        damaged.get_hit(warrior_1.attack())
    else:
        damaged = warrior_1
        damaged.get_hit(warrior_2.attack())
    print('Здоровья у {} осталось {}'.format(damaged.name, damaged.health))
    if damaged.health == 0:
        break
