import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import '../styles/auth.css';
import { sendResetCode, verifyResetCode } from '../services/authService';

function ForgotPassword() {
  const [email, setEmail] = useState('');
  const [verificationCode, setVerificationCode] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [showCodeInput, setShowCodeInput] = useState(false);
  const [message, setMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSendCode = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setError('');
    setMessage('');

    try {
      const response = await sendResetCode(email);
      setMessage(response.data.message);
      setShowCodeInput(true);
    } catch (error) {
      setError(error.response?.data?.detail || 'An error occurred');
    } finally {
      setIsLoading(false);
    }
  };

  const handleResetPassword = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setError('');
    setMessage('');

    try {
      const response = await verifyResetCode(email, verificationCode, newPassword);
      setMessage(response.data.message);
      setTimeout(() => {
        window.location.href = '/login';
      }, 2000);
    } catch (error) {
      setError(error.response?.data?.detail || 'An error occurred');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="login-container">
      <h1>Reset Password</h1>
      {!showCodeInput ? (
        <>
          <p className="service-description">
            Enter your email address and we'll send you a verification code.
          </p>
          {message && <div className="message success">{message}</div>}
          {error && <div className="message error">{error}</div>}
          <form onSubmit={handleSendCode}>
            <input
              type="email"
              placeholder="Enter your email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
            <button 
              type="submit" 
              className={isLoading ? 'loading-button' : ''}
              disabled={isLoading}
            >
              {isLoading ? 'Sending...' : 'Send Code'}
            </button>
          </form>
        </>
      ) : (
        <>
          <p className="service-description">
            Enter the verification code sent to your email and your new password.
          </p>
          {message && <div className="message success">{message}</div>}
          {error && <div className="message error">{error}</div>}
          <form onSubmit={handleResetPassword}>
            <input
              type="text"
              placeholder="Enter verification code"
              value={verificationCode}
              onChange={(e) => setVerificationCode(e.target.value)}
              required
            />
            <input
              type="password"
              placeholder="Enter new password"
              value={newPassword}
              onChange={(e) => setNewPassword(e.target.value)}
              required
            />
            <button 
              type="submit" 
              className={isLoading ? 'loading-button' : ''}
              disabled={isLoading}
            >
              {isLoading ? 'Resetting...' : 'Reset Password'}
            </button>
          </form>
        </>
      )}
      <p>
        <Link to="/login">Back to Login</Link>
      </p>
    </div>
  );
}

export default ForgotPassword; 