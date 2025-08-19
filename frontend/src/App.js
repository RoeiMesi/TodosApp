
import "./App.css";
import "./styles.css";
import TodoPage from "./Pages/Todo/TodoPage";
import RegisterPage from "./Pages/Register/RegisterPage";
import LoginPage from "./Pages/Login/LoginPage";
import { BrowserRouter, Routes, Route } from "react-router-dom";
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
