from enums import Moves


class Helpers:
    @staticmethod
    def move(pos, direction):
        """Generates the positon

        Args:
            pos (tuple): Starting position.
            direction (int): Direction of move.

        Returns:
            tuple: Position after moving in direction
        """
        row, col = pos
        if direction == Moves.RIGHT:
            ret = (row, col + 1)
        elif direction == Moves.LEFT:
            ret = (row, col - 1)
        elif direction == Moves.UP:
            ret = (row - 1, col)
        else:  # direction == Moves.DOWN
            ret = (row + 1, col)

        return ret

    @staticmethod
    def can_move(maze, pos, direction):
        """Ensures potential move isn't out of bounds or blocked by a wall.

        Args:
            maze (Grid): The maze being checked.
            pos (tuple): Starting position.
            direction (int): Direction of move.

        Returns:
            bool
        """
        cell = maze.get_cell(pos)

        if direction == Moves.RIGHT:
            if cell.right:
                return False
        elif direction == Moves.LEFT:
            if cell.left:
                return False
        elif direction == Moves.UP:
            if cell.up:
                return False
        else:  # direction == Moves.DOWN
            if cell.down:
                return False

        row, col = Helpers.move(pos, direction)
        if col < 0 or col >= maze.width:
            return False

        if row < 0 or row >= maze.height:
            return False

        return True

    @staticmethod
    def manhattan_distance(start, end):
        """Distance between two positions using the manhattan distance i.e. |x1 - x2| + |y1 - y2|.

        Args:
            start (tuple): Starting position.
            end (tuple): End position.

        Returns:
            int: Distance between two positions.
        """
        row, col = start
        end_row, end_col = end
        return abs(row - end_row) + abs(col - end_col)


class AStarHelpers:
    class Cell:
        """Represents a cell or state in A*.
        """
        def __init__(self, parent, g, h, pos):
            """
            Args:
                parent (Cell): The cell's parent cell.
                g (int): Cost to get to state.
                h (int): Estimated cost to get from current state to goal.
                pos (tuple): Position on maze.
            """
            self.g = g
            self.h = h
            self.f = g + h
            self.pos = pos
            self.parent = parent

        def new_parent(self, parent):
            """Assigns cell a new parent.

            Args:
                parent (Cell): The cell's new parent.
            """
            self.parent = parent
            self.g = parent.g + 1
            self.f = self.g + self.h

        def get_root(self):
            """The path to get to the current cell.

            Returns:
                list: List of cells.
            """
            path_to_root = [self.pos]
            elem = self.parent
            while elem:
                path_to_root.append(elem.pos)
                elem = elem.parent
            return path_to_root

    @staticmethod
    def contains_cell(cell, lst):
        """Iterates through a list to check if it contains a given cell.

        Args:
            cell (Cell): The given cell.
            lst (list): The list that will be iterated through.

        Returns:
            bool
        """
        for i in range(len(lst)):
            if lst[i].pos == cell.pos:
                return i
        return False

    @staticmethod
    def vis_path(lst):
        """Gets the position of each cell in a list.

        Args:
            lst (list): List of Cells.

        Returns:
            list: List of positions.
        """
        ret = []
        for i in range(len(lst)):
            ret.append(lst[i].pos)
        return ret
