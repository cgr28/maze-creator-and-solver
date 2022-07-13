#!/usr/bin/env python3
# creates a size 30 maze with no soluiton or visited cells

import sys
sys.path.append(".")
from maze_creator.maze_creators import MazeCreators
from maze_drawer import draw_maze


SIZE = 30 # the width and height of the maze in cells

maze = MazeCreators.hunt_and_kill(SIZE) # creates a SIZExSIZE maze using the hunt and kill algorithm

draw_maze(maze, output_file="./examples/no_path_30.svg") # draws a maze with no solution or visited cells
