#TODO fix COORS

import sys
sys.path.append(".")
from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api
from maze_drawer import draw_maze
from maze_creator.maze_creators import MazeCreators
from maze_solver.maze_solvers import MazeSolvers

app = Flask(__name__)
CORS(app)
api = Api(app)

class MazeApi(Resource):

    def get(self, maze_type, size=20, search_type="dfs"):
        if size > 100:
            SIZE = 100
        elif size < 5:
            SIZE = 5
        else:
            SIZE = size
            
        START = (0, 0)
        END = (SIZE - 1, SIZE - 1)

        if maze_type == "hunt-and-kill":
            maze = MazeCreators.hunt_and_kill(SIZE)
        else:
            maze = MazeCreators.hunt_and_kill(SIZE)
        if search_type == "dfs":
            solution_path, vis_cells = MazeSolvers.dfs(maze, START, END)
            visited_cells = len(vis_cells)
            solution_length = len(solution_path)
        elif search_type == "bfs":
            solution_path, vis_cells = MazeSolvers.bfs(maze, START, END)
            visited_cells = len(vis_cells)
            solution_length = len(solution_path)
        else:
            solution_path, vis_cells = (None, None)
            visited_cells = 0
            solution_length = 0

        canvas = draw_maze(maze, solution_path, vis_cells, "./src/maze.svg")
        return {
                'maze': canvas.tostring(),
                'num_of_cells': (SIZE ** 2),
                'visited_cells': visited_cells,
                'solution_length': solution_length
                }

api.add_resource(MazeApi, '/api/<string:maze_type>/<int:size>/<string:search_type>')

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=False)