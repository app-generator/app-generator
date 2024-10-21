import React, { useState, useEffect } from "react";
import axios from "axios";
import Table from "../components/Table";
import SelectDropdown from "../components/Select";
import InputField from "../components/InputField";
import Papa from "papaparse";
import "./index.css";

const CsvUploader = () => {
  const [csvFiles, setCsvFiles] = useState([]);
  const [selectedFile, setSelectedFile] = useState(null);
  const [selectedFilePath, setSelectedFilePath] = useState("");
  const [uploading, setUploading] = useState(false);
  const [changes, setChanges] = useState({});
  const [action, setAction] = useState({});
  const [newFilePath, setNewFilePath] = useState("");
  const [newFileData, setNewFileData] = useState(null);
  const [showProcessFile, setShowProcessFile] = useState(true);

  const baseURL = window.location.origin;

  const fetchCsvFiles = async () => {
    try {
      const response = await axios.get(`${baseURL}/upload-get-csv/`);
      if (response && response.data.files) {
        setCsvFiles(
          response.data.files.map((filePath) => ({
            label: filePath.split("/").pop(),
            value: filePath,
          }))
        );
      }
    } catch (error) {
      if (error.status == 404) {
        alert(error.response.data.message);
      } else {
        alert(error.response.data.detail);
      }

      console.error("Error fetching files:", error);
    }
  };

  useEffect(() => {
    fetchCsvFiles();
  }, []);

  const fetchCsvData = async (filePath, callback = () => { }) => {
    try {
      const response = await axios.get(`${baseURL}${filePath}`);
      Papa.parse(response.data, {
        complete: (result) => {
          const fileData = {
            name: filePath.split("/").pop(),
            data: result.data,
          };
          callback(fileData);
        },
        header: true,
      });
    } catch (error) {
      console.error("Error fetching CSV data:", error);
    }
  };

  const handleFileSelect = (e) => {
    const filePath = e.target.value;

    if (filePath === "show-process-file") {
      setShowProcessFile(true);
      setSelectedFile(null);
      setSelectedFilePath("");
      setNewFileData(null);
      return;
    }

    setSelectedFilePath(filePath);
    setNewFileData(null);
    setChanges({});
    setAction({});
    setShowProcessFile(false);
    fetchCsvData(filePath, setSelectedFile);
  };

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    if (file) {
      setUploading(true);

      const formData = new FormData();
      formData.append("file", file);

      try {
        const response = await axios.post(
          `${baseURL}/upload-get-csv/`,
          formData
        );
        setUploading(false);

        fetchCsvFiles();

        const uploadedFilePath = response.data.file_path;
        setSelectedFilePath(uploadedFilePath);
        fetchCsvData(uploadedFilePath, setSelectedFile);
        setShowProcessFile(false);
      } catch (error) {
        console.error("Error uploading file:", error);
        alert(error.response.data.detail);
        setUploading(false);
      }
    }
  };

  const handleSubmit = async () => {
    const fields = {};
    Object.keys(selectedFile.data[0]).forEach((column) => {
      const newName = changes[column] || "";
      const transformer = action[column] || "";

      if (newName || transformer) {
        fields[column] = {
          new_name: newName,
          transformer: transformer,
        };
      }
    });

    const payload = {
      file: selectedFilePath,
      fields: fields,
    };

    try {
      const response = await axios.post(`${baseURL}/csv_processor/`, payload, {
        headers: {
          "Content-Type": "application/json",
        },
      });
      const filePath = response.data.file_path;
      setNewFilePath(filePath);

      fetchCsvData(filePath, setNewFileData);
    } catch (error) {
      console.error("Error submitting the data:", error);
    }
  };

  const handleDownload = () => {
    if (newFileData) {
      const filteredData = newFileData.data.filter(row =>
        Object.values(row).some(value => value !== null && value !== "")
      );

      const csv = Papa.unparse(filteredData);
      const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
      const link = document.createElement('a');

      const originalFileName = selectedFilePath.split("/").pop();
      link.href = URL.createObjectURL(blob);
      link.setAttribute('download', originalFileName);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }
  };


  return (
    <div className="container">
      <div className="header">
        <div className="dropdown">
          {" "}
          <SelectDropdown
            options={[
              !showProcessFile && {
                value: "show-process-file",
                label: "Show Process File",
              },
              ...csvFiles,
            ].filter(Boolean)}
            value={selectedFilePath}
            onChange={handleFileSelect}
          />
          {showProcessFile && (
            <div className="upload-link">
              <span>Process</span>
              <label className="upload-label" htmlFor="file-upload">
                Upload CSV
              </label>
              <input
                type="file"
                id="file-upload"
                accept=".csv"
                onChange={handleFileUpload}
                className="hidden-input"
              />
            </div>
          )}
        </div>
      </div>

      {/* CSV File Display Section */}
      {selectedFile && (
        <>
          <h3>CSV File</h3>
          <Table
            headers={Object.keys(selectedFile.data[0])}
            data={selectedFile.data}
            limit={15}
            editable={true}
            setChanges={setChanges}
            setAction={setAction}
          />

          {/* Submit Button */}
          <div className="submit-section">
            <button onClick={handleSubmit} className="submit-button">
              Submit
            </button>
          </div>
        </>
      )}

      {/* New File Data Display Section */}
      {newFileData && (
        <div >
          <button onClick={handleDownload} className="download-button">
            Download Processed File
          </button>
          <Table
            headers={Object.keys(newFileData.data[0])}
            data={newFileData.data}
            limit={15}
          />
        </div>
      )}
    </div>
  );
};

export default CsvUploader;
