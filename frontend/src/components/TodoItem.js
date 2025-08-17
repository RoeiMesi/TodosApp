import React, { useState } from "react";

export default function TodoItem( {todo} ) {
    const { title, description, priority, completed } = todo

    return (
        <div className="todo-item">
            <h1>{title}</h1>
            <h1>{description}</h1>
            <h1>{priority}</h1>
            <h1>{completed}</h1>
        </div>
    );
}