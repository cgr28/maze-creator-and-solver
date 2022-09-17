from enums import Moves, Walls, Solver
from grid import Grid

class Helpers:
    
    @staticmethod
    def maze_to_enums(maze: Grid):
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
        solution_enums = [[0 for i in range(maze.width)] for j in range(maze.height)]
        for row, col in vis:
            solution_enums[row][col] = Solver.VIS
        for row, col in sol:
            solution_enums[row][col] = Solver.SOL
        return solution_enums