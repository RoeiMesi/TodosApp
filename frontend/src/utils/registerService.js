import axios from 'axios';

const api = axios.create({
    baseURL:'http://localhost:8000',
});

export const register = async (details) => {
    const { data, status } = await api.post('/auth/register', details);
    return { data, status }
}