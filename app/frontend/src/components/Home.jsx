import React, { useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import AuthContext from '../context/AuthContext';
import { logout } from '../services/authService';
import '../styles/auth.css';

function Home() {
  const { isAuthenticated, setIsAuthenticated } = useContext(AuthContext);
  const navigate = useNavigate();

  // Retrieve the user's email from localStorage
  const userEmail = localStorage.getItem('email');

  const handleLogout = async () => {
    try {
      await logout();
      setIsAuthenticated(false);
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
    <div className="home-container">
      <div className="welcome-header">
        <h1>Welcome Back, {userEmail}</h1>
        <p className="user-info">Your secure authentication dashboard</p>
        <button className="logout-button" onClick={handleLogout}>
          Logout
        </button>
      </div>

      <div className="features-grid">
        <div className="feature-card">
          <img src="/images/security.svg" alt="Security" className="feature-icon" />
          <h3>Secure Authentication</h3>
          <p>Your data is protected with industry-standard security protocols and encryption.</p>
        </div>
        <div className="feature-card">
          <img src="/images/integration.svg" alt="Integration" className="feature-icon" />
          <h3>Google Integration</h3>
          <p>Seamlessly sign in with your Google account for quick access.</p>
        </div>
        <div className="feature-card">
          <img src="/images/speed.svg" alt="Speed" className="feature-icon" />
          <h3>Fast & Reliable</h3>
          <p>Experience lightning-fast authentication with our optimized service.</p>
        </div>
      </div>
    </div>
  );
}

export default Home;