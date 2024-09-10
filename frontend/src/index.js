import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import DBEditor from "./db-editor";

export default function App() {
    return (
        <Router>
            <Routes>
                <Route path='/tools/db-editor' element={<DBEditor />} />
            </Routes>
        </Router>
    )
}

const root = ReactDOM.createRoot(document.getElementById('app'));
root.render(<App />);