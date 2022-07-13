from grid import Grid
import random
from helpers import *


class MazeCreators:
    @staticmethod
    def hunt_and_kill(size: int):
        grid = Grid(size)

        # checks whether cell can hunt
        # if possible returns move
        def can_hunt(pos):
            options = [LEFT, RIGHT, UP, DOWN]
            row, col = pos
            if grid.get_cell((row, col)).vis:
                return None

            while options:
                if len(options) == 0:
                    return False
                elif len(options) == 1:
                    pot_move = 0
                else:
                    pot_move = random.randint(0, len(options) - 1)

                move = options.pop(pot_move)
                pot = grid.get_pos(pos, move)
                pot_row, pot_col = pot

                if not grid.valid_pos(pot):
                    continue

                if grid.get_cell((pot_row, pot_col)).vis == True:
                    return move
            return None

        def hunt():
            for i in range(grid.size):
                for j in range(grid.size):
                    pot_move = can_hunt((i, j))
                    # print((i, j), pot_move)
                    if pot_move:
                        return ((i, j), pot_move)
            return (None, None)

        stack = [(0, 0)]
        begin_hunt = False
        while True:
            options = [LEFT, RIGHT, UP, DOWN]
            if not begin_hunt:
                row, col = stack.pop()

            while not begin_hunt:
                if len(options) == 0:
                    begin_hunt = True
                    break
                elif len(options) == 1:
                    pot_move = 0
                else:
                    pot_move = random.randint(0, len(options) - 1)
                move = options.pop(pot_move)
                # print(type(grid.can_remove((row, col), move)))
                if grid.can_remove((row, col), move):
                    begin_hunt = False
                    new = grid.remove_wall((row, col), move)
                    newRow, newCol = new
                    stack.append(new)
                    break
            grid.get_cell((row, col)).vis = True

            if begin_hunt:
                hunt_pos, move = hunt()
                # print("hunt ", hunt_pos, move)
                if hunt_pos:
                    pos = grid.remove_wall(hunt_pos, move)
                    stack.append(pos)
                    begin_hunt = False
                else:
                    return grid
