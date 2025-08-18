import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
});

const getTodos = async (username) => {
    const { data } = await api.get(`/todos/${encodeURIComponent(username)}`);
    return data;
}

const createTodo = async (todo) => {
    const { data, status } = await api.post(`/todos/create-todo`, todo)
    return { data, status };
}

export { getTodos, createTodo }