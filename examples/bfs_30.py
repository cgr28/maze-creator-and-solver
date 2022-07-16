#!/usr/bin/env python3
# creates a maze of size 30 with a bfs solution

import sys
sys.path.append(".")
from maze_solver.maze_solvers import MazeSolvers
from maze_creator.maze_creators import MazeCreators
from maze_drawer import draw_maze



SIZE = 30 # the width and height of the maze in cells
START = (0, 0) # where the solution will start  min=(0, 0), max=(SIZE-1, SIZE-1)
END = (SIZE - 1, SIZE - 1) # where the solution will end  min=(0, 0), max=(SIZE-1, SIZE-1)

maze = MazeCreators.hunt_and_kill(SIZE) # creates a SIZExSIZE maze using the hunt and kill algorithm
solution_path, vis_cells = MazeSolvers.bfs(maze, START, END) # returns list of cells in the bfs solution and a list of cells visited by the bfs solution

draw_maze(maze, solution_path, vis_cells, "./examples/bfs_30.svg") # draws a maze with a solution and visited cells
