# Сделай игру крестики-нолики
class Desk:
    cells = {
        'A1': None,
        'A2': None,
        'A3': None,
        'B1': None,
        'B2': None,
        'B3': None,
        'C1': None,
        'C2': None,
        'C3': None
    }


class PlayerX:
    def __init__(self):
        self.name = 'Игрок-1'
        self.mark = 'X'
        self.cell = None

    def choice(self):
        print('В какую ячейку ставите свой знак?')
        self.cell = input()
        if Desk.cells[self.cell] != None:
            return False
        else:
            Desk.cells[self.cell] = self.mark
            return True


class PlayerO:
    name = 'Игрок-2'
    mark = 'O'

    def choice(self):
        print('В какую ячейку ставите свой знак?')
        self.cell = input()
        if Desk.cells[self.cell] != None:
            return False
        else:
            Desk.cells[self.cell] = self.mark
            return True


def lets_play(p_1, p_2):
    winner = 0
    while winner == 0:
        print('Ходит {}'.format(p_1.name))
        choice = p_1.choice()
        if choice:
            print('{} выбрал ячейку {}'.format(p_1.name, p_1.cell))
        while not choice:
            print('Выберите другую ячейку')
            choice = p_1.choice()
            if choice:
                print('{} выбрал ячейку {}'.format(p_1.name, p_1.cell))
        winner = who_win(winner)
        if winner != 0:
            break
        print('Ходит {}'.format(p_2.name))
        choice = p_2.choice()
        if choice:
            print('{} выбрал ячейку {}'.format(p_2.name, p_2.cell))
        while not choice:
            print('Выберите другую ячейку')
            choice = p_2.choice()
            if choice:
                print('{} выбрал ячейку {}'.format(p_2.name, p_2.cell))
        winner = who_win(winner)
        if winner != 0:
            break

def who_win(winner):
    if Desk.cells['A1'] == 'X' and Desk.cells['A2'] == 'X' and Desk.cells['A3'] == 'X' \
            or Desk.cells['A1'] == 'X' and Desk.cells['B2'] == 'X' and Desk.cells['C3'] == 'X' \
            or Desk.cells['C1'] == 'X' and Desk.cells['B2'] == 'X' and Desk.cells['A3'] == 'X' \
            or Desk.cells['A1'] == 'X' and Desk.cells['B1'] == 'X' and Desk.cells['C1'] == 'X' \
            or Desk.cells['A2'] == 'X' and Desk.cells['B2'] == 'X' and Desk.cells['C2'] == 'X' \
            or Desk.cells['A3'] == 'X' and Desk.cells['B3'] == 'X' and Desk.cells['C3'] == 'X' \
            or Desk.cells['A1'] == 'X' and Desk.cells['B1'] == 'X' and Desk.cells['C1'] == 'X' \
            or Desk.cells['A2'] == 'X' and Desk.cells['B2'] == 'X' and Desk.cells['C2'] == 'X' \
            or Desk.cells['A3'] == 'X' and Desk.cells['B3'] == 'X' and Desk.cells['C3'] == 'X':
        winner = p_1
        print('Победил {}'.format(p_1.name))
        return winner
    elif Desk.cells['A1'] == 'O' and Desk.cells['A2'] == 'X' and Desk.cells['A3'] == 'O' \
            or Desk.cells['A1'] == 'O' and Desk.cells['B2'] == 'O' and Desk.cells['C3'] == 'O' \
            or Desk.cells['C1'] == 'O' and Desk.cells['B2'] == 'O' and Desk.cells['A3'] == 'O' \
            or Desk.cells['A1'] == 'O' and Desk.cells['B1'] == 'O' and Desk.cells['C1'] == 'O' \
            or Desk.cells['A2'] == 'O' and Desk.cells['B2'] == 'O' and Desk.cells['C2'] == 'O' \
            or Desk.cells['A3'] == 'O' and Desk.cells['B3'] == 'O' and Desk.cells['C3'] == 'O' \
            or Desk.cells['A1'] == 'O' and Desk.cells['B1'] == 'O' and Desk.cells['C1'] == 'O' \
            or Desk.cells['A2'] == 'O' and Desk.cells['B2'] == 'O' and Desk.cells['C2'] == 'O' \
            or Desk.cells['A3'] == 'O' and Desk.cells['B3'] == 'O' and Desk.cells['C3'] == 'O':
        winner = p_2
        print('Победил {}'.format(p_2.name))
        return winner
    elif not None in Desk.cells.values() and winner == 0:
        print('Ничья')
        winner = 'Ничья'
        return winner
    else:
        return winner


p_1 = PlayerX()
p_2 = PlayerO()
lets_play(p_1, p_2)