import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import DBProcessor from "./db-processor";
import DBMigrator from "./db-migrator";
import DjangoGenerator from "./django-generator";
import CSVProcessor from "./csv-processor";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/tools/db-processor" element={<DBProcessor />} />
        <Route path="/tools/db-migrator" element={<DBMigrator />} />
        <Route path="/tools/csv-processor" element={<CSVProcessor />} />
        <Route path="/tools/django-generator" element={<DjangoGenerator />} />
      </Routes>
    </Router>
  );
}

const root = ReactDOM.createRoot(document.getElementById("app"));
root.render(<App />);
0