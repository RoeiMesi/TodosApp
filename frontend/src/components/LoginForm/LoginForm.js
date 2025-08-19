import React, { useState } from "react";
import "./LoginForm.css";
import { login } from "../../utils/authService";
import { useNavigate } from "react-router-dom";

export default function LoginForm() {

  const navigate = useNavigate();

  const handleRegisterClick = () => {
    navigate('/register');
  };

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const clearForm = () => {
    setUsername("");
    setPassword("");
  };

  const handleLogin = async (e) => {
    e.preventDefault();

    const userDetails = {
      username,
      password
    };

    try {
      const { status, data } = await login(userDetails);
      if (status === 200 && data.access_token) {
        localStorage.setItem("token", data.access_token);
        window.location.href = "http://localhost:3000";
        alert("You successfully logged in!");
      }
    } catch (error) {
      console.error(error.response?.data?.detail || "Login failed");
      alert("Wrong credentials.");
    }
    
    clearForm();
  };

  return (
    <form onSubmit={handleLogin} className="login-form">
      <label>Username</label>
      <input
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      ></input>
      <label>Password</label>
      <input
        type="text"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      ></input>

      <button type='submit' className='button'>Submit</button>
      <button type='button' className='button' onClick={handleRegisterClick}>Register</button>
    </form>
  );
}
