import React, { useState, useEffect } from 'react';

function ClientPage() {
const [symptoms, setSymptoms] = useState([]);
const [selectedSymptoms, setSelectedSymptoms] = useState([]);
const [diagnosedIssues, setDiagnosedIssues] = useState([]);
const [diagnoseMessage, setDiagnoseMessage] = useState('');

useEffect(() => {
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
    if (data.faulty_issues.length === 0) {
        setDiagnoseMessage('The symptoms you entered are not enough.');
        setDiagnosedIssues([]);
    } else {
        setDiagnosedIssues(data.faulty_issues);
        setDiagnoseMessage('');
    }
    })
    .catch(error => {
    console.error('Error diagnosing issues:', error);
    });
};

return (
<div className="container client-container">
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
    <button onClick={diagnoseIssues} className="btn">Diagnose Issues</button>
    {diagnoseMessage && <p>{diagnoseMessage}</p>}
    {diagnosedIssues.length > 0 && 
    <div>
        <h2>Diagnosed Issues</h2>
        <ul>
        {diagnosedIssues.map((issue, index) => (
            <li key={index}>{issue}</li>
        ))}
        </ul>
    </div>
    }
</div>
);
}

export default ClientPage;
