import React, { useState, useEffect } from 'react';

function ExpertAddProblemPage() {
  const [problemName, setProblemName] = useState('');
  const [associatedSymptoms, setAssociatedSymptoms] = useState('');
  const [expertEmail, setExpertEmail] = useState('');

  useEffect(() => {
    fetch('/api/expert/email')
      .then(response => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error('Expert not logged in');
        }
      })
      .then(data => {
        setExpertEmail(data.expert_email);
      })
      .catch(error => {
        console.error('Error getting expert email:', error);
      });
  }, []);

  const handleAddProblem = () => {
    fetch('/api/add-symptom', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ issue: problemName, symptom: associatedSymptoms })
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
    <div className="container add-problem-container">
      <h1>Add a faulty with symptoms</h1>
      {expertEmail && <p>Logged in as : {expertEmail}</p>}
      <input type="text" placeholder="Faulty" value={problemName} onChange={(e) => setProblemName(e.target.value)} />
      <input type="text" placeholder="Related symptoms (comma separated: symp1, symp2, ...etc)" value={associatedSymptoms} onChange={(e) => setAssociatedSymptoms(e.target.value)} />
      <button onClick={handleAddProblem} className="btn">Add</button>
    </div>
  );
}

export default ExpertAddProblemPage;
