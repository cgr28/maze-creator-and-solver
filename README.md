# Maze Creator and Solver
##### Creates mazes with solutions using various algorithms and Python.
##### View at https://maze-creator-and-solver.herokuapp.com/
##### The website is hosted from the [prod](https://github.com/cgr28/maze-creator-and-solver/tree/prod/) branch
####
## Pre-requisites
- [svgwrite](https://github.com/mozman/svgwrite) ```pip install svgwrite```
## How to
#### Change size of maze path
Change the value of ```OFFSET``` in [drawer/maze_drawer.py](https://github.com/cgr28/maze-creator-and-solver/blob/main/drawer/maze_drawers.py#L4)
#### Change position of where maze is drawn
Change the value of ```POS_X``` or ```POS_Y``` in [drawer/maze_drawer.py](https://github.com/cgr28/maze-creator-and-solver/blob/main/drawer/maze_drawers.py#L5)
## Maze Creators
- #### [Growing Tree](https://github.com/cgr28/maze-creator-and-solver/blob/main/creator/maze_creators.py#L45) ![Growing Tree](https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/5ad1c3cf11fb508d4a9a547a4ecbcd8cdf6cb7ce/examples/imgs/growing-tree.svg)
- #### [Hunt And Kill](https://github.com/cgr28/maze-creator-and-solver/blob/main/creator/maze_creators.py#L9) ![Hunt and Kill](https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/5ad1c3cf11fb508d4a9a547a4ecbcd8cdf6cb7ce/examples/imgs/hunt-and-kill.svg)
- #### [Prims](https://github.com/cgr28/maze-creator-and-solver/blob/main/creator/maze_creators.py#L76) ![Prims](https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/5ad1c3cf11fb508d4a9a547a4ecbcd8cdf6cb7ce/examples/imgs/prims.svg)

## Maze Solvers
- #### [A Star](https://github.com/cgr28/maze-creator-and-solver/blob/main/solver/maze_solvers.py#L121) ![A Star](https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/5ad1c3cf11fb508d4a9a547a4ecbcd8cdf6cb7ce/examples/imgs/a-star.svg)
- #### [Best First Search](https://github.com/cgr28/maze-creator-and-solver/blob/main/solver/maze_solvers.py#L77) ![Best First Search](https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/5ad1c3cf11fb508d4a9a547a4ecbcd8cdf6cb7ce/examples/imgs/best.svg)
- #### [Breadth First Search](https://github.com/cgr28/maze-creator-and-solver/blob/main/solver/maze_solvers.py#L44) ![Breadth First Search](https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/5ad1c3cf11fb508d4a9a547a4ecbcd8cdf6cb7ce/examples/imgs/breadth.svg)
- #### [Depth First Search](https://github.com/cgr28/maze-creator-and-solver/blob/main/solver/maze_solvers.py#L10) ![Depth First Search](https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/5ad1c3cf11fb508d4a9a547a4ecbcd8cdf6cb7ce/examples/imgs/depth.svg)
## Examples
Examples for creating mazes can be found in the [examples/examples.py](https://github.com/cgr28/maze-creator-and-solver/blob/main/examples/examples.py) file.
Example images can be found in the [examples/imgs](https://github.com/cgr28/maze-creator-and-solver/tree/main/examples/imgs) directory