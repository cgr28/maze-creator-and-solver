from enums import Moves, Walls, Solver
from grid import Grid


class Helpers:
    @staticmethod
    def maze_to_enums(maze: Grid):
        """Generates a list of Walls enums that represents a given maze. This is then used to draw the maze.

        Args:
            maze (Grid): The maze that will converted to an list of Walls enums.

        Returns:
            list: List of Walls enums.
        """
        maze_enums = []
        for i in range(maze.height):
            temp = []
            for j in range(maze.width):
                cell = maze.get_cell((i, j))
                if cell.down and cell.right:
                    temp.append(Walls.BOTH)
                elif cell.down:
                    temp.append(Walls.DOWN)
                elif cell.right:
                    temp.append(Walls.RIGHT)
                else:
                    temp.append(Walls.NONE)
            maze_enums.append(temp)
        return maze_enums

    @staticmethod
    def solution_to_enums(vis, sol, maze):
        """Generates a list of Solver enums that represents a given solution. This is then used to draw the maze solution.

        Args:
            vis (list): The cells visited when finding the solution.
            sol (list): The path to the solution.
            maze (Grid): The maze that was solved.

        Returns:
            list: List of Solver enums.
        """
        solution_enums = [[0 for i in range(maze.width)] for j in range(maze.height)]
        for row, col in vis:
            solution_enums[row][col] = Solver.VIS
        for row, col in sol:
            solution_enums[row][col] = Solver.SOL
        return solution_enums
