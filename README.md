# Maze Creator and Solver
A python program that creates mazes using the hunt and kill algorithm, then solves them using bfs or dfs.
<div class="row">
    <div class="column">
        <img src="https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/main/examples/no_path_30.svg" alt="example">
    </div>
    <div class="column">
        <img src="https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/main/examples/bfs_30.svg" alt="example">
    </div>
</div>
## Pre-requisites
- [svgwrite](https://github.com/mozman/svgwrite) ```pip install svgwrite```
## How to
#### Change size of maze path
Change the value of ```OFFSET``` in [maze_drawer.py](https://github.com/cgr28/maze-creator-and-solver/blob/main/maze_drawer.py)
#### Change where position of where maze is drawn
Change the value of ```POS_X``` or ```POS_Y``` in [maze_drawer.py](https://github.com/cgr28/maze-creator-and-solver/blob/main/maze_drawer.py)
## Examples
Examples can be found in the [examples](https://github.com/cgr28/maze-creator-and-solver/examples) directory.

<style>
.row::after {
  content: "";
  clear: both;
  display: table;
}
.column {
  float: left;
  width: 40%;
  padding: 5px;
}
</style>