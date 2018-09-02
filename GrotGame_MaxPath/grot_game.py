# Task
# https://gist.github.com/sargo/8c75ba58790b230fcf08

from copy import copy

from board import Board


class GrotGame:
    def __init__(self, board):
        self.moves = 0
        self.max = 0
        self.position = None
        self.found_position = None
        self.board = Board(board)

    def start_game(self):
        for i in self.board:
            self.position = copy(i[0])
            grot_element = i[1]
            if not grot_element.visited:
                self.check_path(grot_element)
                if self.max < self.moves:
                    self.max = self.moves
                    self.found_position = i[0]
                self.moves = 0
                self.board.unghost_all()

    def longest_path(self):
        print(f'Max path: {self.max} Start position: [{self.found_position}]')

    def check_path(self, grot_element):
        grot_element.visited = True
        grot_element.ghost = True
        self.moves += 1

        while True:
            self.position += grot_element.move
            if not self.position.in_board:
                break
            next_direction = self.board.get_grot_element(self.position)
            if not next_direction.ghost:
                    self.check_path(next_direction)
                    break


def main():

    sample = [
        ['u', 'd', 'u', 'u'],  # ↑ ↓ ↑ ↑
        ['u', 'r', 'l', 'l'],  # ↑ → ← ←
        ['u', 'u', 'l', 'u'],  # ↑ ↑ ← ↑
        ['l', 'd', 'u', 'l'],  # ← ↓ ↑ ←
    ]

    game = GrotGame(sample)
    game.start_game()
    game.longest_path()


main()
