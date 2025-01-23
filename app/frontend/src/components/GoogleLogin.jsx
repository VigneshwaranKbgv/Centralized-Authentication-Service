import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

function GoogleLogin() {
  const navigate = useNavigate();

  useEffect(() => {
    // Redirect the user to the backend's /auth/google endpoint
    window.location.href = 'http://localhost:8000/auth/google';
  }, [navigate]);

  // Display a loading message while redirecting
  return <div>Redirecting to Google...</div>;
}

export default GoogleLogin;