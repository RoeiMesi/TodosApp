import axios from "axios";

const api = axios.create({
  baseURL: "https://h5ufuelq83.execute-api.il-central-1.amazonaws.com",
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

api.interceptors.response.use(
  (res) => res,
  (err) => {
    const status = err?.response?.status;
    if (status === 401 || status === 403) {
      localStorage.removeItem("token");
      window.location.href = "/login";
    }
    return Promise.reject(err);
  }
);

const getTodos = async (username) => {
  const { data } = await api.get(`/todos/${encodeURIComponent(username)}`);
  return data;
};

const createTodo = async (todo) => {
  const { data, status } = await api.post(`/todos/create-todo`, todo);
  return { data, status };
};

const deleteTodo = async (username, createdAt) => {
  const { status } = await api.delete(
    `/todos/${encodeURIComponent(username)}/${encodeURIComponent(createdAt)}`
  );
  return status; // Should be 204 for success
};

const updateTodo = async (todo) => {
  const { status, data } = await api.put("/todos/update-todo", todo);
  return { status, data };
};

export { getTodos, createTodo, deleteTodo, updateTodo };
