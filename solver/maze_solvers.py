from grid import Grid
from enums import Moves
from solver.helpers import *
from collections import deque


class MazeSolvers:
    """A collection of maze solvers."""

    @staticmethod
    def depth_first_search(maze: Grid, start: tuple, end: tuple):
        """Gets the depth first search solution to a maze. Solution not guaranteed to be optimal.

        Args:
            maze (Grid): Maze that will searched for solution.
            start (tuple): Starting position.
            end (tuple): Ending position.

        Returns:
            tuple:
                list: Contains the positions of cells in the solution path.
                list: Contains the positions of visited cells.
                    or
            None: Couldn't find a solution.
        """
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

            if Helpers.can_move(maze, pos, Moves.UP):
                new_row, new_col = Helpers.move(pos, Moves.UP)
                stack.append((new_row, new_col, path.copy()))
            if Helpers.can_move(maze, pos, Moves.DOWN):
                new_row, new_col = Helpers.move(pos, Moves.DOWN)
                stack.append((new_row, new_col, path.copy()))
            if Helpers.can_move(maze, pos, Moves.LEFT):
                new_row, new_col = Helpers.move(pos, Moves.LEFT)
                stack.append((new_row, new_col, path.copy()))
            if Helpers.can_move(maze, pos, Moves.RIGHT):
                new_row, new_col = Helpers.move(pos, Moves.RIGHT)
                stack.append((new_row, new_col, path.copy()))

        return None  # there is no solution

    @staticmethod
    def breadth_first_search(maze: Grid, start: tuple, end: tuple):
        """Gets the breadth first search solution to a maze.  Solution guaranteed to be optimal.

        Args:
            maze (Grid): Maze that will searched for solution.
            start (tuple): Starting position.
            end (tuple): Ending position.

        Returns:
            tuple:
                list: Contains the positions of cells in the solution path.
                list: Contains the positions of visited cells.
                    or
            None: Couldn't find a solution.
        """
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

            if Helpers.can_move(maze, pos, Moves.UP):
                new_row, new_col = Helpers.move(pos, Moves.UP)
                que.append((new_row, new_col, path.copy()))
            if Helpers.can_move(maze, pos, Moves.DOWN):
                new_row, new_col = Helpers.move(pos, Moves.DOWN)
                que.append((new_row, new_col, path.copy()))
            if Helpers.can_move(maze, pos, Moves.LEFT):
                new_row, new_col = Helpers.move(pos, Moves.LEFT)
                que.append((new_row, new_col, path.copy()))
            if Helpers.can_move(maze, pos, Moves.RIGHT):
                new_row, new_col = Helpers.move(pos, Moves.RIGHT)
                que.append((new_row, new_col, path.copy()))

        return None  # there is no solution

    @staticmethod
    def best_first_search(maze: Grid, start: tuple, end: tuple):
        """Gets the best first search solution to a maze.  Solution not guaranteed to be optimal.

        Args:
            maze (Grid): Maze that will searched for solution.
            start (tuple): Starting position.
            end (tuple): Ending position.

        Returns:
            tuple:
                list: Contains the positions of cells in the solution path.
                list: Contains the positions of visited cells.
                    or
            None: Couldn't find a solution.
        """
        start_row, start_col = start
        pot = [(start_row, start_col, [])]
        vis = set()

        while pot:
            min_cell_index = 0
            for i in range(len(pot)):
                if Helpers.manhattan_distance(
                    pot[i][:-1], end
                ) <= Helpers.manhattan_distance(pot[min_cell_index][:-1], end):
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

            if Helpers.can_move(maze, pos, Moves.UP):
                new_row, new_col = Helpers.move(pos, Moves.UP)
                if (new_row, new_col) not in vis:
                    pot.append((new_row, new_col, path.copy()))
            if Helpers.can_move(maze, pos, Moves.DOWN):
                new_row, new_col = Helpers.move(pos, Moves.DOWN)
                if (new_row, new_col) not in vis:
                    pot.append((new_row, new_col, path.copy()))
            if Helpers.can_move(maze, pos, Moves.LEFT):
                new_row, new_col = Helpers.move(pos, Moves.LEFT)
                if (new_row, new_col) not in vis:
                    pot.append((new_row, new_col, path.copy()))
            if Helpers.can_move(maze, pos, Moves.RIGHT):
                new_row, new_col = Helpers.move(pos, Moves.RIGHT)
                if (new_row, new_col) not in vis:
                    pot.append((new_row, new_col, path.copy()))

        return None

    @staticmethod
    def a_star(maze: Grid, start: tuple, end: tuple):
        """Gets A* solution to a maze.  Solution guaranteed to be optimal.

        Args:
            maze (Grid): Maze that will searched for solution.
            start (tuple): Starting position.
            end (tuple): Ending position.

        Returns:
            tuple:
                list: Contains the positions of cells in the solution path.
                list: Contains the positions of visited cells.
                    or
            None: Couldn't find a solution.
        """
        open = [
            AStarHelpers.Cell(None, 0, Helpers.manhattan_distance(start, end), start)
        ]
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
                return (min_cell.get_root(), AStarHelpers.vis_path(closed))

            for dir in [Moves.UP, Moves.DOWN, Moves.LEFT, Moves.RIGHT]:
                if not Helpers.can_move(maze, min_cell.pos, dir):
                    continue
                pot_pos = Helpers.move(min_cell.pos, dir)
                pot = AStarHelpers.Cell(
                    min_cell,
                    min_cell.g + 1,
                    Helpers.manhattan_distance(pot_pos, end),
                    pot_pos,
                )

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
