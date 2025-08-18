export default function todoReducer(state, action) {
  switch (action.type) {
    case "SET_TODOS":
      return { ...state, todos: action.payload };
    case "ADD_TODO":
      return { ...state, todos: [...state.todos, action.payload] };
    case "UPDATE_TODO":
      return {
        ...state,
        todos: state.todos.map((todo) =>
          todo.id === action.payload.id ? action.payload : todo
        ),
        editingTodo:
          state.editingTodo && state.editingTodo.id === action.payload.id
            ? null
            : state.editingTodo,
      };

    case "DELETE_TODO":
      return {
        ...state,
        todos: state.todos.filter((todo) => todo.id !== action.payload.id),
        editingTodo:
          state.editingTodo && state.editingTodo.id === action.payload.id
            ? null
            : state.editingTodo,
      };

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
