import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './components/Login';
import Register from './components/Register';
import GoogleLogin from './components/GoogleLogin';
import LoginSuccess from './components/LoginSuccess';
import Home from './components/Home';
import ProtectedRoute from './components/ProtectedRoute'; // Import the ProtectedRoute component

function App() {
  return (
    <Router>
      <Routes>
        {/* Protect the home route */}
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <Home />
            </ProtectedRoute>
          }
        />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/google-login" element={<GoogleLogin />} />
        <Route path="/login-success" element={<LoginSuccess />} />
      </Routes>
    </Router>
  );
}

export default App;