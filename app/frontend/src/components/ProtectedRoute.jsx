import React, { useContext } from 'react';
import { Navigate } from 'react-router-dom';
import AuthContext from '../context/AuthContext';

function ProtectedRoute({ children }) {
  const { isAuthenticated } = useContext(AuthContext);

  // If the user is not authenticated, redirect to the login page
  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  // If the user is authenticated, render the children (protected component)
  return children;
}

export default ProtectedRoute;