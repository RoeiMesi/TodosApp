import logo from "./logo.svg";
import "./App.css";
import "./styles.css";
import TodoList from "./components/TodoList";
import TodoForm from "./components/TodoForm";
import MainPage from "./Pages/MainPage/MainPage";
import RegisterPage from "./Pages/RegisterPage/RegisterPage";
import LoginPage from "./Pages/LoginPage/LoginPage";
import { BrowserRouter, Router, Routes, Route, Link } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <nav>
          <ul>
            <li>
              <Link to="/register">Register Page</Link>
            </li>
            <li>
              <Link to='/login'>Login Page</Link>
            </li>
            <li>
              <Link to='/'>Main Page</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/register" element={<RegisterPage />}>
          </Route>
          <Route path="/login" element={<LoginPage />}>
          </Route>
          <Route path="/" element={<MainPage />}>
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
