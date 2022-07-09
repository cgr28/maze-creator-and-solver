from grid import Grid
from helpers import *
from maze_solver.helpers import *
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
