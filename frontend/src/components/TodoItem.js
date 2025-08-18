import React, { useState } from "react";

export default function TodoItem({ todo, dispatch }) {
  const { title, description, priority, completed, dateCreated } = todo;

  const priorityClass = {
    1: "priority-low",
    2: "priority-medium",
    3: "priority-high",
  };

  return (
    <div className="todo-item">
      <div className={`priority-dot ${priorityClass[todo.priority]}`}></div>
      <h3>{title}</h3>
      <p>{description}</p>

      <button
        className="button"
        onClick={() =>
          dispatch({ type: "DELETE_TODO", payload: { dateCreated } })
        }
      >
        Delete
      </button>

      <button
        className="button"
        onClick={() => dispatch({ type: "SET_EDITING_TODO", payload: todo })}
      >
        Edit
      </button>
    </div>
  );
}
