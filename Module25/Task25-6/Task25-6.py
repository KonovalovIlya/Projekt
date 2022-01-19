# Артём увлёкся предыдущим экспериментом и решил расширить его, создав целую семью из Мужа, Жены и Кота.
# Условия эксперимента следующие.
# Каждый день участники жизни могут делать только одно действие. Все вместе они должны прожить год и не умереть.
#
# Муж может:
# есть,
# играть,
# ходить на работу.
#
# Жена может:
# есть,
# покупать продукты,
# покупать шубу,
# убираться в доме.
#
# Кот может:
# есть,
# спать,
# драть обои.
#
# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (вначале 100),
#   кол-во еды в холодильнике (вначале 50),
#   еда для кота (вначале 30),
#   кол-во грязи (вначале 0).
#
# У людей есть имя, степень сытости (вначале 30) и степень счастья (вначале 100).
# Все люди могут гладить кота (+5 к счастью).
#
# У кота есть имя и степень сытости (вначале 30).
#
# Любое действие (в том числе и кота), кроме «есть», приводит к уменьшению степени сытости на 10 пунктов.
# Взрослые едят максимум по 30 единиц еды, степень сытости растёт на один пункт за один пункт еды.
# Кот ест максимум по 10 единиц еды, степень сытости растёт на два пункта за один пункт еды.
# Степень сытости не должна падать ниже нуля, иначе человек или кот умрёт от голода.
#
# Деньги в тумбочку добавляет муж, после работы — сразу 150 единиц.
# Еда стоит 10 денег за 10 единиц еды. Шуба стоит 350 единиц.
# Еда для кота тоже покупается: за 10 денег 10 еды.
#
# Грязь добавляется каждый день по пять пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если кот дерёт обои, то грязи тоже становится больше на пять пунктов.
# Если в доме грязи больше 90, у людей падает степень счастья каждый день на 10 пунктов.
# Степень счастья растёт: у мужа от игры в компьютер (на 20), у жены от покупки шубы (на 60, но шуба дорогая).
# Степень счастья не должна падать ниже 10, иначе человек умирает от депрессии.
#
# Реализуйте такую программу. Подведите итоги жизни за год: сколько было заработано денег, сколько съедено еды, сколько куплено шуб.
# Дополнительно: добавьте ещё ребёнка и несколько котов.
import random


class House:
    __money = 100
    __food = 50
    __food_pet = 30
    __dirt = 0

    def set_money_up(self, number):
      self.__money += number

    def set_money_down(self, number):
      self.__money -= number

    def set_food_up(self, number):
      self.__food += number

    def set_food_down(self, number):
      self.__food -= number

    def set_food_pet_up(self, number):
      self.__food_pet += number

    def set_food_pet_down(self, number):
      self.__food_pet -= number

    def set_dirt(self, number):
      self.__dirt = number

    def set_dirt_up(self, number):
      self.__dirt += number

    def set_dirt_down(self, number):
      self.__dirt -= number

    def get_dirt(self):
        return self.__dirt

    def get_food(self):
        return self.__food

    def get_money(self):
        return self.__money

    def __str__(self):
        return 'кол-во денег в тумбочке - {money}, кол-во еды в холодильнике - {food}, ' \
               'еда для кота - {food_pet}, кол-во грязи - {dirt}.'.format(
            money= self.__money,
            food= self.__food,
            food_pet= self.__food_pet,
            dirt= self.__dirt
        )


class Humanoid:
    def __init__(self, name, satiety = 30, happiness = 100):
        self.__name = name
        self.__satiety = satiety
        self.__happiness = happiness

    # def set_name(self, data):
    #     self.__name = data

    def set_happiness_up(self, number):
        self.__happiness += number

    def set_happiness_down(self, number):
        self.__happiness -= number

    def set_satiety_up(self, number):
        self.__satiety += number

    def set_satiety_down(self, number):
        self.__satiety -= number

    def get_name(self):
        return self.__name

    def get_satiety(self):
        return self.__satiety

    def get_happiness(self):
        return self.__happiness

    def glitch_the_cat(self):
        self.set_happiness_up(5)

    def eat(self, house):
        print('Пора поесть')
        eating = random.randint(1, 30)
        house.set_food_down(eating)
        self.set_satiety_up(eating)
        print('Сытость +{}'.format(eating))
        print('Еды осталось {}'.format(house.get_food()))

    def __str__(self):
        return 'Имя - {name}, степень сытости - {satiety} и степень счастья - {happiness}'.format(
            name= self.__name,
            satiety= self.__satiety,
            happiness= self.__happiness
        )


class Husband(Humanoid):
    def __init__(self, name):
        super().__init__(name)
        print('Привет! Меня зовут {}'.format(self.get_name()))

    def play(self):
        self.set_satiety_down(10)
        self.set_happiness_up(20)

    def work(self, house):
        self.set_satiety_down(10)
        house.set_money_up(150)


class Wife(Humanoid):
    def __init__(self, name):
        super().__init__(name)
        print('Привет! Меня зовут {}'.format(self.get_name()))

    def shopping_food(self, house):
        amount = 10 * random.randint(1, 7)
        self.set_satiety_down(10)
        house.set_food_up(amount)
        house.set_money_down(amount)

    def cleaning(self, house):
        amount = random.randint(30, 100)
        self.set_satiety_down(10)
        if not house.get_dirt() - amount >= 0:
            house.set_dirt(0)
        else:
            house.set_dirt_down(amount)

    def shopping_fur_coat(self, house):
        print('{}, похоже пора купить шубу'.format(wife.get_name()))
        house.set_money_down(350)
        self.set_satiety_down(10)
        self.set_happiness_up(60)


class Pet:
    def __init__(self, name, satiety = 30):
        self.__name = name
        self.__satiety = satiety

    def set_satiety_up(self, number):
        self.__satiety += number

    def set_satiety_down(self, number):
        self.__satiety -= number

    def get_satiety(self):
        return self.__satiety

    def eat(self, house):
        eating = random.randint(1, 30)
        self.set_satiety_up(eating)
        house.set_food_pet_down(house, eating)


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name)

    def wall_crushing(self, house):
        self.set_satiety_down(10)
        house.set_dirt_up(5)

    def sleep(self):
        self.set_satiety_down(10)


class Death(Exception):
    pass


def another_day(home, husband, wife, cat):
    death = False
    if husband.get_satiety() <= 0 or wife.get_satiety() <= 0 or cat.get_satiety() <= 0:
        death = True
    elif husband.get_happiness() <= 10 or wife.get_happiness() <= 10:
        death = True
    if death:
        print('У нас тепленький труп!')
        raise Death(Exception)

    home.set_dirt_up(5)
    if home.get_dirt() > 90:
        husband.set_happiness_down(10)
        wife.set_happiness_down(10)

    cube = random.randint(1, 6)
    if husband.get_satiety() < 20:
        print('Эй {}'.format(husband.get_name()))
        husband.eat(home)
    if wife.get_satiety() < 20:
        print('Эй {}'.format(wife.get_name()))
        wife.eat(home)
    if wife.get_happiness() < 20:
        wife.shopping_fur_coat(home)
    elif home.get_food() < 10:
        wife.shopping_food(home)
    elif home.get_money() < 50:
        husband.work(home)
    elif cube == 1:
        husband.work(home)
    elif cube == 2:
        wife.cleaning(home)
    else:
        husband.play()
        wife.glitch_the_cat()


home = House()
husband = Husband('Vova')
wife = Wife('Liza')
cat = Cat('Tom')

for i in range(365):
    print('День {}'.format(i))
    another_day(home, husband, wife, cat)
# print(home.__str__())
# husband.eat(home)
# wife.eat(home)
#
# print(husband.__str__())
# print(wife.__str__())
# print(home.__str__())
