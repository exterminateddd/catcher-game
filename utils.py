from random import randint


def chance(top: int, bottom: int):
    return randint(1, top) == bottom


def rem_space(val: str, maxlength: int = 2):
    return val + ' '*(maxlength-len(val)) if len(val) < maxlength else val
