from flask import Flask, send_from_directory, request
from flask_cors import CORS
from creator.maze_creators import MazeCreators
from solver.maze_solvers import MazeSolvers
from helpers import *

app = Flask(__name__, static_folder="../build", static_url_path="/")
CORS(
    app,
    origin=[
        "http://localhost:8080/",
        "https://maze-creator-and-solver.herokuapp.com/",
        "http://maze-creator-and-solver.herokuapp.com/",
        "http://localhost:3000/",
    ],
)


@app.route(
    "/api/<string:creator>/<int:height>/<int:width>/<int:vis>", methods=["GET"]
)
def Maze(creator, height=20, width=20, vis=0):
    """Generates a maze and solutions using given parameters.

    Args:
        creator (str): The type of maze creator that will be used.
        height (int, optional): The height of the maze. Defaults to 20.
        width (int, optional): The width of the maze. Defaults to 20.
        vis (int, optional): If 0 visited cells will be excluded. If 1 visited cells will be included. Defaults to 0.

    Returns:
        dict: API response.
    """
    args = request.args
    try:
        solvers = args.getlist("solver")
        if not solvers:
            solvers = ["none"]
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

    if creator == "hunt-and-kill":
        maze = MazeCreators.hunt_and_kill(HEIGHT, WIDTH)
    elif creator == "growing-tree":
        maze = MazeCreators.growing_tree(HEIGHT, WIDTH)
    elif creator == "prims":
        maze = MazeCreators.prims(HEIGHT, WIDTH)
    else:
        maze = MazeCreators.hunt_and_kill(HEIGHT, WIDTH)

    maze_enums = Helpers.maze_to_enums(maze)
    solutions = []

    for solver in solvers:
        if solver == "depth-first-search":
            solution_path, vis_cells = MazeSolvers.depth_first_search(maze, START, END)
        elif solver == "breadth-first-search":
            solution_path, vis_cells = MazeSolvers.breadth_first_search(
                maze, START, END
            )
        elif solver == "best-first-search":
            solution_path, vis_cells = MazeSolvers.best_first_search(maze, START, END)
        elif solver == "a-star":
            solution_path, vis_cells = MazeSolvers.a_star(maze, START, END)
        else:
            solution_path, vis_cells = ([], [])

        num_visited_cells = len(vis_cells)
        solution_length = len(solution_path)

        if not vis:
            vis_cells = []

        solution_enums = Helpers.solution_to_enums(vis_cells, solution_path, maze)
        solutions.append(
            {
                "search_type": solver,
                "visited_cells": num_visited_cells,
                "solution_length": solution_length,
                "solution": solution_enums,
            }
        )

    response = {
        "maze": maze_enums,
        "height": (HEIGHT),
        "width": (WIDTH),
        "solutions": solutions,
    }

    return response


@app.route("/")
def serve():
    return send_from_directory(app.static_folder, "index.html")


@app.errorhandler(404)
def page_not_found(e):
    """When there's a 404 error, return to the main page."""
    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=False)
