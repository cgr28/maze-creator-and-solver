export const arrToMaze = (arr, width, height, solution, id) => {
    const OFFSET = 5
    var canvas = document.getElementById(id);
    canvas.setAttribute("width", width * OFFSET + 1);
    canvas.setAttribute("height", height * OFFSET + 1);
    var context = canvas.getContext('2d');
    context.translate(0.5, 0.5);

    context.fillStyle = "white";
    context.fillRect(0, 0, width * OFFSET + 1, height * OFFSET + 1)
    context.stroke();
    
    for (let i = 0; i < arr.length; i++) {
      for (let j = 0; j < arr[i].length; j++) {
        let x = j * OFFSET;
        let y = i * OFFSET;
        let cell = arr[i][j]
        if (cell === 1 || cell === 3) {
          context.moveTo(x, y + OFFSET);
          context.lineTo(x + OFFSET, y + OFFSET)
        }
        if (cell === 2 || cell === 3) {
          context.moveTo(x + OFFSET, y);
          context.lineTo(x + OFFSET, y + OFFSET)
        }
      }
    }
    context.moveTo(0, 0)
    context.lineTo(OFFSET * width, 0)

    context.moveTo(0, 0)
    context.lineTo(0, OFFSET * height)

    context.moveTo(OFFSET * width, 0)
    context.lineTo(OFFSET * width, OFFSET * height)

    context.moveTo(0, OFFSET * height)
    context.lineTo(OFFSET * width, OFFSET * height)

    context.strokeStyle = "black";
    context.lineWidth = 0.5;
    context.stroke();

    context.lineWidth = 0
    context.fillStyle = "rgb(0,128,0, 0.5)";

    for (let i = 0; i < arr.length; i++) {
      for (let j = 0; j < arr[i].length; j++) {
        let x = j * OFFSET;
        let y = i * OFFSET;
        let sol = solution[i][j]
        if (sol === 1) {
          context.fillStyle = "rgb(0,128,0, 0.3)";
          context.fillRect(x, y, OFFSET, OFFSET)
          context.stroke();
        }
        if (sol === 2) {
          context.fillStyle = "rgb(255,165,0, 0.2)";
          context.fillRect(x, y, OFFSET, OFFSET)
          context.stroke();
        }
      }
    }
    context.stroke();
    return canvas
  }

export const mazeKey = {"best-first-search": "Best First Search", "breadth-first-search": "Breadth First Search", "depth-first-search": "Depth First Search", "a-star": "A-Star", "none": "None"}