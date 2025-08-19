import React, { useState } from "react";
import "./RegisterForm.css";
import { register } from "../../utils/authService";
import { useNavigate } from "react-router-dom";

export default function RegisterForm() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [firstname, setFirstname] = useState("");
  const [lastname, setLastname] = useState("");
  const [password, setPassword] = useState("");
  
  const navigate = useNavigate();

  const clearForm = () => {
    setUsername("");
    setEmail("");
    setFirstname("");
    setLastname("");
    setPassword("");
  };

  const handleLoginClick = () => {
    navigate('/login');
    alert('Moved to login page');
  };

  const handleRegister = async (e) => {
    e.preventDefault();

    const userData = {
      username,
      email,
      firstname,
      lastname,
      password,
    };

    if (!userData.username || !userData.email || !userData.firstname || !userData.lastname || !userData.password) {
      alert('You must fill all fields to register!');
      return;
    }

    try {
      const { data, status } = await register(userData);
      if (status === 201) {
        console.log(data.message);
        alert(data.message);
      }
    } catch (error) {
      console.error(error.response?.data?.detail);
      alert(error.response?.data?.detail);
    }
    clearForm();
  };

  return (
    <form onSubmit={handleRegister} className="register-form">
      <label>Username</label>
      <input
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      ></input>
      <label>E-mail</label>
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      ></input>
      <label>First name</label>
      <input
        type="text"
        value={firstname}
        onChange={(e) => setFirstname(e.target.value)}
      ></input>
      <label>Last name</label>
      <input
        type="text"
        value={lastname}
        onChange={(e) => setLastname(e.target.value)}
      ></input>
      <label>Password</label>
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      ></input>

      <button type="submit" className="button">
        Submit
      </button>
      <button type="button" className="button" onClick={handleLoginClick}>Login</button>
    </form>
  );
}
