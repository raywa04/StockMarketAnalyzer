import React, { useState } from 'react';
import axios from 'axios';

const Dashboard = () => {
  const [symbol, setSymbol] = useState('');
  const [image, setImage] = useState('');
  const [message, setMessage] = useState('');

  const handleVisualize = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.get(`http://localhost:5000/visualize?symbol=${symbol}`);
      setImage(response.data.image_url);
      setMessage('');
    } catch (error) {
      setMessage('Failed to fetch data.');
    }
  };

  const handleUpdate = async (event) => {
    event.preventDefault();
    try {
      const formData = new FormData();
      formData.append('symbol', symbol);
      const response = await axios.post('http://localhost:5000/update_dashboard', formData);
      setMessage(response.data.message);
    } catch (error) {
      setMessage('Failed to update dashboard.');
    }
  };

  return (
    <div className="container">
      <h1 className="my-4">Real-Time Stock Market Dashboard</h1>
      <form className="mb-4" onSubmit={handleVisualize}>
        <div className="mb-3">
          <label htmlFor="symbol" className="form-label">Enter Stock Symbol</label>
          <input
            type="text"
            id="symbol"
            className="form-control"
            value={symbol}
            onChange={(e) => setSymbol(e.target.value)}
            required
          />
        </div>
        <button type="submit" className="btn btn-primary me-2">Visualize Data</button>
        <button type="button" className="btn btn-secondary" onClick={handleUpdate}>Update Dashboard</button>
      </form>
      {message && <div className="alert alert-info">{message}</div>}
      {image && <img src={image} alt="Stock Visualization" className="img-fluid" />}
    </div>
  );
};

export default Dashboard;
