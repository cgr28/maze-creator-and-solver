import sys
sys.path.append(".")
from flask import Flask
from flask_restful import Resource, Api
from maze_drawer import draw_maze
from maze_creator.maze_creators import MazeCreators
from maze_solver.maze_solvers import MazeSolvers
from grid import Grid

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):

    def get(self):
        SIZE = 100
        START = (0, 0)  # default: solver starts at the top left of the maze
        END = (SIZE - 1, SIZE - 1)  # default: solver ends at bottom right of maze

        grid = Grid(SIZE)
        maze = MazeCreators.hunt_and_kill(grid)
        solution_path, vis_cells = MazeSolvers.dfs(maze, START, END)
        # solution_path = MazeSolvers.a_star(maze, START, END)
        # remove vis_cells to hide visited cells e.g. draw_maze(maze, solution_path)
        # remove solution_path to hide the solutoin e.g. draw_maze(maze)
        draw_maze(maze, solution_path, vis_cells)
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)