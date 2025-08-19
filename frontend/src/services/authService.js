import axios from "axios";
import { jwtDecode } from 'jwt-decode';

const api = axios.create({
  baseURL: "http://localhost:8000",
});

export const register = async (details) => {
  const { data, status } = await api.post("/auth/register", details);
  return { data, status };
};

export const login = async (details) => {
  const params = new URLSearchParams();
  params.append("username", details.username);
  params.append("password", details.password);

  const { data, status } = await api.post("/auth/token", params, {
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
  });

  return { data, status };
};

export const getUsernameFromToken = () => {
  const token = localStorage.getItem("token");
  if (!token) return null;

  const decoded = jwtDecode(token);
  console.log(decoded?.sub ?? null);
  return decoded?.sub ?? null;
};
