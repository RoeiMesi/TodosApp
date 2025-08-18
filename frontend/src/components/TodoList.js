import React from "react";
import TodoItem from "./TodoItem";

export default function TodoList({ todos, dispatch }) {
  return (
    <div className="todo-list">
      {todos.map((todo) => (
        <TodoItem
          key={todo.createdAt}
          dispatch={dispatch}
          todo={todo}
        ></TodoItem>
      ))}
    </div>
  );
}
