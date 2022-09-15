import React, { useEffect, useState } from "react";
import { arrToMaze } from "../utils/MazeUtils";
import Spinner from 'react-bootstrap/Spinner';


export default function Maze({ maze, sol, height, width }) {
  const [canvas, setCanvas] = useState(0)
  useEffect(()=> {
    setCanvas(arrToMaze(maze, width, height, sol))
  }, [maze])
  return (
    <div>
      {canvas ? <img src={canvas.toDataURL()} alt="maze" /> : <Spinner />}
    </div>
  );
}
