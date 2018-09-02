# Task
# https://gist.github.com/sargo/8c75ba58790b230fcf08

from grot_element import GrotElement
from position import Position


class Board:
    def __init__(self, board_description):
        self.__board = self.create_board(board_description)

    def create_board(self, board_description):
        Position.max_x = len(board_description) - 1
        Position.max_y = len(board_description[0]) - 1
        for index_x, row in enumerate(board_description):
            for index_y, grot in enumerate(row):
                board_description[index_x][index_y] = GrotElement.map_grot_to_move(grot)
        return board_description

    def get_grot_element(self, position):
        return self.__board[position.x][position.y]

    def __iter__(self):
        for index_x, row in enumerate(self.__board):
            for index_y, direction in enumerate(row):
                yield Position(index_x, index_y), direction

    def unghost_all(self):
        for index_x, row in enumerate(self.__board):
            for index_y, direction in enumerate(row):
                direction.ghost = False
