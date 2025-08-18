export default function todoReducer(state, action) {
  switch (action.type) {
    case "ADD_TODO":
      return { ...state, todos: [...state.todos, action.payload] };
    case "UPDATE_TODO":
      return {
        ...state,
        todos: state.todos.map((todo) =>
          todo.dateCreated === action.payload.dateCreated
            ? action.payload
            : todo
        ),
      };
    case "DELETE_TODO":
      if (
        state.editingTodo &&
        state.editingTodo.dateCreated === action.payload.dateCreated
      ) {
        return {
          ...state,
          todos: state.todos.filter(
            (todo) => todo.dateCreated !== action.payload.dateCreated
          ),
          editingTodo: null,
        };
      } else {
        return {
          ...state,
          todos: state.todos.filter(
            (todo) => todo.dateCreated !== action.payload.dateCreated
          ),
        };
      }
    case "SET_EDITING_TODO":
      return {
        ...state,
        editingTodo: action.payload,
      };
    case "CLEAR_EDITING_TODO":
      return {
        ...state,
        editingTodo: null,
      };
    case "SET_SORTING":
      return {
        ...state,
        sortPreference: action.payload,
      };

    default:
      return state;
  }
}
