import React from "react";
import "./Checkbox.scss";

export default function Checkbox({ onChange, checked, value, label, name }) {
    return (
        <>
            <input
                onChange={onChange}
                id={name}
                value={value}
                type="checkbox"
                checked={checked}
            />
            <label htmlFor={name}>{label}</label>
        </>
    );
}
