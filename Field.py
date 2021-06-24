from P import P
from random import randint


class Field:
    def __init__(self):
        self.field: list = [
            [P(c, r, val=randint(1, 22) == 3) for c in range(20)] for r in range(20)
        ]

    def try_to_catch(self, p: P):
        if self.field[p.y][p.x].catchable and not self.field[p.y][p.x].caught:
            self.field[p.y][p.x].caught = True
            return True
        return False

    def __list__(self):
        return \
            [
                'P  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20',
                *[
                    ''.join([f'{r+1}  ' if len(str(r+1)) == 1 else f'{r+1} ',
                             *['O  ' if not p.catchable else 'X  ' if not p.caught else '=  ' for p in self.field[r]]
                             ]) for r in range(len(self.field))]
            ]
