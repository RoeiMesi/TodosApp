import logo from "./logo.svg";
import "./App.css";
import "./styles.css";
import TodoList from "./components/TodoList";
import TodoForm from "./components/TodoForm";
import TodoPage from "./Pages/TodoPage/TodoPage";
import RegisterPage from "./Pages/RegisterPage/RegisterPage";
import LoginPage from "./Pages/LoginPage/LoginPage";
import { BrowserRouter, Router, Routes, Route, Link } from "react-router-dom";
import PrivateRoute from "./PrivateRoute";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/register" element={<RegisterPage />}></Route>
          <Route path="/login" element={<LoginPage />}></Route>
          <Route
            path="/"
            element={
              <PrivateRoute>
                <TodoPage />
              </PrivateRoute>
            }
          ></Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
