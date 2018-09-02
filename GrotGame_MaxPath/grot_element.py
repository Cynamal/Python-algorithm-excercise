# Task
# https://gist.github.com/sargo/8c75ba58790b230fcf08

from position import Position


class GrotElement:
    grot_symbol_mapping = {
        'u': (-1, 0),
        'd': (1, 0),
        'l': (0, -1),
        'r': (0, 1)
    }

    def __init__(self, position, grot, visited=False, ghost=False):
        self.move = Position(position[0], position[1])
        self.grot = grot
        self.visited = visited
        self.ghost = ghost

    @classmethod
    def map_grot_to_move(cls, grot):
        return cls(cls.grot_symbol_mapping[grot], grot)
