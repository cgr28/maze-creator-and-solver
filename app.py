#TODO fix COORS

import sys
sys.path.append(".")
from flask import Flask, send_from_directory
from flask_cors import CORS
from maze_drawer import draw_maze
from maze_creator.maze_creators import MazeCreators
from maze_solver.maze_solvers import MazeSolvers

app = Flask(__name__, static_folder="./client", static_url_path="")
CORS(app)

@app.route('/api/<string:maze_type>/<int:size>/<string:search_type>')
def Maze(maze_type, size=20, search_type="dfs"):
    print(app.static_folder)
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

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=False)