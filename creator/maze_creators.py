from grid import Grid
import random
from helpers import *
from creator.helpers import *


class MazeCreators:
    @staticmethod
    def hunt_and_kill(size: int):
        grid = Grid(size)
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
                    index = 0
                else:
                    index = random.randint(0, len(options) - 1)
                move = options.pop(index)
                if grid.can_remove_and_unvis((row, col), move):
                    begin_hunt = False
                    new = grid.remove_wall((row, col), move)
                    newRow, newCol = new
                    stack.append(new)
                    break
            grid.mark_vis((row, col))

            if begin_hunt:
                hunt_pos, move = HuntAndKillHelpers.hunt(size, grid)
                # print("hunt ", hunt_pos, move)
                if hunt_pos:
                    pos = grid.remove_wall(hunt_pos, move)
                    stack.append(pos)
                    begin_hunt = False
                else:
                    return grid
    
    @staticmethod
    def growing_tree(size: int):
        grid = Grid(size)
        row, col = (random.randint(0, size-1), random.randint(0, size-1))
        stack = []

        while True:
            begin_unravel = True
            stack.append((row, col))
            grid.mark_vis((row, col))
            options = [LEFT, RIGHT, UP, DOWN]
            while options:
                if len(options) == 1:
                    index = 0
                else:
                    index = random.randint(0, len(options) - 1)
                move = options.pop(index)
                if grid.can_remove_and_unvis((row, col), move):
                    new_pos = grid.remove_wall((row, col), move)
                    begin_unravel = False
                    break

            if begin_unravel:
                unravel_pos = GrowingTreeHelpers.unravel(stack, grid)
                if unravel_pos:
                    row, col = unravel_pos
                else:
                    return grid
            else:
                row, col = new_pos
        
    @staticmethod
    def prims(size: int):
        row, col = (random.randint(0, size-1), random.randint(0, size-1)) # starting row and col
        grid = Grid(size)
        curr_cell = (row, col)
        adj_cells = [] # yet to visit adjacent cells
        # adding cells that are adjacent to starting cell
        for move in [LEFT, RIGHT, UP, DOWN]:
                if grid.can_remove_and_unvis(curr_cell, move):
                    pot_pos = grid.get_pos(curr_cell, move)
                    adj_cells.append(pot_pos)

        grid.mark_vis(curr_cell)
        while adj_cells:
            # pop a random cell from adj cell
            if len(adj_cells) == 1:
                index = 0
            else:
                index = random.randint(0, len(adj_cells) - 1)
            curr_cell = adj_cells.pop(index)
            grid.mark_vis(curr_cell)

            options = [LEFT, RIGHT, UP, DOWN]
            # removing a random wall
            while options:
                if len(options) == 0:
                    break
                elif len(options) == 1:
                    index = 0
                else:
                    index = random.randint(0, len(options) - 1)
                move = options.pop(index)
                if grid.can_remove(curr_cell, move):
                    pot_pos = grid.get_pos(curr_cell, move)
                    if grid.is_vis(pot_pos):
                        grid.remove_wall(curr_cell, move)
                        break
            # adding adjacent cells
            for move in [LEFT, RIGHT, UP, DOWN]:
                if grid.can_remove(curr_cell, move):
                    pot_pos = grid.get_pos(curr_cell, move)
                    if not grid.is_vis(pot_pos) and (pot_pos not in adj_cells):
                        adj_cells.append(pot_pos)
        return grid
            
            