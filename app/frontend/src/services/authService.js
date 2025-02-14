import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const login = async (credentials) => {
  const formData = new URLSearchParams();
  formData.append('username', credentials.username);
  formData.append('password', credentials.password);

  const response = await axios.post(`${API_URL}/auth/login`, formData, {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
  });
  return response.data;
};

export const logout = async () => {
  const token = localStorage.getItem('token');
  try {
    await axios.post(`${API_URL}/auth/logout`, null, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    localStorage.removeItem('token');
    localStorage.removeItem('email');
  } catch (error) {
    console.error('Logout error:', error);
    throw error;
  }
};

export const register = async (userData) => {
  const response = await axios.post(`${API_URL}/auth/register`, userData);
  return response.data;
};

export const googleLogin = async () => {
  const response = await axios.get(`${API_URL}/auth/google`);
  return response.data;
};

export const getProtectedData = async () => {
  const token = localStorage.getItem('token');
  const response = await axios.get(`${API_URL}/protected`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};