import React from "react";
import "./MainNav.scss"

export default function MainNav() {
    return (
        <nav class="navbar main-nav">
            <div class="container-fluid">
                <a class="navbar-brand">Maze Creator and Solver</a>
                <div class="navbar-nav">
                    <a
                        class="nav-link"
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
