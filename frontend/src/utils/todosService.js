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

const deleteTodo = async (username, createdAt) => {
    const { status } = await api.delete(`/todos/${encodeURIComponent(username)}/${encodeURIComponent(createdAt)}`);
    return status; // Should be 204 for success
}

const updateTodo = async(todo) => {
    const { status, data } = await api.put('/todos/update-todo', todo);
    return { status, data };
}

export { getTodos, createTodo, deleteTodo, updateTodo }