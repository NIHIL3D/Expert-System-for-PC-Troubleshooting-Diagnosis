// import React, { useState } from 'react';

// function App() {
//   const [question, setQuestion] = useState("");
//   const [diagnosis, setDiagnosis] = useState("");

//   const startDiagnosis = async () => {
//     setDiagnosis('');
//     try {
//       const response = await fetch('/start');
//       if (!response.ok) {
//         throw new Error('Failed to start diagnosis.');
//       }
//       // setQuestion("Diagnosis started. Please answer the questions.");
//       const data = await response.json();
//       if (data.question) {
//         setQuestion(data.question);}
//       console.log(response);
//     } catch (error) {
//       console.error('Error:', error);
//       setQuestion("Failed to start diagnosis.");
//     }
//   };

//   const answerQuestion = async (ans) => {
//     try {
//       const response = await fetch(`/answer/${ans}`);
//       if (!response.ok) {
//         throw new Error('Failed to get response from server.');
//       }
//       const data = await response.json();
//       if (data.diagnosis) {
//         setDiagnosis(data.diagnosis);
//         setQuestion('');
//       } else if (data.question) {
//         setQuestion(data.question);
//       } else {
//         throw new Error('Invalid response from server.');
//       }
//     } catch (error) {
//       console.error('Error:', error);
//       setQuestion("Failed to get response from server.");
//     }
//   };

//   return (
//     <div>
//       <h1>Computer Diagnostic Expert System</h1>
//       <button onClick={startDiagnosis}>Start Diagnosis</button>
//       <p>{question}</p>
//       <p>{diagnosis}</p>
//       {!diagnosis && 
//       <div>
//       <button onClick={() => answerQuestion('yes')}>Yes</button>
//       <button onClick={() => answerQuestion('no')}>No</button>
//       </div>
//       }
//     </div>
//   );
// }

// export default App;

import React, { useState } from 'react';

function App() {
  const [selectedProblems, setSelectedProblems] = useState([]);
  const [diagnosis, setDiagnosis] = useState('');

  const symptomsList = [
    "blank_screen",
    "artifacting_on_screen",
    "flickering_display",
    "no_sound",
    "loud_fan_noise",
    "computer_overheating",
    "random_shutdowns",
    "slow_performance",
    "high_CPU_usage",
    "computer_not_booting_to_OS",
    "USB_device_not_recognized",
    "blue_screen_of_death",
    "network_connection_issues",
    "unresponsive_keyboard",
    "loud_hard_drive_noise",
    "spontaneous_rebooting",
    "computer_won't_power_on",
    "printer_not_printing",
    "malware_infection",
    "blocked_airflow",
    "improper_drive_installation"
  ];

  const handleCheckboxChange = (event) => {
    const problem = event.target.value;
    if (event.target.checked) {
      setSelectedProblems([...selectedProblems, problem]);
    } else {
      setSelectedProblems(selectedProblems.filter((p) => p !== problem));
    }
  };

  const handleDiagnose = async () => {
    try {
      const response = await fetch('/diagnose', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ symptoms: selectedProblems })
      });

      const data = await response.json();
      setDiagnosis(data.diagnosis.join(', '));
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h2>Select the problems you are experiencing:</h2>
      <form>
        {symptomsList.map(symptom => (
          <div key={symptom}>
            <label>
              <input
                type="checkbox"
                value={symptom}
                onChange={handleCheckboxChange}
              />
              {symptom.replace(/_/g, ' ')}
            </label>
          </div>
        ))}
      </form>
      <button onClick={handleDiagnose}>Diagnose</button>
      {diagnosis && <p>Diagnosis: {diagnosis}</p>}
    </div>
  );
}

export default App;
