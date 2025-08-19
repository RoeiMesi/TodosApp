import React, { useState } from "react";
import { deleteTodo } from "../utils/todosService";

export default function TodoItem({ todo, dispatch }) {
  const { completed, created_at, priority, username, description, id, title } =
    todo;

  const priorityClass = {
    1: "priority-low",
    2: "priority-medium",
    3: "priority-high",
  };

  const handleDelete = async () => {
    try {
      const status = await deleteTodo(username, created_at);
      if (status === 204) {
        dispatch({ type: "DELETE_TODO", payload: { id } });
      }
    } catch (error) {
      console.error("Failed to delete todo:", error);
    }
  };

  return (
    <div className="todo-item">
      <div className={`priority-dot ${priorityClass[Number(priority)]}`}></div>
      <h3>{title}</h3>
      <p>{description}</p>

      <button className="button" onClick={handleDelete}>
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
