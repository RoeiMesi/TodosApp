import React, { useReducer, useEffect } from "react";
import TodoForm from "../../components/Todo/TodoForm";
import TodoList from "../../components/Todo/TodoList";
import { sortTodos } from "../../utils/sortingUtilities";
import todoReducer from "../../reducers/todoReducer";
import { getTodos } from "../../services/todosService";
import { getUsernameFromToken } from "../../services/authService";

export default function TodoPage() {
  const initialState = {
    todos: [],
    editingTodo: null,
    sortPreference: "High to Low",
  };

  const [state, dispatch] = useReducer(todoReducer, initialState);

  useEffect(() => {
    const username = getUsernameFromToken();
    (async () => {
      try {
        const todos = await getTodos(`${username}`);
        dispatch({ type: "SET_TODOS", payload: todos });
      } catch (error) {
        console.error("Failed to fetch todos:", error);
      }
    })();
  }, []);

  const sortedTodos = sortTodos(state.todos, state.sortPreference);

  const handleLogout = () => {
    localStorage.removeItem("token");
    window.location.href = "http://localhost:3000";
    alert('Logged out successfully!');
  };

  return (
    <div className="container">
      <button className="logout-button" onClick={handleLogout}>
        Logout
      </button>
      <h1>Create Todo</h1>
      <TodoForm dispatch={dispatch} editingTodo={state.editingTodo}></TodoForm>

      {state.todos.length > 0 && (
        <div className="todos">
          <h2>All Todos:</h2>

          <select
            value={state.sortPreference}
            onChange={(e) =>
              dispatch({ type: "SET_SORTING", payload: e.target.value })
            }
          >
            <option value="High to Low">High to Low</option>
            <option value="Low to High">Low to High</option>
          </select>

          <TodoList todos={sortedTodos} dispatch={dispatch}></TodoList>
        </div>
      )}
    </div>
  );
}
