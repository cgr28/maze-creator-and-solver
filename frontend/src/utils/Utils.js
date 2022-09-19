// returns the maze solvers query for the api call
// @param checked: array of bools, that represent whether a maze solver checkbox was checked
// @param solverTypes: an array containing objects, that have the name and value for each algorithm
export const getSolversQuery = (checked, solverTypes) => {
    let solvers = [];
    for (let i = 0; i < checked.length; i++) {
        if (checked[i]) {
            solvers.push(solverTypes[i].value);
        }
    }
    if (solvers.length === 0) {
        return "";
    } else if (solvers.length === 1) {
        return `?solver=${solvers[0]}`;
    } else {
        let query = `?solver=${solvers[0]}`;
        for (let i = 1; i < solvers.length; i++) {
            query += `&solver=${solvers[i]}`;
        }
        return query;
    }
};

// draws the maze to an html canvas element
// @param maze: a 2d array representing the maze to be drawn
// @param width: the width of the maze
// @param height: the height of the maze
// @param solution: the a 2d array reperesenting the mazes solution
// @param canvasId: the id of the canvas element where the maze will be drawn
export const drawMaze = (maze, width, height, solution, canvasId) => {
    const OFFSET = 5;
    var canvas = document.getElementById(canvasId);
    canvas.setAttribute("width", width * OFFSET + 1);
    canvas.setAttribute("height", height * OFFSET + 1);
    var context = canvas.getContext("2d");
    context.translate(0.5, 0.5);

    context.fillStyle = "white";
    context.fillRect(0, 0, width * OFFSET + 1, height * OFFSET + 1);
    context.stroke();

    for (let i = 0; i < maze.length; i++) {
        for (let j = 0; j < maze[i].length; j++) {
            let x = j * OFFSET;
            let y = i * OFFSET;
            let cell = maze[i][j];
            if (cell === 1 || cell === 3) {
                context.moveTo(x, y + OFFSET);
                context.lineTo(x + OFFSET, y + OFFSET);
            }
            if (cell === 2 || cell === 3) {
                context.moveTo(x + OFFSET, y);
                context.lineTo(x + OFFSET, y + OFFSET);
            }
        }
    }
    context.moveTo(0, 0);
    context.lineTo(OFFSET * width, 0);

    context.moveTo(0, 0);
    context.lineTo(0, OFFSET * height);

    context.moveTo(OFFSET * width, 0);
    context.lineTo(OFFSET * width, OFFSET * height);

    context.moveTo(0, OFFSET * height);
    context.lineTo(OFFSET * width, OFFSET * height);

    context.strokeStyle = "black";
    context.lineWidth = 0.5;
    context.stroke();

    context.lineWidth = 0;
    context.fillStyle = "rgb(0,128,0, 0.5)";

    for (let i = 0; i < maze.length; i++) {
        for (let j = 0; j < maze[i].length; j++) {
            let x = j * OFFSET;
            let y = i * OFFSET;
            let sol = solution[i][j];
            if (sol === 1) {
                context.fillStyle = "rgb(0,128,0, 0.3)";
                context.fillRect(x, y, OFFSET, OFFSET);
                context.stroke();
            }
            if (sol === 2) {
                context.fillStyle = "rgb(255,165,0, 0.2)";
                context.fillRect(x, y, OFFSET, OFFSET);
                context.stroke();
            }
        }
    }
    context.stroke();
    return canvas;
};

// key: maze solver value
// value: maze solver name
export const solverMap = {
    "best-first-search": "Best First Search",
    "breadth-first-search": "Breadth First Search",
    "depth-first-search": "Depth First Search",
    "a-star": "A-Star",
    "none": "None",
};

// an array contaning the name and values of every solver type
export const solverTypes = [
    { name: "Breadth First Search", value: "breadth-first-search" },
    { name: "Depth First Search", value: "depth-first-search" },
    { name: "Best First Search", value: "best-first-search" },
    { name: "A-Star", value: "a-star" },
    { name: "None", value: "none" },
];
