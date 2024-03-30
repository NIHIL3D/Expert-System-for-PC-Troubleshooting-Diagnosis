import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';

function ExpertLoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const history = useHistory();

  const handleLogin = async () => {
    setError('');
    try {
      const response = await fetch('/api/expert/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
      });
      if (response.ok) {
        history.push('/expert/add-problem');
      } else {
        const data = await response.json();
        setError(data.error);
      }
    } catch (error) {
      console.error('Error logging in:', error);
      setError('An unexpected error occurred');
    }
  };

  return (
    <div className="container login-container">
      <h1>Expert Login</h1>
      <div>
        <label>Email:</label>
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
      </div>
      <div>
        <label>Password:</label>
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      </div>
      {error && <div className="error">{error}</div>}
      <button onClick={handleLogin} className="btn">Login</button>
    </div>
  );
}

export default ExpertLoginPage;
