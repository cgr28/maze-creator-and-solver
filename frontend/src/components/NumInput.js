import React from "react";
import "./NumInput.scss";

export default function NumInput({ name, value, onChange, min, max, label, disabled=false }) {
    return (
        <>
            <input
                type={"number"}
                min={min}
                max={max}
                id={name}
                value={value}
                onChange={onChange}
                className={"num-input mt-1"}
                disabled={disabled}
            />
            <label htmlFor={name}>{label}</label>
        </>
    );
}
