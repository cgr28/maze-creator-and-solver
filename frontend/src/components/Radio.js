import React from "react";
import "./Radio.scss";

export default function Radio({
    name,
    label,
    value,
    onChange,
    defaultChecked,
    group,
    disabled=false
}) {
    return (
        <>
            <input
                type={"radio"}
                id={name}
                value={value}
                onChange={onChange}
                defaultChecked={defaultChecked}
                name={group}
                disabled={disabled}
            />
            <label htmlFor={name}>{label}</label>
        </>
    );
}
