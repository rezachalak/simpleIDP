import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Clouds from './components/Clouds';
import Clusters from './components/Clusters';
import Projects from './components/Projects';

const App: React.FC = () => {
    return (
        <Router>
            <div>
                <Navbar />
                <Routes> // Changed Switch to Routes
                    <Route path="/clouds" element={<Clouds />} />
                    <Route path="/clusters" element={<Clusters />} />
                    <Route path="/projects" element={<Projects />} />
                </Routes> // Changed Switch to Routes
            </div>
        </Router>
    );
};

export default App;
