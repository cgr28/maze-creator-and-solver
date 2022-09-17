from enums import Moves


class Cell:
    """A cell containing four walls."""

    def __init__(self):
        self.right = True
        self.left = True
        self.up = True
        self.down = True
        self.vis = False


class Grid:
    """A grid of cells, that will be made into a maze."""

    def __init__(self, height, width):
        """
        Args:
            height (int): Height of grid.
            width (int): Width of grid.
        """
        self.grid = [[Cell() for i in range(width)] for j in range(height)]
        self.height = height
        self.width = width

    def get_cell(self, pos):
        """Gets the cell at a given position in the grid.

        Args:
            pos (tuple): Position.

        Returns:
            Cell: The cell at the given position.
        """
        row, col = pos
        return self.grid[row][col]

    def get_pos(self, pos, direction):
        """Gets position to the left, right, up, or down of a given position.

        Args:
            pos (tuple): Starting position.
            direction (int): The direction to get the new position.

        Returns:
            tuple: New position.
                or
            None: Invalid direction given.
        """
        row, col = pos
        if direction == Moves.LEFT:
            pot = (row, col - 1)
        elif direction == Moves.RIGHT:
            pot = (row, col + 1)
        elif direction == Moves.UP:
            pot = (row - 1, col)
        elif direction == Moves.DOWN:
            pot = (row + 1, col)
        else:
            return None
        return pot

    def valid_pos(self, pos):
        """Ensures position isn't out of bounds.

        Args:
            pos (tuple): Position.

        Returns:
            bool
        """
        pot_row, pot_col = pos
        if pot_row < 0 or pot_row >= self.height:
            return False
        if pot_col < 0 or pot_col >= self.width:
            return False
        return True

    def can_remove(self, pos, wall):
        """Checks if a wall can be removed.

        Args:
            pos (tuple): Position.
            wall (int): Wall to be checked for removal.

        Returns:
            bool
        """
        pot = self.get_pos(pos, wall)  # potential position

        if not self.valid_pos(pot):
            return False
        return True

    def can_remove_and_unvis(self, pos, wall):
        """Checks if a wall can be removed and if its unvisited.

        Args:
            pos (tuple): Position.
            wall (int): Wall to be checked for removal.

        Returns:
            bool
        """
        pot = self.get_pos(pos, wall)  # potential position
        pot_row, pot_col = pot

        if not self.valid_pos(pot):
            return False
        if self.is_vis((pot_row, pot_col)):
            return False
        return True

    def remove_wall(self, pos, wall):
        """Removes bordering walls between two cells.

        Args:
            pos (tuple): Position.
            wall (int): Wall to be removed.

        Returns:
            tuple: Position of cell in the direction of removed wall.
        """
        row, col = pos
        if wall == Moves.LEFT:
            pot = (row, col - 1)
            pot_row, pot_col = pot
            self.get_cell((row, col)).left = False
            self.get_cell((pot_row, pot_col)).right = False
        if wall == Moves.RIGHT:
            pot = (row, col + 1)
            pot_row, pot_col = pot
            self.get_cell((row, col)).right = False
            self.get_cell((pot_row, pot_col)).left = False
        if wall == Moves.UP:
            pot = (row - 1, col)
            pot_row, pot_col = pot
            self.get_cell((row, col)).up = False
            self.get_cell((pot_row, pot_col)).down = False
        if wall == Moves.DOWN:
            pot = (row + 1, col)
            pot_row, pot_col = pot
            self.get_cell((row, col)).down = False
            self.get_cell((pot_row, pot_col)).up = False
        return pot

    def is_vis(self, pos):
        """Checks if a cell has been visited.

        Args:
            pos (tuple): Position of cell.

        Returns:
            bool
        """
        return self.get_cell(pos).vis

    def mark_vis(self, pos):
        """Marks a cell as visited.

        Args:
            pos (tuple): Position of cell.
        """
        self.get_cell(pos).vis = True
