import sys
sys.path.append(".")
from flask import Flask, send_from_directory
from flask_cors import CORS
from drawer.maze_drawers import Drawer
from creator.maze_creators import MazeCreators
from solver.maze_solvers import MazeSolvers

app = Flask(__name__, static_folder="./../client", static_url_path="")
CORS(app, origin=["http://localhost:8080/", "https://maze-creator-and-solver.herokuapp.com/", "http://maze-creator-and-solver.herokuapp.com/"])

@app.route('/api/<string:maze_type>/<int:height>/<int:width>/<string:search_type>/<int:vis>')
def Maze(maze_type, height=20, width=20, search_type="dfs", vis=0):
    if height > 100:
        HEIGHT = 100
    elif height < 5:
        HEIGHT = 5
    else:
        HEIGHT = height
    
    if width > 100:
        WIDTH = 100
    elif width < 5:
        WIDTH = 5
    else:
        WIDTH = width
        
    START = (0, 0)
    END = (HEIGHT - 1, WIDTH - 1)

    if maze_type == "hunt-and-kill":
        maze = MazeCreators.hunt_and_kill(HEIGHT, WIDTH)
    elif maze_type == "growing-tree":
        maze = MazeCreators.growing_tree(HEIGHT, WIDTH)
    elif maze_type == "prims":
        maze = MazeCreators.prims(HEIGHT, WIDTH)
    else:
        maze = MazeCreators.hunt_and_kill(HEIGHT, WIDTH)

    if search_type == "depth-first-search":
        solution_path, vis_cells = MazeSolvers.depth_first_search(maze, START, END)
        visited_cells = len(vis_cells)
        solution_length = len(solution_path)
    elif search_type == "breadth-first-search":
        solution_path, vis_cells = MazeSolvers.breadth_first_search(maze, START, END)
        visited_cells = len(vis_cells)
        solution_length = len(solution_path)
    elif search_type == "best-first-search":
        solution_path, vis_cells = MazeSolvers.best_first_search(maze, START, END)
        visited_cells = len(vis_cells)
        solution_length = len(solution_path)
    elif search_type == "a-star":
        solution_path, vis_cells = MazeSolvers.a_star(maze, START, END)
        visited_cells = len(vis_cells)
        solution_length = len(solution_path)
    else:
        solution_path, vis_cells = (None, None)
        visited_cells = 0
        solution_length = 0
    if not vis:
        vis_cells = []

    canvas = Drawer.draw(maze, solution_path, vis_cells)
    return {
            'maze': canvas.tostring(),
            'height': (HEIGHT),
            "width": (WIDTH),
            'visited_cells': visited_cells,
            'solution_length': solution_length
            }

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=False)