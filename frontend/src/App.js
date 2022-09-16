import "./App.css";
import React, { useState } from "react";
import { getSolversQuery } from "./utils/Utils";
import Maze from "./components/Maze"

const solverTypes = [{name: "Breadth First Search", value: "breadth-first-search"}, {name: "Depth First Search", value: "depth-first-search"}, {name: "Best First Search", value: "best-first-search"}, {name: "A-Star", value: "a-star"}, {name: "None", value: "none"}]

function App() {
    const [solvers, setSolvers] = useState(
            new Array(solverTypes.length).fill(false)
        );
        const [creator, setCreator] = useState("hunt-and-kill");
        const [width, setWidth] = useState(20)
        const [height, setHeight] = useState(20)
        const [vis, setVis] = useState(1)
        const [maze, setMaze] = useState()
        const [solutions, setSolutions] = useState([])
        
    const handleSubmit = (event) => {
      event.preventDefault()
      console.log("creating maze...")
      const solverParams = getSolversQuery(solvers, solverTypes);
      fetch(
        `http://localhost:8080/api/${creator}/${height}/${width}/${vis}${solverParams}`
      )
        .then((res) => res.json())
        .then((data) => {
            setMaze(data.maze);
            setSolutions(data.solutions)
        })
        .catch((error) => {
          console.log(error);
          return;
        });

    }
    
    const handleCreatorChange = (event) => {
        setCreator(event.target.value);
    };
    const handleSolverChange = (pos) => {
        const updatedSolvers = solvers.map((item, index) =>
            index === pos ? !item : item
        );
        setSolvers(updatedSolvers)
    };
    const handleWidthChange = (event) => {
        setWidth(event.target.value)
    };
    const handleHeightChange = (event) => {
        setHeight(event.target.value)
    }
    const handleVisChange = () => {
        vis ? setVis(0) : setVis(1);
    }
    return (
        <div className="App">
            <form className="container mt-5" id="maze-form" onSubmit={handleSubmit}>
                <p className="header">Maze Creator Algorithm</p>
                <input
                    id="hunt-and-kill"
                    name="creator"
                    type="radio"
                    value="hunt-and-kill"
                    onChange={handleCreatorChange}
                    defaultChecked={true}
                />
                <label htmlFor="hunt-and-kill">Hunt and Kill</label>
                <input
                    id="growing-tree"
                    name="creator"
                    type="radio"
                    value="growing-tree"
                    onChange={handleCreatorChange}
                />
                <label htmlFor="growing-tree">Growing Tree</label>
                <input
                    id="prims"
                    name="creator"
                    type="radio"
                    value="prims"
                    onChange={handleCreatorChange}
                />
                <label htmlFor="prims">Prims</label>
                <br />
                <p className="header mt-4">Maze Solver Algorithm</p>
                    {
                        solverTypes.map(({ name, value }, index) => {
                            return (<div key={index}>
                                <input 
                                    type="checkbox"
                                    name="solver"
                                    id={value}
                                    value={value}
                                    checked={solvers[index]}
                                    onChange={() => handleSolverChange(index)}
                                    />
                                <label htmlFor={value}>{name}</label>
                            </div>)
                        })
                    }
                <br />
                <p className="header mt-4">Customize maze</p>
                <input
                    type="number"
                    min="5"
                    max="100"
                    value={height}
                    className="slider"
                    id="height"
                    onChange={handleHeightChange}
                />
                <label htmlFor="height" id="slider-label">
                    Height (min: 5, max: 100)
                </label>
                <input
                    type="number"
                    min="5"
                    max="100"
                    value={width}
                    className="slider"
                    id="width"
                    onChange={handleWidthChange}
                />
                <label htmlFor="width" id="slider-label">
                    Width (min: 5, max: 100)
                </label>
                <input
                    type="checkbox"
                    id="visited"
                    name="visited"
                    value="True"
                    defaultChecked={true}
                    onChange={handleVisChange}
                />
                <label htmlFor="Visited">Visited Cells</label>
                <br />
                <button
                    type="submit"
                    form="maze-form"
                    id="generate"
                    className="mt-4"
                >
                    Create Maze(s)
                </button>
            </form>
            <div className="mt-5" id="stats"></div>
            <div className="mt-5 mb-4 container" id="maze-container">
                {maze ? 
                    solutions.map((solution) => {
                        return (
                            <Maze width={width} height={height} maze={maze} solInfo={solution} />
                        )
                    })
                        : 
                    "Click the button above to create a maze."}
            </div>
        </div>
    );
}

export default App;
