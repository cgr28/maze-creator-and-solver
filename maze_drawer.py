from grid import Grid
import svgwrite

OFFSET = 5  # determines how wide the path of the maze is
POS_X = 20  # offsets the maze from the right
POS_Y = 20  # offsets the maze from the top
OUTPUT_FILE = "maze.svg"  # the path of the output file


def draw_maze(maze, path=None, vis=None):
    canvas = svgwrite.Drawing(
        OUTPUT_FILE, size=("100%", "100%"), profile="full"
    )

    for i in range(maze.size):
        for j in range(maze.size):
            y = i * OFFSET + POS_Y
            x = j * OFFSET + POS_X
            if maze.get_cell((i, j)).right:
                canvas.add(
                    canvas.line(
                        (x + OFFSET, y),
                        (x + OFFSET, y + OFFSET),
                        stroke="black",
                    )
                )
            if maze.get_cell((i, j)).down:
                canvas.add(
                    canvas.line(
                        (x, y + OFFSET),
                        (x + OFFSET, y + OFFSET),
                        stroke="black",
                    )
                )

    if vis:
        for cell in vis:
            x, y = cell
            x = (x * OFFSET) + POS_X
            y = (y * OFFSET) + POS_Y
            canvas.add(
                canvas.rect(
                    (y, x),
                    (OFFSET, OFFSET),
                    stroke="yellow",
                    fill="orange",
                    opacity=0.2,
                )
            )

    if path:
        for cell in path:
            x, y = cell
            x = (x * OFFSET) + POS_X
            y = (y * OFFSET) + POS_Y
            canvas.add(
                canvas.rect(
                    (y, x),
                    (OFFSET, OFFSET),
                    stroke="lightgreen",
                    fill="green",
                    opacity=0.3,
                )
            )

    canvas.add(
        canvas.line(
            (POS_X, POS_Y),
            (POS_X + (OFFSET * maze.size), POS_Y),
            stroke="black",
        )
    )
    canvas.add(
        canvas.line(
            (POS_X, POS_Y),
            (POS_X, POS_Y + (OFFSET * maze.size)),
            stroke="black",
        )
    )

    canvas.save()
