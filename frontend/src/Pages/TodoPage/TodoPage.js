import React, { useReducer } from "react";
import TodoForm from "../../components/TodoForm";
import TodoList from "../../components/TodoList";
import { sortTodos } from "../../utils/sortingUtilities";
import todoReducer from "../../reducers/todoReducer";

export default function TodoPage() {
  const initialState = {
    todos: [],
    editingTodo: null,
    sortPreference: "High to Low",
  };

  const [state, dispatch] = useReducer(todoReducer, initialState);

  const sortedTodos = sortTodos(state.todos, state.sortPreference);

  return (
    <div className="container">
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

          <TodoList
          todos={sortedTodos}
          dispatch={dispatch}
          ></TodoList>
        </div>
      )}
    </div>
  );
}
