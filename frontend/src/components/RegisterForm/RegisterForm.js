import React, { useState } from "react";
import "./RegisterForm.css";
import { register } from "../../utils/registerService";

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

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        
        const userData = {
            username,
            email,
            firstname,
            lastname,
            password
        };

        try {
            const { data, status } = await register(userData);
            if (status === 201) {
                console.log(data.message);
            }
        } catch (error) {
            console.error(error.message);
        }
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

                <button type='submit' className='button'>Submit</button>
            </form>
    )
}