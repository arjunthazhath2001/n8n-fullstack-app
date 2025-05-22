import { useState } from 'react';
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    email: '',
    budget: '',
    message: '',
  });

  const [status, setStatus] = useState('');

  const BUDGET_OPTIONS = ['0-100', '100-1000', '1000+'];

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus('Submitting...');
    try {
      const response = await fetch('http://127.0.0.1:8000/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        setStatus('Form submitted successfully!');
        setFormData({
          first_name: '',
          last_name: '',
          email: '',
          budget: '',
          message: '',
        });
      } else {
        const errorData = await response.json();
        setStatus(`Submission failed: ${JSON.stringify(errorData)}`);
      }
    } catch (error) {
      setStatus(`Error: ${error.message}`);
    }
  };

  return (
    <div className="container">
      <h1>User Onboarding</h1>
      <form onSubmit={handleSubmit}>
        <input
          name="first_name"
          placeholder="First Name"
          value={formData.first_name}
          onChange={handleChange}
          required
        />
        <input
          name="last_name"
          placeholder="Last Name"
          value={formData.last_name}
          onChange={handleChange}
          required
        />
        <input
          name="email"
          placeholder="Email"
          type="email"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <select
          name="budget"
          value={formData.budget}
          onChange={handleChange}
          required
        >
          <option value="">Select Budget</option>
          {BUDGET_OPTIONS.map((option) => (
            <option key={option} value={option}>{option}</option>
          ))}
        </select>
        <textarea
          name="message"
          placeholder="Your message..."
          value={formData.message}
          onChange={handleChange}
          required
        />
        <button type="submit">Submit</button>
      </form>
      <p>{status}</p>
    </div>
  );
}

export default App;
