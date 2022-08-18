from grid import Grid
import svgwrite

OFFSET = 5  # determines how wide the path of the maze is
POS_X = 0  # offsets the maze from the right
POS_Y = 0  # offsets the maze from the top


class Drawer:
    @staticmethod
    def draw(maze, path=None, vis=None, output_file=None):
        if output_file:
            OUTPUT_FILE = output_file  # the path of the output file
        else:
            OUTPUT_FILE = "maze.svg"

        canvas = svgwrite.Drawing(OUTPUT_FILE, size=("100%", "100%"), profile="tiny")

        canvas.add(
            canvas.rect(
                (POS_X, POS_Y),
                (POS_X + (OFFSET * maze.width), POS_Y + (OFFSET * maze.height)),
                fill="white",
                stroke_width=0,
            )
        )

        for i in range(maze.height):
            for j in range(maze.width):
                y = i * OFFSET + POS_Y
                x = j * OFFSET + POS_X
                if maze.get_cell((i, j)).right:
                    canvas.add(
                        canvas.line(
                            (x + OFFSET, y),
                            (x + OFFSET, y + OFFSET),
                            stroke="black",
                            stroke_width=0.5,
                        )
                    )
                if maze.get_cell((i, j)).down:
                    canvas.add(
                        canvas.line(
                            (x, y + OFFSET),
                            (x + OFFSET, y + OFFSET),
                            stroke="black",
                            stroke_width=0.5,
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
                        fill="orange",
                        opacity=0.2,
                        stroke_width=0,
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
                        fill="green",
                        opacity=0.3,
                        stroke_width=0,
                    )
                )

        canvas.add(
            canvas.line(
                (POS_X, POS_Y),
                (POS_X + (OFFSET * maze.width), POS_Y),
                stroke="black",
                stroke_width=2,
            )
        )
        canvas.add(
            canvas.line(
                (POS_X, POS_Y),
                (POS_X, POS_Y + (OFFSET * maze.height)),
                stroke="black",
                stroke_width=2,
            )
        )
        canvas.add(
            canvas.line(
                (POS_X, POS_Y + (OFFSET * maze.height)),
                (POS_X + (OFFSET * maze.width), POS_Y + (OFFSET * maze.height)),
                stroke="black",
                stroke_width=2,
            )
        )
        canvas.add(
            canvas.line(
                (POS_X + (OFFSET * maze.width), POS_Y),
                (POS_X + (OFFSET * maze.width), POS_Y + (OFFSET * maze.height)),
                stroke="black",
                stroke_width=2,
            )
        )

        if output_file:
            canvas.save()
        return canvas
