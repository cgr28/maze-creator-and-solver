import React from "react";
import "./Checkbox.scss"

export default function Checkbox({ onChange, defaultChecked=false, checked, value, label, name }) {
    return (
        <>
        <input
        onChange={onChange}
        id={name}
        value={value}
        type="checkbox"
        checked={checked}
        defaultChecked={defaultChecked}
        />
        <label htmlFor={name}>{label}</label>
        </>
    )
}