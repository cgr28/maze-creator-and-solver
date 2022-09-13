import "./App.css";
import React, { useState } from "react";

function App() {
    const [solver, setSolver] = useState("breadth-first-search");
    const [creator, setCreator] = useState("hunt-and-kill");

    const handleSubmit = (event) => {
      event.preventDefault()
    }

    const handleCreatorChange = (event) => {
        setCreator(event.target.value);
        console.log(event.target.value);
    };
    const handleSolverChange = (event) => {
        setSolver(event.target.value);
    };
    return (
        <div className="App">
            <form class="container mt-5" id="maze-form" onSubmit={handleSubmit}>
                <p class="header">Maze generator algorithm</p>
                <input
                    id="hunt-and-kill"
                    name="creator"
                    type="radio"
                    value="hunt-and-kill"
                    onChange={handleCreatorChange}
                    defaultChecked={true}
                />
                <label for="hunt-and-kill">Hunt and Kill</label>
                <input
                    id="growing-tree"
                    name="creator"
                    type="radio"
                    value="growing-tree"
                    onChange={handleCreatorChange}
                />
                <label for="growing-tree">Growing Tree</label>
                <input
                    id="prims"
                    name="creator"
                    type="radio"
                    value="prims"
                    onChange={handleCreatorChange}
                />
                <label for="prims">Prims</label>
                <br />
                <p class="header mt-4">Maze solver algorithm</p>
                <input
                    id="breadth-first-search"
                    name="solver"
                    type="radio"
                    value="breadth-first-search"
                    defaultChecked={true}
                    onChange={handleSolverChange}
                />
                <label for="breadth-first-search">Breadth First Search</label>
                <input
                    id="depth-first-search"
                    name="solver"
                    type="radio"
                    value="depth-first-search"
                    onChange={handleSolverChange}
                />
                <label for="depth-first-search">Depth First Search</label>
                <input
                    id="best-first-search"
                    name="solver"
                    type="radio"
                    value="best-first-search"
                    onChange={handleSolverChange}
                />
                <label for="best-first-search">Best First Search</label>
                <input
                    id="a-star"
                    name="solver"
                    type="radio"
                    value="a-star"
                    onChange={handleSolverChange}
                />
                <label for="a-star">A-Star</label>
                <input
                    id="none"
                    name="solver"
                    type="radio"
                    value="none"
                    onChange={handleSolverChange}
                />
                <label for="none">None</label>
                <br />
                <p class="header mt-4">Customize maze</p>
                <input
                    type="number"
                    min="5"
                    max="100"
                    value="20"
                    class="slider"
                    id="height"
                />
                <label for="height" id="slider-label">
                    Height (min: 5, max: 100)
                </label>
                <input
                    type="number"
                    min="5"
                    max="100"
                    value="20"
                    class="slider"
                    id="width"
                />
                <label for="width" id="slider-label">
                    Width (min: 5, max: 100)
                </label>
                <input
                    type="checkbox"
                    id="visited"
                    name="visited"
                    value="True"
                    defaultChecked={true}
                />
                <label for="Visited">Visited Cells</label>
                <br />
                <button
                    type="submit"
                    form="maze-form"
                    id="generate"
                    class="mt-4"
                    onclick="userAction()"
                >
                    Generate Maze
                </button>
            </form>
            <div class="mt-5" id="stats"></div>
            <div class="mt-5 mb-4 container" id="maze-container">
                Click the button to generate a maze.
            </div>
        </div>
    );
}

export default App;
