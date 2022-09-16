import "./App.css";
import React, { useState } from "react";
import { getSolversQuery, solverTypes } from "./utils/Utils";
import Maze from "./components/Maze"
import Header from "./components/Header";
import Checkbox from "./components/Checkbox";
import NumInput from "./components/NumInput";
import Radio from "./components/Radio";

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
    const [error, setError] = useState(false)
        
    const handleSubmit = (event) => {
      event.preventDefault()
      console.log("creating maze...")
      const solverParams = getSolversQuery(solvers, solverTypes);
      if (!solverParams) {

      }
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
                <Header text={"Maze Creator Algorithms"} />

                <Radio name={"hunt-and-kill"} value={"hunt-and-kill"} onChange={handleCreatorChange} defaultChecked={true} label={"Hunt and Kill"} group={"creator"} /><br/>
                <Radio name={"growing-tree"} value={"growing-tree"} onChange={handleCreatorChange} label={"Growing Tree"} group={"creator"} /><br/>
                <Radio name={"prims"} value={"prims"} onChange={handleCreatorChange} label={"Prims"} group={"creator"} /><br/>
                <br />
                <Header text={"Maze Solver Algorithms"} />
                    {
                        solverTypes.map(({ name, value }, index) => {
                            return (<div key={index}>
                                <Checkbox name={value} label={name} value={value} checked={solvers[index]} onChange={() => handleSolverChange(index)} />
                            </div>)
                        })
                    }
                <br />
                <Header text={"Customize Maze"} />
                <NumInput min={5} max={100} value={height} name={"height"} onChange={handleHeightChange} label={"Height (min: 5, max: 100)"}/><br/>
                <NumInput min={5} max={100} value={width} name={"width"} onChange={handleWidthChange} label={"Width (min: 5, max: 100)"}/><br/>
                <Checkbox onChange={handleVisChange} name="visited" defaultChecked={true} label={"Visited Cells"}/><br/>
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
