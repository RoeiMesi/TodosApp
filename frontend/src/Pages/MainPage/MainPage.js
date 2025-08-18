import React from "react";
import TodoForm from "../../components/TodoForm";
import TodoList from "../../components/TodoList";

export default function MainPage() {
  const sampletodos = [
    {
      title: "Hello",
      description: "description",
      priority: 1,
      completed: false,
    },
    {
      title: "Hello2",
      description: "description",
      priority: 1,
      completed: false,
    },
  ];

  return (
    <div className="container">
      <h1>Create Todo</h1>
      <TodoForm />

      <h2>All Todos:</h2>
      <TodoList todos={sampletodos} />
    </div>
  );
}
