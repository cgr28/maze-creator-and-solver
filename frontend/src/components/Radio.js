import React from "react";
import "./Radio.scss";

export default function Radio({
    name,
    label,
    value,
    onChange,
    defaultChecked,
    group,
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
            />
            <label htmlFor={name}>{label}</label>
        </>
    );
}
