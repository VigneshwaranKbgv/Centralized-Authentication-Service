import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const login = async (credentials) => {
  // Convert the credentials object to URL-encoded format
  const formData = new URLSearchParams();
  formData.append('username', credentials.username); // Use 'username' instead of 'email'
  formData.append('password', credentials.password);

  const response = await axios.post(`${API_URL}/token`, formData, {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded', // Set the correct content type
    },
  });
  return response.data;
};

export const register = async (user) => {
  const response = await axios.post(`${API_URL}/register`, user);
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