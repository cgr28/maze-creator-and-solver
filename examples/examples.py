import sys

sys.path.append(".")
from backend.drawer.maze_drawers import Drawer
from backend.creator.maze_creators import MazeCreators
from backend.solver.maze_solvers import MazeSolvers

# CONSTANTS
HEIGHT = 30  # height of maze
WIDTH = 30  # width of maze
START = (0, 0)  # solution starting cell
END = (HEIGHT - 1, WIDTH - 1)  # solution ending cell

# HOW TO CREATE MAZE
hunt_and_kill = MazeCreators.hunt_and_kill(
    HEIGHT, WIDTH
)  # creates a maze using Hunt and Kill algorithm
growing_tree = MazeCreators.growing_tree(
    HEIGHT, WIDTH
)  # creates a maze using Growing Tree algorithm
prims = MazeCreators.prims(HEIGHT, WIDTH)  # creates a maze using Prims algorithm

# HOW TO SOLVE MAZE
breadth_solution, breadth_visited = MazeSolvers.breadth_first_search(
    hunt_and_kill, START, END
)  # solves maze using breadth first search
depth_solution, depth_visited = MazeSolvers.depth_first_search(
    hunt_and_kill, START, END
)  # solves maze depth first search
best_solution, best_visited = MazeSolvers.best_first_search(
    hunt_and_kill, START, END
)  # solves maze using best first search
a_star_solution, a_star_visited = MazeSolvers.a_star(
    hunt_and_kill, START, END
)  # solves maze A-Star

# HOW TO DRAW MAZE WITH SOLUTION AND VISITED CELLS
Drawer.draw(
    hunt_and_kill,
    breadth_solution,
    breadth_visited,
    output_file="./examples/imgs/breadth.svg",
)
Drawer.draw(
    hunt_and_kill,
    depth_solution,
    depth_visited,
    output_file="./examples/imgs/depth.svg",
)
Drawer.draw(
    hunt_and_kill, best_solution, best_visited, output_file="./examples/imgs/best.svg"
)
Drawer.draw(
    hunt_and_kill,
    a_star_solution,
    a_star_visited,
    output_file="./examples/imgs/a-star.svg",
)

# HOW TO DRAW MAZE WITH SOLUTION AND NO VISITED CELLS
Drawer.draw(
    hunt_and_kill, breadth_solution, output_file="./examples/imgs/breadth-no-vis.svg"
)
Drawer.draw(
    hunt_and_kill, depth_solution, output_file="./examples/imgs/depth-no-vis.svg"
)
Drawer.draw(hunt_and_kill, best_solution, output_file="./examples/imgs/best-no-vis.svg")
Drawer.draw(
    hunt_and_kill, a_star_solution, output_file="./examples/imgs/a-star-no-vis.svg"
)

# HOW TO DRAW MAZE WITH NO SOLUTION
Drawer.draw(hunt_and_kill, output_file="./examples/imgs/hunt-and-kill.svg")
Drawer.draw(growing_tree, output_file="./examples/imgs/growing-tree.svg")
Drawer.draw(prims, output_file="./examples/imgs/prims.svg")
