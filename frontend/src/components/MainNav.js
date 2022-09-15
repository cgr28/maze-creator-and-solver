import React from "react";
import "./MainNav.scss"

export default function MainNav() {
    return (
        <nav className="navbar main-nav">
            <div className="container-fluid">
                <a className="navbar-brand">Maze Creator and Solver</a>
                <div className="navbar-nav">
                    <a
                        className="nav-link"
                        href="https://github.com/cgr28/maze-creator-and-solver"
                        target="_blank"
                    >
                        Github
                    </a>
                </div>
            </div>
        </nav>
    );
}
