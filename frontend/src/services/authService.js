import axios from "axios";
import { jwtDecode } from "jwt-decode";

const api = axios.create({
  baseURL: "http://localhost:8000",
});

export const register = async (details) => {
  const { data, status } = await api.post("/auth/register", details, {
    headers: { "Content-Type": "application/json" },
  });
  return { data, status };
};

export const login = async (details) => {
  const { data, status } = await api.post(
    "/auth/login",
    { username: details.username, password: details.password },
    { headers: { "Content-Type": "application/json" } }
  );
  return { data, status };
};

export const getUsernameFromToken = () => {
  const token = localStorage.getItem("token");
  if (!token) return null;

  const decoded = jwtDecode(token);
  console.log(decoded?.sub ?? null);
  return decoded?.sub ?? null;
};
