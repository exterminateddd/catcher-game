from Field import Field
from pprint import pprint
from itertools import chain


class Game:
    def __init__(self, field: Field):
        self.field = field
        self.count = 0
        self.messages = []
        self.current_bonus = 0

    def set_bonus(self, val: int):
        self.current_bonus = val

    def add_msg(self, msg: str):
        self.messages.append(msg)

    def increase_count(self, val):
        self.count += val + self.current_bonus

    def decrease_count(self):
        self.count -= 1 if self.count >= 1 else 0

    def get_caught_points(self):
        return list(chain(*[[c for c in r if c.caught] for r in self.field.field]))

    def output(self):
        pprint(self.field.__list__())
        print('  =' * 10 + '-  ' + str(self.count) + '  -' + 10 * '=  ')
        print((self.messages[-1] + '  ' + (65-len(self.messages[-1])) * '*') if self.messages else '')

    def __int__(self):
        return self.count
