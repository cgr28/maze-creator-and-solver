import React from "react";
import "./Header.scss"

export default function Header({ text }) {
    return (
        <div className="header mt-3">
            {text}
        </div>
    )
}