import logo from "./logo.svg";
import "./App.css";
import "./styles.css";
import TodoList from "./components/TodoList";
import TodoForm from "./components/TodoForm";

function App() {
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
    <div className="App">
      <div className="container">
        <h1>Create Todo</h1>
        <TodoForm />

        <h2>All Todos:</h2>
        <TodoList todos={sampletodos} />
      </div>
    </div>
  );
}

export default App;
