import React, { useState } from "react";
import "./RegisterForm.css";

export default function RegisterForm() {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [firstname, setFirstname] = useState('');
    const [lastname, setLastname] = useState('');
    const [password, setPassword] = useState('');

    const clearForm = () => {
        setUsername('');
        setEmail('');
        setFirstname('');
        setLastname('');
        setPassword('');
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        clearForm();
    }

    return (
            <form onSubmit={handleSubmit} className='register-form'>
                <label>Username</label>
                <input
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                ></input>
                <label>E-mail</label>
                <input
                    type="text"
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
                    type="text"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                ></input>
            </form>
    )
}