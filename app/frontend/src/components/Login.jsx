import React, { useState, useContext } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { login } from '../services/authService';
import AuthContext from '../context/AuthContext';

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
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Login</button>
      </form>
      <button onClick={handleGoogleLogin}>Login with Google</button>
      <p>
        Don't have an account? <Link to="/register">Register here</Link>
      </p>
    </div>
  );
}

export default Login;