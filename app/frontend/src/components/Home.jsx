import React, { useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import AuthContext from '../context/AuthContext';
import axios from 'axios';

function Home() {
  const { isAuthenticated, setIsAuthenticated } = useContext(AuthContext);
  const navigate = useNavigate();

  // Retrieve the user's email from localStorage
  const userEmail = localStorage.getItem('email');

  const handleLogout = async () => {
    try {
      // Get the token from localStorage
      const token = localStorage.getItem('token');

      // Send a request to the backend to blacklist the token
      await axios.post(
        'http://localhost:8000/logout',
        {},
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );

      // Remove the token and email from localStorage
      localStorage.removeItem('token');
      localStorage.removeItem('email');

      // Set the authentication state to false
      setIsAuthenticated(false);

      // Redirect the user to the login page
      navigate('/login');
    } catch (error) {
      console.error('Logout failed:', error);
    }
  };

  // If the user is not authenticated, redirect to the login page
  if (!isAuthenticated) {
    navigate('/login');
    return null; // Return null to avoid rendering the home page
  }

  return (
    <div>
      <h1>Welcome to the Home Page</h1>
      <p>You are logged in as: {userEmail}</p>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
}

export default Home;