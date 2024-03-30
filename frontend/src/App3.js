import React, { useState, useEffect } from 'react';

function App() {
  const [symptoms, setSymptoms] = useState([]);
  const [selectedSymptoms, setSelectedSymptoms] = useState([]);
  const [diagnosedIssues, setDiagnosedIssues] = useState([]);
  const [newFaulty, setNewFaulty] = useState('');
  const [newFaultySymptoms, setNewFaultySymptoms] = useState('');

  useEffect(() => {
    // Fetch symptoms from Flask API
    fetch('/api/symptoms')
      .then(response => response.json())
      .then(data => {
        setSymptoms(data.symptoms);
      })
      .catch(error => {
        console.error('Error fetching symptoms:', error);
      });
  }, []);

  const handleSymptomChange = (event) => {
    const { value, checked } = event.target;
    if (checked) {
      setSelectedSymptoms(prevSelected => [...prevSelected, value]);
    } else {
      setSelectedSymptoms(prevSelected => prevSelected.filter(symptom => symptom !== value));
    }
  };

  const diagnoseIssues = () => {
    fetch('/api/diagnose', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ symptoms: selectedSymptoms })
    })
      .then(response => response.json())
      .then(data => {
        setDiagnosedIssues(data.faulty_issues);
      })
      .catch(error => {
        console.error('Error diagnosing issues:', error);
      });
  };

  const addFaulty = () => {
    fetch('/api/add-symptom', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ issue: newFaulty, symptom: newFaultySymptoms })
    })
      .then(response => response.json())
      .then(data => {
        console.log(data.message);
      })
      .catch(error => {
        console.error('Error adding faulty:', error);
      });
  };

  return (
    <div>
      <h1>Symptom Checker</h1>
      <h2>Symptoms</h2>
      <ul>
        {symptoms.map(symptom => (
          <li key={symptom}>
            <label>
              <input
                type="checkbox"
                value={symptom}
                checked={selectedSymptoms.includes(symptom)}
                onChange={handleSymptomChange}
              />
              {symptom}
            </label>
          </li>
        ))}
      </ul>
      <button onClick={diagnoseIssues}>Diagnose Issues</button>
      <h2>Diagnosed Issues</h2>
      <ul>
        {diagnosedIssues.map((issue, index) => (
          <li key={index}>{issue}</li>
        ))}
      </ul>
      <h2>Add Faulty</h2>
      <input
        type="text"
        placeholder="Faulty Name"
        value={newFaulty}
        onChange={(e) => setNewFaulty(e.target.value)}
      />
      <input
        type="text"
        placeholder="Associated Symptoms (comma separated)"
        value={newFaultySymptoms}
        onChange={(e) => setNewFaultySymptoms(e.target.value)}
      />
      <button onClick={addFaulty}>Add Faulty</button>
    </div>
  );
}

export default App;
