from helpers import *


class Cell:
    def __init__(self):
        self.right = True
        self.left = True
        self.up = True
        self.down = True
        self.vis = False


class Grid:
    def __init__(self, size):
        self.grid = [[Cell() for i in range(size)] for j in range(size)]
        self.size = size

    def get_cell(self, pos):
        row, col = pos
        return self.grid[row][col]

    # gets position to the left, right, up, or down of given pos
    def get_pos(self, pos, wall):
        row, col = pos
        if wall == LEFT:
            pot = (row, col - 1)
        elif wall == RIGHT:
            pot = (row, col + 1)
        elif wall == UP:
            pot = (row - 1, col)
        elif wall == DOWN:
            pot = (row + 1, col)
        else:
            return None
        return pot

    # ensures that pos isn't out of bounds
    def valid_pos(self, pos):
        pot_row, pot_col = pos
        if pot_row < 0 or pot_row >= self.size:
            return False
        if pot_col < 0 or pot_col >= self.size:
            return False
        return True

    # checks whether a wall can be removed
    def can_remove(self, pos, wall):
        pot = self.get_pos(pos, wall)  # potential position
        pot_row, pot_col = pot

        if not self.valid_pos(pot):
            return False
        if self.get_cell((pot_row, pot_col)).vis:
            return False
        return True

    def remove_wall(self, pos, wall):
        row, col = pos
        if wall == LEFT:
            pot = (row, col - 1)
            pot_row, pot_col = pot
            self.get_cell((row, col)).left = False
            self.get_cell((pot_row, pot_col)).right = False
        if wall == RIGHT:
            pot = (row, col + 1)
            pot_row, pot_col = pot
            self.get_cell((row, col)).right = False
            self.get_cell((pot_row, pot_col)).left = False
        if wall == UP:
            pot = (row - 1, col)
            pot_row, pot_col = pot
            self.get_cell((row, col)).up = False
            self.get_cell((pot_row, pot_col)).down = False
        if wall == DOWN:
            pot = (row + 1, col)
            pot_row, pot_col = pot
            self.get_cell((row, col)).down = False
            self.get_cell((pot_row, pot_col)).up = False
        return pot
