import React from "react";
import "./Footer.scss";

export default function Footer() {
    return (
        <div className="container text-center footer">
            Made by:{" "}
            <a
                href="https://colbe.me"
                target="__blank"
                id="name-link"
                rel="noreferrer"
            >
                Colbe Roberson
            </a>
            <br />
            <a
                href="https://github.com/cgr28/maze-creator-and-solver"
                target="_blank"
                id="github-link"
                rel="noreferrer"
            >
                GitHub
            </a>
            <br />
            <a
                href="https://github.com/cgr28/maze-creator-and-solver/tree/aws#maze-creator-algorithms"
                target="_blank"
                id="github-link"
                rel="noreferrer"
            >
                Algos Info
            </a>
        </div>
    );
}
