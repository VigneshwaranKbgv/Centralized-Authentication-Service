import React from 'react';
import '../styles/toast.css';

export const Toast = ({ message, type }) => (
  <div className={`toast ${type}`}>
    {message}
  </div>
); 