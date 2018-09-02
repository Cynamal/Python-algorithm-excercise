# Task
# https://gist.github.com/sargo/8c75ba58790b230fcf08

class Position:
    max_x = None
    max_y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, position):
        self.x += position.x
        self.y += position.y
        return self

    def __str__(self):
        return f'X: {self.x} Y: {self.y}'

    @property
    def in_board(self):
        if 0 <= self.x <= Position.max_x and 0 <= self.y <= Position.max_y:
            return True
        return False

