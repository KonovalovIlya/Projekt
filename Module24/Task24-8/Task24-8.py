import random


class PlayerHand:
    cards = []
    score = 0

    def info(self):
        print(self.score)

    def take_card(self):
        self.cards.append(Card().amount)
        self.score_up()

    def score_up(self):
        if '2 - Черви' in self.cards or '2 - Буби' in self.cards \
                or '2 - Крести' in self.cards or '2 - Пики' in self.cards:
            self.score += 2
        if '3 - Черви' in self.cards or '3 - Буби' in self.cards \
                or '3 - Крести' in self.cards or '3 - Пики' in self.cards:
            self.score += 3
        if '4 - Черви' in self.cards or '4 - Буби' in self.cards \
                or '4 - Крести' in self.cards or '4 - Пики' in self.cards:
            self.score += 4
        if '5 - Черви' in self.cards or '5 - Буби' in self.cards \
                or '5 - Крести' in self.cards or '5 - Пики' in self.cards:
            self.score += 5
        if '6 - Черви' in self.cards or '6 - Буби' in self.cards \
                or '6 - Крести' in self.cards or '6 - Пики' in self.cards:
            self.score += 6
        if '7 - Черви' in self.cards or '7 - Буби' in self.cards \
                or '7 - Крести' in self.cards or '7 - Пики' in self.cards:
            self.score += 7
        if '8 - Черви' in self.cards or '8 - Буби' in self.cards \
                or '8 - Крести' in self.cards or '8 - Пики' in self.cards:
            self.score += 8
        if '9 - Черви' in self.cards or '9 - Буби' in self.cards \
                or '9 - Крести' in self.cards or '9 - Пики' in self.cards:
            self.score += 9
        if '10 - Черви' in self.cards or '10 - Буби' in self.cards \
                or '10 - Крести' in self.cards or '10 - Пики' in self.cards:
            self.score += 10
        if 'Валет - Черви' in self.cards or 'Валет - Буби' in self.cards \
                or 'Валет - Крести' in self.cards or 'Валет - Пики' in self.cards:
            self.score += 10
        if 'Дама - Черви' in self.cards or 'Дама - Буби' in self.cards \
                or 'Дама - Крести' in self.cards or 'Дама - Пики' in self.cards:
            self.score += 10
        if 'Король - Черви' in self.cards or 'Король - Буби' in self.cards \
                or 'Король - Крести' in self.cards or 'Король - Пики' in self.cards:
            self.score += 10
        if 'Туз - Черви' in self.cards or 'Туз - Буби' in self.cards \
                or 'Туз - Крести' in self.cards or 'Туз - Пики' in self.cards:
            if self.score < 21:
                self.score += 11
            else:
                self.score += 1


class Diller:
    cards = []
    score = 0

    def take_card(self):
        self.cards.append(Card().amount)
        self.score_up()

    def score_up(self):
        if '2 - Черви' in self.cards or '2 - Буби' in self.cards \
                or '2 - Крести' in self.cards or '2 - Пики' in self.cards:
            self.score += 2
        if '3 - Черви' in self.cards or '3 - Буби' in self.cards \
                or '3 - Крести' in self.cards or '3 - Пики' in self.cards:
            self.score += 3
        if '4 - Черви' in self.cards or '4 - Буби' in self.cards \
                or '4 - Крести' in self.cards or '4 - Пики' in self.cards:
            self.score += 4
        if '5 - Черви' in self.cards or '5 - Буби' in self.cards \
                or '5 - Крести' in self.cards or '5 - Пики' in self.cards:
            self.score += 5
        if '6 - Черви' in self.cards or '6 - Буби' in self.cards \
                or '6 - Крести' in self.cards or '6 - Пики' in self.cards:
            self.score += 6
        if '7 - Черви' in self.cards or '7 - Буби' in self.cards \
                or '7 - Крести' in self.cards or '7 - Пики' in self.cards:
            self.score += 7
        if '8 - Черви' in self.cards or '8 - Буби' in self.cards \
                or '8 - Крести' in self.cards or '8 - Пики' in self.cards:
            self.score += 8
        if '9 - Черви' in self.cards or '9 - Буби' in self.cards \
                or '9 - Крести' in self.cards or '9 - Пики' in self.cards:
            self.score += 9
        if '10 - Черви' in self.cards or '10 - Буби' in self.cards \
                or '10 - Крести' in self.cards or '10 - Пики' in self.cards:
            self.score += 10
        if 'Валет - Черви' in self.cards or 'Валет - Буби' in self.cards \
                or 'Валет - Крести' in self.cards or 'Валет - Пики' in self.cards:
            self.score += 10
        if 'Дама - Черви' in self.cards or 'Дама - Буби' in self.cards \
                or 'Дама - Крести' in self.cards or 'Дама - Пики' in self.cards:
            self.score += 10
        if 'Король - Черви' in self.cards or 'Король - Буби' in self.cards \
                or 'Король - Крести' in self.cards or 'Король - Пики' in self.cards:
            self.score += 10
        if 'Туз - Черви' in self.cards or 'Туз - Буби' in self.cards \
                or 'Туз - Крести' in self.cards or 'Туз - Пики' in self.cards:
            if self.score < 21:
                self.score += 11
            else:
                self.score += 1


class Card:
    amount_list = [
        '2 - Черви', '3 - Черви', '4 - Черви', '5 - Черви', '6 - Черви', '7 - Черви', '8 - Черви', '9 - Черви',
        '10 - Черви', 'Валет - Черви', 'Дама - Черви', 'Король - Черви', 'Туз - Черви',
        '2 - Буби', '3 - Буби', '4 - Буби', '5 - Буби', '6 - Буби', '7 - Буби', '8 - Буби', '9 - Буби',
        '10 - Буби', 'Валет - Буби', 'Дама - Буби', 'Король - Буби', 'Туз - Буби',
        '2 - Крести', '3 - Крести', '4 - Крести', '5 - Крести', '6 - Крести', '7 - Крести', '8 - Крести',
        '9 - Крести', '10 - Крести', 'Валет - Крести', 'Дама - Крести', 'Король - Крести', 'Туз - Крести',
        '2 - Пики', '3 - Пики', '4 - Пики', '5 - Пики', '6 - Пики', '7 - Пики', '8 - Пики', '9 - Пики',
        '10 - Пики', 'Валет - Пики', 'Дама - Пики', 'Король - Пики', 'Туз - Пики'
    ]

    def __init__(self):
        self.amount = random.choice(self.amount_list)
        self.amount_list.pop(self.amount_list.index(self.amount))


def play_the_game(p, d):
    for _ in range(2):
        p.take_card()
        d.take_card()
    p.info()
    if p.score > 21:
        print('Ты проиграл.')
        exit()
    elif d.score > 21:
        print('У диллера {}. Ты выйграл!'.format(d.score))
        exit()
    elif p.score == 21:
        print('Ты выйграл.')
        exit()
    while p.score != 21:
        print('Еще карту?')
        answer = input()
        if answer == 'Еще':
            p.take_card()
            p.info()
        elif answer == 'Себе':
            d.take_card()
        if p.score > 21:
            print('Ты проиграл.')
            break
        elif d.score > 21:
            print('У диллера {}. Ты выйграл!'.format(d.score))
            break
        elif p.score == 21:
            print('Ты выйграл.')



p = PlayerHand()
d = Diller()
play_the_game(p, d)
