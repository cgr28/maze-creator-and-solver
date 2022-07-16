from grid import Grid
from helpers import *
from maze_solver.helpers import *
import sys
from collections import deque


class MazeSolvers:
    @staticmethod
    def dfs(maze: Grid, start: tuple, end: tuple):
        start_row, start_col = start
        stack = [(start_row, start_col, [])]
        vis = set()
        while stack:
            row, col, path = stack.pop()
            # print(row, col)
            path += [(row, col)]

            if (row, col) == end:
                return (path, list(vis))

            if (row, col) in vis:
                continue

            vis.add((row, col))

            if can_move(maze, (row, col), UP):
                new_row, new_col = move((row, col), UP)
                stack.append((new_row, new_col, path.copy()))
            if can_move(maze, (row, col), DOWN):
                new_row, new_col = move((row, col), DOWN)
                stack.append((new_row, new_col, path.copy()))
            if can_move(maze, (row, col), LEFT):
                new_row, new_col = move((row, col), LEFT)
                stack.append((new_row, new_col, path.copy()))
            if can_move(maze, (row, col), RIGHT):
                new_row, new_col = move((row, col), RIGHT)
                stack.append((new_row, new_col, path.copy()))

        return None  # there is no solution

    @staticmethod
    def bfs(maze: Grid, start: tuple, end: tuple):
        start_row, start_col = start
        que = deque([(start_row, start_col, [])])
        vis = set()
        while que:
            row, col, path = que.popleft()
            # print(row, col)
            path += [(row, col)]

            if (row, col) == end:
                return (path, list(vis))

            if (row, col) in vis:
                continue

            vis.add((row, col))

            if can_move(maze, (row, col), UP):
                new_row, new_col = move((row, col), UP)
                que.append((new_row, new_col, path.copy()))
            if can_move(maze, (row, col), DOWN):
                new_row, new_col = move((row, col), DOWN)
                que.append((new_row, new_col, path.copy()))
            if can_move(maze, (row, col), LEFT):
                new_row, new_col = move((row, col), LEFT)
                que.append((new_row, new_col, path.copy()))
            if can_move(maze, (row, col), RIGHT):
                new_row, new_col = move((row, col), RIGHT)
                que.append((new_row, new_col, path.copy()))

        return None  # there is no solution

    # @staticmethod
    # def a_star(maze: Grid, start: tuple, end: tuple):
    #     end_row, end_col = end
    #     open = [AStarCell(None, 0, get_heuristic(start, end), start)]
    #     closed = []
    #     path = []

    #     while open:
    #         min_i = 0

    #         # finds lowest f in open
    #         for i in range(len(open)):
    #             if open[i].f <= open[min_i].f:
    #                 min_i = i
                
    #         min_cell = open.pop(min_i)
    #         path.append(min_cell.pos)

    #         if min_cell.pos == end:
    #             return path

    #         closed.append(min_cell)

    #         for dir in [UP, DOWN, LEFT, RIGHT]:
    #             if not can_move(maze, min_cell.pos, dir):
    #                 continue
    #             pot_pos = move(min_cell.pos, dir)
    #             pot = AStarCell(min_cell, min_cell.g+1, get_heuristic(pot_pos, end), pot_pos)
    #             if pot in closed:
    #                 print("108")
    #                 continue
    #             if pot not in open:
    #                 open.append(pot)
    #             else:
    #                 index = open.index(pot)
    #                 og = open[index]
    #                 if pot.g < og.g:
    #                     og.new_parent(min_cell)
    #     return None