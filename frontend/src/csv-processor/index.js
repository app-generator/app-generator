import React, { useState, useEffect } from "react";
import axios from "axios";
import Table from "../components/Table";
import SelectDropdown from "../components/Select";
import InputField from "../components/InputField";
import Papa from "papaparse";
// import "./index.css";

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
  const isPro = window.IS_PRO;
  const csvLimit = window.CSV_PROCESS_LIMIT;

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

      //if (error.status == 404) {
      //  alert(error.response.data.message);
      //} else {
      //  alert(error.response.data.detail);
      //}

      console.error("Error fetching files:", error);
    }
  };

  useEffect(() => {
    fetchCsvFiles();
  }, []);

  const fetchCsvData = async (filePath, callback = () => { }) => {
    try {
      const csv_f_path = `${baseURL}${filePath}`
      console.log( '> Processed CSV: ' + csv_f_path )
      const response = await axios.get( csv_f_path );
      Papa.parse(response.data, {
        complete: (result) => {
          const fileData = {
            name: filePath.split("/").pop(),
            data: result.data,
          };
          if (!isPro && fileData.data.length > csvLimit) {
            fileData.data = fileData.data.slice(0, csvLimit);
          }
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

  const handleDownload = (fileData) => {
    if (fileData) {
      const filteredData = fileData.data.filter(row =>
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

  const handleFileDelete = async (filePath) => {
    if (!filePath) {
      alert("No file selected for deletion.");
      return;
    }

    try {
      const response = await axios.delete(`${baseURL}/upload-get-csv/`, {
        data: { file_path: filePath },
      });

      fetchCsvFiles();
      setSelectedFilePath("");
      setSelectedFile(null);
    } catch (error) {
      console.error("Error deleting file:", error);
      alert(error.response?.data?.detail || "Error occurred while deleting the file");
    }
  };


  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="w-full">
        <div className="mb-6">
          <h1 className="mb-3 text-3xl font-semibold text-center">
            CSV Processor
          </h1>
          {!isPro &&
            <p className="text-center">Limited to {csvLimit} lines for Basic Accounts - <a href="/terms/" target="_blank" className="underline font-semibold">Upgrade to PRO</a></p>}
        </div>
        <div className="grid grid-cols-1 gap-6">

          {/* Source csv */}
          <div className="py-6 px-3 bg-white rounded-lg shadow-md">
            <div className="flex items-center gap-3 mb-5">
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
                className="border-gray-300 rounded-md min-w-32"
              />
              {showProcessFile && (
                <div className="upload-link">
                  <label className="underline text-blue-500 cursor-pointer" htmlFor="file-upload">
                    Upload CSV
                  </label>
                  <input
                    type="file"
                    id="file-upload"
                    accept=".csv"
                    onChange={handleFileUpload}
                    className="hidden"
                  />
                </div>
              )}
            </div>

            <div className="grid grid-cols-1 gap-4">
              {selectedFile && (
                <div className="border-t border-gray-300 pt-5">
                  <div className="flex items-center justify-end gap-3 mb-5">
                    <button
                      onClick={() => handleDownload(selectedFile)}
                      className="px-6 py-2 text-white bg-blue-500 rounded hover:bg-blue-600"
                    >
                      Download
                    </button>
                    <button
                      onClick={() => handleFileDelete(selectedFilePath)}
                      className="px-6 py-2 text-white bg-red-500 rounded hover:bg-red-600"
                    >
                      Delete
                    </button>
                  </div>
                  <Table
                    headers={Object.keys(selectedFile.data[0])}
                    data={selectedFile.data}
                    limit={15}
                    editable={true}
                    setChanges={setChanges}
                    setAction={setAction}
                  />

                  {/* Submit Button */}
                  <div className="flex justify-center mt-10">
                    <button onClick={handleSubmit} className="px-6 py-2 text-white bg-blue-500 rounded hover:bg-blue-600">
                      Submit
                    </button>
                  </div>
                </div>
              )}
            </div>
          </div>

          {/* Processed csv */}
          {newFileData && (
            <div className="py-6 px-3 bg-white rounded-lg shadow-md">
              <div>
                <div className="flex items-center justify-between gap-3 mb-5">
                  <div>
                    {!isPro &&
                      <p className="text-center">Output file truncated - <a href="/terms/" target="_blank" className="underline font-semibold">Upgrade to PRO</a></p>}
                  </div>
                  <button onClick={() => handleDownload(newFileData)} className="px-6 py-2 text-white bg-blue-500 rounded hover:bg-blue-600">
                    Download
                  </button>
                </div>
                <Table
                  headers={Object.keys(newFileData.data[0])}
                  data={newFileData.data}
                  limit={15}
                />
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default CsvUploader;
