from enums import Moves


class Helpers:
    @staticmethod
    def move(pos, direction):
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
    # ensures that the potential move doesn't have walls, or isn't OOB
    def can_move(maze, pos, direction):
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
    def manhattan_distance(pos, end):
        row, col = pos
        end_row, end_col = end
        return abs(row - end_row) + abs(col - end_col)


class AStarHelpers:
    class Cell:
        def __init__(self, parent, g, h, pos):
            self.g = g
            self.h = h
            self.f = g + h
            self.pos = pos
            self.parent = parent

        def new_parent(self, parent):
            self.parent = parent
            self.g = parent.g + 1
            self.f = self.g + self.h

        def get_root(self):
            path_to_root = [self.pos]
            elem = self.parent
            while elem:
                path_to_root.append(elem.pos)
                elem = elem.parent
            return path_to_root

    @staticmethod
    def contains_cell(cell, lst):
        for i in range(len(lst)):
            if lst[i].pos == cell.pos:
                return i
        return False

    @staticmethod
    def vis_path(lst):
        ret = []
        for i in range(len(lst)):
            ret.append(lst[i].pos)
        return ret
