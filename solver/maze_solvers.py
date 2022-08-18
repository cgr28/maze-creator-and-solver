from grid import Grid
from helpers import *
from solver.helpers import *
import sys
from collections import deque


class MazeSolvers:
    @staticmethod
    def depth_first_search(maze: Grid, start: tuple, end: tuple):
        start_row, start_col = start
        stack = [(start_row, start_col, [])]
        vis = set()
        while stack:
            row, col, path = stack.pop()
            pos = (row, col)

            path += [pos]

            if pos == end:
                return (path, list(vis))

            if pos in vis:
                continue

            vis.add(pos)

            if Helpers.can_move(maze, pos, UP):
                new_row, new_col = Helpers.move(pos, UP)
                stack.append((new_row, new_col, path.copy()))
            if Helpers.can_move(maze, pos, DOWN):
                new_row, new_col = Helpers.move(pos, DOWN)
                stack.append((new_row, new_col, path.copy()))
            if Helpers.can_move(maze, pos, LEFT):
                new_row, new_col = Helpers.move(pos, LEFT)
                stack.append((new_row, new_col, path.copy()))
            if Helpers.can_move(maze, pos, RIGHT):
                new_row, new_col = Helpers.move(pos, RIGHT)
                stack.append((new_row, new_col, path.copy()))

        return None  # there is no solution

    @staticmethod
    def breadth_first_search(maze: Grid, start: tuple, end: tuple):
        start_row, start_col = start
        que = deque([(start_row, start_col, [])])
        vis = set()
        while que:
            row, col, path = que.popleft()
            pos = (row, col)
            path += [pos]

            if pos == end:
                return (path, list(vis))

            if pos in vis:
                continue

            vis.add(pos)

            if Helpers.can_move(maze, pos, UP):
                new_row, new_col = Helpers.move(pos, UP)
                que.append((new_row, new_col, path.copy()))
            if Helpers.can_move(maze, pos, DOWN):
                new_row, new_col = Helpers.move(pos, DOWN)
                que.append((new_row, new_col, path.copy()))
            if Helpers.can_move(maze, pos, LEFT):
                new_row, new_col = Helpers.move(pos, LEFT)
                que.append((new_row, new_col, path.copy()))
            if Helpers.can_move(maze, pos, RIGHT):
                new_row, new_col = Helpers.move(pos, RIGHT)
                que.append((new_row, new_col, path.copy()))

        return None  # there is no solution

    @staticmethod
    def best_first_search(maze: Grid, start: tuple, end: tuple):
        start_row, start_col = start
        pot = [(start_row, start_col, [])]
        vis = set()

        while pot:
            min_cell_index = 0
            for i in range(len(pot)):
                # print(pot[i][0])
                if Helpers.manhattan_distance(pot[i][:-1], end) <= Helpers.manhattan_distance(pot[min_cell_index][:-1], end):
                    min_cell_index = i
            row, col, path = pot.pop(min_cell_index)
            pos = (row, col)
            path += [pos]
            if pos in vis:
                continue

            if pos == end:
                vis.add(pos)
                return (path, list(vis))
            
            vis.add(pos)

            if Helpers.can_move(maze, pos, UP):
                new_row, new_col = Helpers.move(pos, UP)
                if (new_row, new_col) not in vis:
                    pot.append((new_row, new_col, path.copy()))
            if Helpers.can_move(maze, pos, DOWN):
                new_row, new_col = Helpers.move(pos, DOWN)
                if (new_row, new_col) not in vis:
                    pot.append((new_row, new_col, path.copy()))
            if Helpers.can_move(maze, pos, LEFT):
                new_row, new_col = Helpers.move(pos, LEFT)
                if (new_row, new_col) not in vis:
                    pot.append((new_row, new_col, path.copy()))
            if Helpers.can_move(maze, pos, RIGHT):
                new_row, new_col = Helpers.move(pos, RIGHT)
                if (new_row, new_col) not in vis:
                    pot.append((new_row, new_col, path.copy()))

        return None

    @staticmethod
    def a_star(maze: Grid, start: tuple, end: tuple):
        open = [AStarHelpers.Cell(None, 0, Helpers.manhattan_distance(start, end), start)]
        closed = []

        while open:
            min_cell_pos = 0

            # finds lowest f in open
            for i in range(len(open)):
                if open[i].f <= open[min_cell_pos].f:
                    min_cell_pos = i
                
            min_cell = open.pop(min_cell_pos)
            closed.append(min_cell)

            if min_cell.pos == end:
                return min_cell.get_root(), AStarHelpers.vis_path(closed)

            for dir in [UP, DOWN, LEFT, RIGHT]:
                if not Helpers.can_move(maze, min_cell.pos, dir):
                    continue
                pot_pos = Helpers.move(min_cell.pos, dir)
                pot = AStarHelpers.Cell(min_cell, min_cell.g+1, Helpers.manhattan_distance(pot_pos, end), pot_pos)

                if AStarHelpers.contains_cell(pot, closed) != False:
                    continue
                pos_in_open = AStarHelpers.contains_cell(pot, open)
                if pos_in_open == False:
                    open.append(pot)
                else:
                    og = open[pos_in_open]
                    if pot.f < og.f:
                        og.new_parent(min_cell)
        return None