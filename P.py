class P:
    def __init__(self, x: int, y: int, val: bool = False, caught: bool = False, hidden: bool = False):
        self.x = x
        self.y = y
        self.catchable = val
        self.caught = caught
        self.hidden = hidden
