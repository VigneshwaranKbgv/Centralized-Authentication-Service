import React, { useEffect, useContext } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';
import AuthContext from '../context/AuthContext';

function LoginSuccess() {
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();
  const { setIsAuthenticated } = useContext(AuthContext);

  useEffect(() => {
    // Extract the token and email from the query parameter
    const token = searchParams.get('token');
    const email = searchParams.get('email');

    if (token && email) {
      // Store the token and email in localStorage
      localStorage.setItem('token', token);
      localStorage.setItem('email', email); // Store the email
      console.log('Token stored:', token);
      console.log('Email stored:', email);

      // Update the authentication state
      setIsAuthenticated(true);

      // Redirect to the home page
      console.log('Redirecting to home page...');
      navigate('/');
    } else {
      console.error('No token or email found in the URL');
      navigate('/login'); // Redirect to login page if no token or email is found
    }
  }, [searchParams, navigate, setIsAuthenticated]);

  return <div>Logging you in...</div>;
}

export default LoginSuccess;