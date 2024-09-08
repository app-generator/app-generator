import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import DBEditor from "./DBEditor";

export default function App() {
    return (
        <Router>
            <Routes>
                <Route path='/db-editor' element={<DBEditor />} />
            </Routes>
        </Router>
    )
}

const root = ReactDOM.createRoot(document.getElementById('app'));
root.render(<App />);