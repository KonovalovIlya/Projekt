# Реализуйте иерархию классов, описывающих имущество налогоплательщиков. Она должна состоять из базового класса
# Property и производных от него классов Apartment, Car и CountryHouse.
#
# Базовый класс должен иметь атрибут worth (стоимость), который передаётся в конструктор, и метод расчёта налога,
# переопределённый в каждом из производных классов. Налог на квартиру вычисляется как 1/1000 её стоимости,
# на машину — 1/200, на дачу — 1/500.
#
# Каждый дочерний класс должен иметь конструктор с одним параметром, передающий свой параметр конструктору базового
# класса.
#
# Разработайте интерфейс программы. Пусть она запрашивает у пользователя количество его денег и стоимость имущества,
# а затем выдаёт ему налог на соответствующее имущество и сколько денег ему не хватает (если это так).
#
class Property:
    def __init__(self, worth):
        self.__worth = worth

    def tax(self):
        self.__worth /= 100


class Apartment(Property):
    def get_worth(self):
        return self.__worth

    def set_worth(self, number):
        self.__worth = number

    def __init__(self, worth):
        super().__init__(worth)
        self.set_worth(worth)

    def tax(self):
        tax = self.get_worth() / 1000
        return tax


class Car(Property):
    def get_worth(self):
        return self.__worth

    def set_worth(self, number):
        self.__worth = number

    def __init__(self, worth):
        super().__init__(worth)
        self.set_worth(worth)

    def tax(self):
        tax = self.get_worth() / 200
        return tax


class CountryHouse(Property):
    def get_worth(self):
        return self.__worth

    def set_worth(self, number):
        self.__worth = number

    def __init__(self, worth):
        super().__init__(worth)
        self.set_worth(worth)

    def tax(self):
        tax = self.get_worth() / 500
        return tax


money = int(input('Сколько у вас денег? '))

worth_apartment = int(input('Укажите стоимость вашей квартиры: '))
apartment = Apartment(worth_apartment)

worth_car = int(input('Укажите стоимость вашей машины: '))
car = Car(worth_car)

worth_country_house = int(input('Укажите стоимость вашего загородного дома: '))
country_house = CountryHouse(worth_country_house)

print('Вам необходимо заплатить налог')

apartment_tax = apartment.tax()
print('за квартиру в размере {}'.format(apartment_tax))

car_tax = car.tax()
print('за машину в размере {}'.format(car_tax))

country_house_tax = country_house.tax()
print('за загородный дом в размере {}'.format(country_house_tax))

if money < apartment_tax + car_tax + country_house_tax:
    print('Вам не хватает {}'.format(abs(money - (apartment_tax + car_tax + country_house_tax))))