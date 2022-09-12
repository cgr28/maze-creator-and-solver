from enum import Enum


class Moves(Enum):
    """All moves that can be made in maze."""

    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Walls:
    """Wall directions in maze for maze generation."""

    DOWN = 1
    RIGHT = 2
    BOTH = 3
    NONE = 4

class Solver:
    """Solution and visited for solution generation."""

    SOL = 1
    VIS = 2