import random
from enums import Moves


class HuntAndKillHelpers:
    """A collection of helper methods for the Hunt and Kill algorithm.
    """
    
    @staticmethod
    def can_hunt(pos, grid):
        """Decides if Hunt and Kill algorithm can begin \"hunt\".

        Args:
            pos (_type_): Position.
            grid (_type_): Grid to be checked for hunt.

        Returns:
            None: Can't begin hunt.
                or
            int: Direction of move that should be used for hunt.
        """
        options = [Moves.LEFT, Moves.RIGHT, Moves.UP, Moves.DOWN]
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
        """Completes the hunt for the Hunt and Kill algorithm.

        Args:
            height (_type_): Height of grid.
            width (_type_): Width of grid.
            grid (_type_): Grid where hunt will completed.

        Returns:
            tuple:
                tuple: Position where kill should be continued from.
                int: Next move that should be completed.
                    or
                None: Maze is complete.
        """
        for i in range(height):
            for j in range(width):
                move = HuntAndKillHelpers.can_hunt((i, j), grid)
                if move:
                    return ((i, j), move)
        return (None, None)


class GrowingTreeHelpers:
    """A collection of helper methods for the Growing Tree algorithm.
    """

    @staticmethod
    def unravel(stack, grid):
        """Unravels the Growing Tree stack until it finds a valid cell.

        Args:
            stack (list): Stack that will be unraveled.
            grid (Grid): The grid to unravel on.

        Returns:
            tuple: Position after the unraveling.
                or
            None: Maze is complete.
        """
        while stack:
            row, col = stack.pop()
            options = [Moves.LEFT, Moves.RIGHT, Moves.UP, Moves.DOWN]

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
