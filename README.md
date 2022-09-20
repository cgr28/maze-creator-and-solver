# Maze Creator And Solver ![Icon](https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/main/frontend/public/icon.png)
A Python Flask and React web app that allows you to create and download mazes with solutions.
![Walk-through](https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/main/imgs/walkthrough.gif)
<br />
<a href="https://maze-creator-and-solver.herokuapp.com/" target="_blank" rel="noreferrer"><img src="https://img.shields.io/badge/website-maze--creator--and--solver.herokuapp.com-green?style=for-the-badge" /></a>

## Install and Run App
### Docker
```bash
docker compose up
```
***View at any of the following http://localhost:8080 | http://0.0.0.0:8080/ | http://127.0.0.1:8080/***
### Manual
#### Frontend
```bash
cd frontend
npm install
npm start
```
#### Backend
##### Option 1 - app.py
```bash
cd backend
pip install -r requirements.txt
python3 app.py
```
or
##### Option 2 - gunicorn
```bash
cd backend
pip install -r requirements.txt
gunicorn -b :8080 app:app
```

***View at http://localhost:3000***

## Usage
1. Select the algorithm that will be used to create the maze.
2. Select one or more algorithms that will be used to generate solutions. To generate a maze with no solutions select "None".
3. Select the height and width of the maze.  Choose if generated mazes will display the cells that were visited by the solver when finding the solution.
4. Click the "Create Maze(s)" button to have your maze(s) created.
5. To download png of a maze click the "Download" button beneath the maze.

## Maze Creator Algorithms
### [Growing Tree](https://github.com/cgr28/maze-creator-and-solver/blob/main/backend/creator/maze_creators.py#L45) <br /> ![Growing Tree](https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/main/imgs/growing-tree.png)
*Creates a perfect maze (only one solution).*
### [Hunt And Kill](https://github.com/cgr28/maze-creator-and-solver/blob/main/backend/creator/maze_creators.py#L9) <br /> ![Hunt and Kill](https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/main/imgs/hunt-and-kill.png)
*Creates mazes that may have more than one solution. Takes the longest to generate mazes.*
### [Prims](https://github.com/cgr28/maze-creator-and-solver/blob/main/backend/creator/maze_creators.py#L76) <br /> ![Prims](https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/main/imgs/prims.png)
*Creates a perfect maze (only one solution).*

## Maze Solver Algorithms
### [A*](https://github.com/cgr28/maze-creator-and-solver/blob/main/backend/solver/maze_solvers.py#L121) <br /> ![A*](https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/main/imgs/a-star.png)
*Finds the solution that has the shortest possible path. Uses Manhattan distance as heuristic.*
### [Best First Search](https://github.com/cgr28/maze-creator-and-solver/blob/main/backend/solver/maze_solvers.py#L77) <br /> ![Best First Search](https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/main/imgs/best-first-search.png)
*Solution path may not be the shortest one possible. Uses Manhattan distance as heuristic.*
### [Breadth First Search](https://github.com/cgr28/maze-creator-and-solver/blob/main/backend/solver/maze_solvers.py#L44) <br /> ![Breadth First Search](https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/main/imgs/breadth-first-search.png)
*Finds the solution that has the shortest possible path.*
### [Depth First Search](https://github.com/cgr28/maze-creator-and-solver/blob/main/backend/solver/maze_solvers.py#L10) <br /> ![Depth First Search](https://raw.githubusercontent.com/cgr28/maze-creator-and-solver/main/imgs/depth-first-search.png)
*Solution path may not be the shortest one possible.*

## Liscense
[MIT](https://github.com/cgr28/maze-creator-and-solver/blob/main/LICENSE)