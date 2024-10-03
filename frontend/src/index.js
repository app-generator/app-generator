import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import DBEditor from "./db-editor";
import DjangoGenerator from "./django-generator";
import CSVProcessor from "./csv-processor";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/tools/db-editor" element={<DBEditor />} />
        <Route path="/tools/csv-processor" element={<CSVProcessor />} />
        <Route path="/tools/django-generator" element={<DjangoGenerator />} />
      </Routes>
    </Router>
  );
}

const root = ReactDOM.createRoot(document.getElementById("app"));
root.render(<App />);
0