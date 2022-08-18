from os import stat
import random
from helpers import *

class HuntAndKillHelpers:

    @staticmethod
    def can_hunt(pos, grid):
                options = [LEFT, RIGHT, UP, DOWN]
                row, col = pos
                if grid.get_cell((row, col)).vis:
                    return None

                while options:
                    if len(options) == 0:
                        return False
                    elif len(options) == 1:
                        index = 0
                    else:
                        index = random.randint(0, len(options) - 1)

                    move = options.pop(index)
                    new_pos = grid.get_pos(pos, move)

                    if not grid.valid_pos(new_pos):
                        continue

                    if grid.is_vis(new_pos):
                        return move
                return None

    @staticmethod
    def hunt(height, width, grid):
        for i in range(height):
            for j in range(width):
                move = HuntAndKillHelpers.can_hunt((i, j), grid)
                if move:
                    return ((i, j), move)
        return (None, None)

class GrowingTreeHelpers:

    @staticmethod
    def unravel(stack, grid):
            while stack:
                row, col = stack.pop()
                options = [LEFT, RIGHT, UP, DOWN]

                while options:
                    if len(options) == 0:
                        break
                    elif len(options) == 1:
                        index = 0
                    else:
                        index = random.randint(0, len(options) - 1)

                    move = options.pop(index)
                    pos = grid.get_pos((row, col), move)

                    if not grid.valid_pos(pos):
                        continue

                    if grid.is_vis(pos) == True:
                        continue
                    else:
                        grid.remove_wall((row, col), move)
                        return pos

            return None