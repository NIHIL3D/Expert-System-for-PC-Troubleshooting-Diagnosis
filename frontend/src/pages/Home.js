// Home.js
import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div className="container home-container">
      
      <h1>Choose your role</h1>
      <Link to="/client" className="btn">Client</Link>
      <Link to="/expert/login" className="btn">Expert</Link>
    </div>
  );
}

export default Home;
