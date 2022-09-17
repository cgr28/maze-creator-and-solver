from flask import Flask, send_from_directory, request
from flask_cors import CORS
from drawer.maze_drawers import Drawer
from creator.maze_creators import MazeCreators
from solver.maze_solvers import MazeSolvers
from helpers import *

app = Flask(__name__, static_folder="./../frontend/build", static_url_path="")
CORS(
    app,
    origin=[
        "http://localhost:8080/",
        "https://maze-creator-and-solver.herokuapp.com/",
        "http://maze-creator-and-solver.herokuapp.com/",
        "http://localhost:3000/"
    ],
)


@app.route(
    "/api/<string:maze_type>/<int:height>/<int:width>/<int:vis>",
    methods=['GET']
)
def Maze(maze_type, height=20, width=20, vis=0):
    args = request.args
    try:
        solvers = args.getlist("solver")
    except:
        solvers = ["none"]
        
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

    maze_enums = Helpers.maze_to_enums(maze)
    solutions = []

    for search_type in solvers:
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
            solution_path, vis_cells = ([], [])
            visited_cells = 0
            solution_length = 0
        if not vis:
            vis_cells = []
        solution_enums = Helpers.solution_to_enums(vis_cells, solution_path, maze)
        solutions.append({"search_type": search_type, "visited_cells": visited_cells, "solution_length": solution_length, "solution": solution_enums})
        

    response = {
        "maze": maze_enums,
        "height": (HEIGHT),
        "width": (WIDTH),
        "solutions": solutions
    }

    return response


@app.route("/")
def serve():
    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
