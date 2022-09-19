import "./App.scss";
import React, { useState } from "react";
import { getSolversQuery, solverTypes } from "./utils/Utils";
import Maze from "./components/Maze";
import Header from "./components/Header";
import Checkbox from "./components/Checkbox";
import NumInput from "./components/NumInput";
import Radio from "./components/Radio";

function App() {
    const [solvers, setSolvers] = useState(
        new Array(solverTypes.length).fill(false)
    );
    const [creator, setCreator] = useState("hunt-and-kill");
    const [width, setWidth] = useState(20);
    const [height, setHeight] = useState(20);
    const [vis, setVis] = useState(1);
    const [maze, setMaze] = useState();
    const [solutions, setSolutions] = useState([]);
    const [error, setError] = useState(false);
    const [loading, setLoading] = useState(0);

    const handleSubmit = (event) => {
        event.preventDefault();
        const solverParams = getSolversQuery(solvers, solverTypes);
        if (!solverParams) {
            setError("***Error, please select a solver algorithm.***");
            return;
        }
        setLoading(1);
        fetch(
            `/api/${creator}/${height}/${width}/${vis}${solverParams}`
        )
            .then((res) => res.json())
            .then((data) => {
                setMaze(data.maze);
                setSolutions(data.solutions);
                setError(false);
                setLoading(0);
            })
            .catch((error) => {
                setError("***Error, please try again.***");
                setLoading(0);
                return;
            });
    };

    const handleCreatorChange = (event) => {
        setCreator(event.target.value);
    };
    const handleSolverChange = (pos) => {
        const updatedSolvers = solvers.map((item, index) =>
            index === pos ? !item : item
        );
        setSolvers(updatedSolvers);
    };
    const handleWidthChange = (event) => {
        setWidth(event.target.value);
    };
    const handleHeightChange = (event) => {
        setHeight(event.target.value);
    };
    const handleVisChange = () => {
        vis ? setVis(0) : setVis(1);
    };
    return (
        <div className="App container">
            {error ? (
                <div className="text-center" id="error-message">
                    {error}
                </div>
            ) : (
                ""
            )}
            <div className="row">
                <div className="col-sm-12 col-md-6">
                    <form
                        className="mt-5 mx-auto"
                        id="maze-form"
                        onSubmit={handleSubmit}
                    >
                        <Header text={"Maze Creator Algorithms"} />

                        <Radio
                            name={"hunt-and-kill"}
                            value={"hunt-and-kill"}
                            onChange={handleCreatorChange}
                            defaultChecked={true}
                            label={"Hunt and Kill"}
                            group={"creator"}
                            disabled={loading}
                        />
                        <br />
                        <Radio
                            name={"growing-tree"}
                            value={"growing-tree"}
                            onChange={handleCreatorChange}
                            label={"Growing Tree"}
                            group={"creator"}
                            disabled={loading}
                        />
                        <br />
                        <Radio
                            name={"prims"}
                            value={"prims"}
                            onChange={handleCreatorChange}
                            label={"Prims"}
                            group={"creator"}
                            disabled={loading}
                        />
                        <br />
                        <Header text={"Maze Solver Algorithms"} />
                        {solverTypes.map(({ name, value }, index) => {
                            return (
                                <div key={index}>
                                    <Checkbox
                                        name={"solver"}
                                        label={name}
                                        value={value}
                                        checked={solvers[index]}
                                        onChange={() =>
                                            handleSolverChange(index)
                                        }
                                        disabled={loading}
                                    />
                                </div>
                            );
                        })}
                        <Header text={"Customize Maze"} />
                        <NumInput
                            min={5}
                            max={100}
                            value={height}
                            name={"height"}
                            onChange={handleHeightChange}
                            label={"Height (min: 5, max: 100)"}
                            disabled={loading}
                        />
                        <br />
                        <NumInput
                            min={5}
                            max={100}
                            value={width}
                            name={"width"}
                            onChange={handleWidthChange}
                            label={"Width (min: 5, max: 100)"}
                            disabled={loading}
                        />
                        <br />
                        <Checkbox
                            onChange={handleVisChange}
                            name="visited"
                            label={"Draw Visited Cells"}
                            checked={vis}
                            disabled={loading}
                        />
                        <br />
                        <Header text={"Key"} />
                        <div>
                            <div id="green">Green:&emsp;</div>solution path
                        </div>
                        <div>
                            <div id="yellow">Yellow:&emsp;</div>visited cell
                        </div>
                        <button
                            type="submit"
                            form="maze-form"
                            id="create-button"
                            className="mt-4"
                            disabled={loading}
                        >
                            Create Maze(s)
                        </button>
                    </form>
                </div>
                <div className="col-sm-12 col-md-6">
                    <div className="mt-5 mb-4" id="mazes">
                        <Header text={"Mazes"} />
                        {loading ? <div id={"loading"}>Loading...</div> : ""}
                        {maze
                            ? solutions.map((solution, index) => {
                                  return (
                                      <Maze
                                          width={width}
                                          height={height}
                                          maze={maze}
                                          solInfo={solution}
                                          id={index}
                                          key={index}
                                      />
                                  );
                              })
                            : "Click the button above to create a maze."}
                    </div>
                </div>
            </div>
        </div>
    );
}

export default App;
