import React from "react";
import TodoItem from "./TodoItem";

export default function TodoList({ todos, dispatch }) {
  return (
    <div className="todo-list">
      {todos.map((todo, idx) => (
        <TodoItem
          key={todo.id ?? todo.dateCreated ?? idx}
          dispatch={dispatch}
          todo={todo}
        ></TodoItem>
      ))}
    </div>
  );
}
