import React, { useEffect, useState } from "react";
import { arrToMaze, mazeKey } from "../utils/MazeUtils";
import Spinner from 'react-bootstrap/Spinner';


export default function Maze({ maze, solInfo, height, width }) {
  const [canvas, setCanvas] = useState(0)
  const [loading, setLoading] = useState(1)
  useEffect(()=> {
    setCanvas(arrToMaze(maze, width, height, solInfo.solution))
    setLoading(0)
  }, [maze])
  return (
    <div>
      <div>Solver: {mazeKey[solInfo.search_type]}</div>
      <div>Cells Visited: {solInfo.visited_cells}</div>
      <div>Solution Length: {solInfo.solution_length}</div>
      {!loading ? <img src={canvas.toDataURL()} alt="maze" /> : <Spinner />}
      {!loading ? <div><a href={canvas.toDataURL()} download={`${solInfo.search_type}.png`}>Download</a></div> : ""}
    </div>
  );
}
