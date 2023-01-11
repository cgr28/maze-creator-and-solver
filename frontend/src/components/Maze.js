import React, { useEffect, useState } from "react";
import { drawMaze, solverMap } from "../utils/Utils";
import { ReImg } from "reimg";
import "./Maze.scss";

export default function Maze({ maze, solInfo, height, width, id }) {
    const [canvas, setCanvas] = useState(0);
    useEffect(() => {
        setCanvas(drawMaze(maze, width, height, solInfo.solution, id));
    }, [maze]);
    return (
        <div className="maze mt-3">
            <div>Solver: {solverMap[solInfo.search_type]}</div>
            <div>Cells Visited: {solInfo.visited_cells}</div>
            <div>Solution Length: {solInfo.solution_length}</div>
            <canvas id={id} className={"maze-output"}></canvas>
            {canvas ? (
                <div className="mt-2">
                    <button
                        onClick={() => {
                            ReImg.fromCanvas(canvas).downloadPng();
                        }}
                    >
                        Download
                    </button>
                </div>
            ) : (
                ""
            )}
        </div>
    );
}
