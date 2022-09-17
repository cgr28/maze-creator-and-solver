import React, { useEffect, useState } from "react";
import { arrToMaze, mazeKey } from "../utils/MazeUtils";
import Spinner from 'react-bootstrap/Spinner';
import "./Maze.scss"


export default function Maze({ maze, solInfo, height, width }) {
  const [canvas, setCanvas] = useState(0)
  useEffect(()=> {
    setCanvas(arrToMaze(maze, width, height, solInfo.solution).toDataURL())
  }, [maze])
  return (
    <div className="maze mt-3">
      <div>Solver: {mazeKey[solInfo.search_type]}</div>
      <div>Cells Visited: {solInfo.visited_cells}</div>
      <div>Solution Length: {solInfo.solution_length}</div>
      {canvas ? <img src={canvas} alt="maze" /> : <Spinner />}
      {canvas ? <div className="mt-2"><a href={canvas} download={`${solInfo.search_type}.png`}>Download</a></div> : ""}
    </div>
  );
}
