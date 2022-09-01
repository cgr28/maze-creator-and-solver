import random
from enums import Moves


class Cell:
    def __init__(self):
        self.right = True
        self.left = True
        self.up = True
        self.down = True
        self.vis = False
        self.val = random.random()


class Grid:
    def __init__(self, height, width):
        self.grid = [[Cell() for i in range(width)] for j in range(height)]
        self.height = height
        self.width = width

    def get_cell(self, pos):
        row, col = pos
        return self.grid[row][col]

    # gets position to the left, right, up, or down of given pos
    def get_pos(self, pos, wall):
        row, col = pos
        if wall == Moves.LEFT:
            pot = (row, col - 1)
        elif wall == Moves.RIGHT:
            pot = (row, col + 1)
        elif wall == Moves.UP:
            pot = (row - 1, col)
        elif wall == Moves.DOWN:
            pot = (row + 1, col)
        else:
            return None
        return pot

    # ensures that pos isn't out of bounds
    def valid_pos(self, pos):
        pot_row, pot_col = pos
        if pot_row < 0 or pot_row >= self.height:
            return False
        if pot_col < 0 or pot_col >= self.width:
            return False
        return True

    # checks if a wall can be removed
    def can_remove(self, pos, wall):
        pot = self.get_pos(pos, wall)  # potential position

        if not self.valid_pos(pot):
            return False
        return True

    # checks whether a wall can be removed and is unvisitied
    def can_remove_and_unvis(self, pos, wall):
        pot = self.get_pos(pos, wall)  # potential position
        pot_row, pot_col = pot

        if not self.valid_pos(pot):
            return False
        if self.is_vis((pot_row, pot_col)):
            return False
        return True

    def remove_wall(self, pos, wall):
        row, col = pos
        if wall == Moves.LEFT:
            pot = (row, col - 1)
            pot_row, pot_col = pot
            self.get_cell((row, col)).left = False
            self.get_cell((pot_row, pot_col)).right = False
        if wall == Moves.RIGHT:
            pot = (row, col + 1)
            pot_row, pot_col = pot
            self.get_cell((row, col)).right = False
            self.get_cell((pot_row, pot_col)).left = False
        if wall == Moves.UP:
            pot = (row - 1, col)
            pot_row, pot_col = pot
            self.get_cell((row, col)).up = False
            self.get_cell((pot_row, pot_col)).down = False
        if wall == Moves.DOWN:
            pot = (row + 1, col)
            pot_row, pot_col = pot
            self.get_cell((row, col)).down = False
            self.get_cell((pot_row, pot_col)).up = False
        return pot

    # checks if a cell has been visited
    def is_vis(self, pos):
        return self.get_cell(pos).vis

    def mark_vis(self, pos):
        self.get_cell(pos).vis = True
