import React, { useState, useContext } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { login } from '../services/authService';
import AuthContext from '../context/AuthContext';
import '../styles/auth.css';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();
  const { setIsAuthenticated } = useContext(AuthContext);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Send username instead of email
      const response = await login({ username: email, password });
      
      // Store the token and email in localStorage
      localStorage.setItem('token', response.access_token);
      localStorage.setItem('email', response.email); // Store the email
      console.log('Token stored:', response.access_token);
      console.log('Email stored:', response.email);

      // Update the authentication state
      setIsAuthenticated(true);

      // Redirect to the home page
      console.log('Redirecting to home page...');
      navigate('/');
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  const handleGoogleLogin = () => {
    window.location.href = 'http://localhost:8000/auth/google';
  };

  return (
    <div className="login-container">
      <h1>Centralized Authentication Service</h1>
      <h2>Welcome Back</h2>
      <p className="service-description">
        Secure, Simple, and Seamless Authentication Solution
      </p>
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          placeholder="Enter your email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="password"
          placeholder="Enter your password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Sign In</button>
      </form>
      <button className="google-button" onClick={handleGoogleLogin}>
        <img src="/google-icon.svg" alt="Google" width="18" height="18" />
        Continue with Google
      </button>
      <p>
        Don't have an account? <Link to="/register">Create Account</Link>
      </p>
    </div>
  );
}

export default Login;