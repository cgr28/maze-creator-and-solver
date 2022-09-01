<h1 align="center">Maze Creator and Solver</h1>
Creates mazes with solutions using various algorithms and Python.<br/>
View at https://maze-creator-and-solver.herokuapp.com/<br/>

## Pre-requisites
All packages in [requirements.txt](https://github.com/cgr28/maze-creator-and-solver/blob/main/requirements.txt) installed ```pip install -r requirements.txt```

## How to
### Change size of maze path
Change the value of ```OFFSET``` in [drawer/maze_drawer.py](https://github.com/cgr28/maze-creator-and-solver/blob/main/drawer/maze_drawers.py#L4)
### Change position of where maze is drawn
Change the value of ```POS_X``` or ```POS_Y``` in [drawer/maze_drawer.py](https://github.com/cgr28/maze-creator-and-solver/blob/main/drawer/maze_drawers.py#L5)

### Run App
1. Complete pre-requisites
2. Run the api ```python3 api/app.py```
3. Navigate to http://localhost:8080/

## Maze Creators
### [Growing Tree](https://github.com/cgr28/maze-creator-and-solver/blob/main/creator/maze_creators.py#L45) <br /> ![Growing Tree](https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/5ad1c3cf11fb508d4a9a547a4ecbcd8cdf6cb7ce/examples/imgs/growing-tree.svg)
### [Hunt And Kill](https://github.com/cgr28/maze-creator-and-solver/blob/main/creator/maze_creators.py#L9) <br /> ![Hunt and Kill](https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/5ad1c3cf11fb508d4a9a547a4ecbcd8cdf6cb7ce/examples/imgs/hunt-and-kill.svg)
### [Prims](https://github.com/cgr28/maze-creator-and-solver/blob/main/creator/maze_creators.py#L76) <br /> ![Prims](https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/5ad1c3cf11fb508d4a9a547a4ecbcd8cdf6cb7ce/examples/imgs/prims.svg)

## Maze Solvers
### [A Star](https://github.com/cgr28/maze-creator-and-solver/blob/main/solver/maze_solvers.py#L121) <br /> ![A Star](https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/5ad1c3cf11fb508d4a9a547a4ecbcd8cdf6cb7ce/examples/imgs/a-star.svg)
### [Best First Search](https://github.com/cgr28/maze-creator-and-solver/blob/main/solver/maze_solvers.py#L77) <br /> ![Best First Search](https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/5ad1c3cf11fb508d4a9a547a4ecbcd8cdf6cb7ce/examples/imgs/best.svg)
### [Breadth First Search](https://github.com/cgr28/maze-creator-and-solver/blob/main/solver/maze_solvers.py#L44) <br /> ![Breadth First Search](https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/5ad1c3cf11fb508d4a9a547a4ecbcd8cdf6cb7ce/examples/imgs/breadth.svg)
### [Depth First Search](https://github.com/cgr28/maze-creator-and-solver/blob/main/solver/maze_solvers.py#L10) <br /> ![Depth First Search](https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/5ad1c3cf11fb508d4a9a547a4ecbcd8cdf6cb7ce/examples/imgs/depth.svg)
## Examples
### Maze Creation and Solving
Examples for creating mazes can be found in the [examples/examples.py](https://github.com/cgr28/maze-creator-and-solver/blob/main/examples/examples.py) file.
### Mazes
Example maze images can be found in the [examples/imgs](https://github.com/cgr28/maze-creator-and-solver/tree/main/examples/imgs) directory

