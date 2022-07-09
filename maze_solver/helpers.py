from helpers import *


def move(pos, direction):
    row, col = pos
    if direction == RIGHT:
        ret = (row, col + 1)
    elif direction == LEFT:
        ret = (row, col - 1)
    elif direction == UP:
        ret = (row - 1, col)
    else:  # direction == DOWN
        ret = (row + 1, col)

    return ret


# ensures that the potential move doesn't have walls, or isn't OOB
def can_move(maze, pos, direction):
    row, col = pos
    cell = maze.get_cell(pos)

    if direction == RIGHT:
        if cell.right:
            return False
    elif direction == LEFT:
        if cell.left:
            return False
    elif direction == UP:
        if cell.up:
            return False
    else:  # direction == DOWN
        if cell.down:
            return False

    pot_row, pot_col = move(pos, direction)
    if pot_col < 0 or pot_col >= maze.size:
        return False

    if pot_row < 0 or pot_row >= maze.size:
        return False

    return True
