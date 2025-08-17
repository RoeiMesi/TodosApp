import React from "react";
import TodoItem from "./TodoItem";

export default function TodoList({ todos }) {
  return (
    <div className="todo-list">
      {todos.map((todo) => (
        <TodoItem todo={todo}></TodoItem>
      ))}
    </div>
  );
}
