// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './pages/Home';
import ClientPage from './pages/ClientPage';
import ExpertLoginPage from './pages/ExpertLoginPage';
import ExpertAddProblemPage from './pages/ExpertAddProblemPage';

function App() {
return (
<Router>
    <div className="App">
    <h1 className="Title">PC Troubleshooting Diagnosis</h1>
    <hr />
    <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/client" component={ClientPage} />
        <Route path="/expert/login" component={ExpertLoginPage} />
        <Route path="/expert/add-problem" component={ExpertAddProblemPage} />
    </Switch>
    </div>
</Router>
);
}

export default App;
