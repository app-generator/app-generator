import React, { useState, useEffect, useMemo, useCallback } from "react";
import Papa from "papaparse";
import Table from "../components/Table";
import ComboBox from "../components/ComboBox";
import "./index.css";
import { getLocalStorageItem } from "./utils";
import axios from "axios";

const CSVProcessor = () => {
  const [csvFiles, setCsvFiles] = useState(() =>
    getLocalStorageItem("csvFiles", [
      {
        name: "CSV File 1",
        content: [
          {
            PassengerID: "12",
            ServiceID: "001",
            Name: "John Bradley",
            Sex: "Male",
            Age: "50",
          },
        ],
      },
      {
        name: "CSV File 2",
        content: [
          {
            PassengerID: "13",
            ServiceID: "003",
            Name: "Emily Clark",
            Sex: "Female",
            Age: "45",
          },
        ],
      },
    ])
  );

  const [selectedFile, setSelectedFile] = useState(() =>
    getLocalStorageItem("selectedFile", null)
  );
  const [columnChanges, setColumnChanges] = useState(() =>
    getLocalStorageItem("columnChanges", {})
  );
  const [columnActions, setColumnActions] = useState(() =>
    getLocalStorageItem("columnActions", {})
  );
  const [uploadedRawFile, setUploadedRawFile] = useState(null);

  useEffect(() => {
    const updateLocalStorage = () => {
      localStorage.setItem("csvFiles", JSON.stringify(csvFiles));
      localStorage.setItem("selectedFile", JSON.stringify(selectedFile));
      localStorage.setItem("columnChanges", JSON.stringify(columnChanges));
      localStorage.setItem("columnActions", JSON.stringify(columnActions));
    };
    const debounceUpdate = setTimeout(updateLocalStorage, 300);
    return () => clearTimeout(debounceUpdate);
  }, [csvFiles, selectedFile, columnChanges, columnActions]);

  const initializeColumnData = useCallback((fileContent) => {
    const initialData = fileContent[0]
      ? Object.keys(fileContent[0]).reduce(
          (acc, column) => ({ ...acc, [column]: "" }),
          {}
        )
      : {};
    setColumnChanges(initialData);
    setColumnActions(initialData);
  }, []);

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      setUploadedRawFile(file);
      Papa.parse(file, {
        header: true,
        complete: (result) => {
          const newCsvFile = { name: file.name, content: result.data };
          setCsvFiles((prevFiles) => [...prevFiles, newCsvFile]);
          setSelectedFile(newCsvFile);
          initializeColumnData(result.data);
        },
        error: (error) => console.error("Error parsing CSV file:", error),
      });
    }
  };

  const handleFileSelection = (event) => {
    const selectedFileName = event.target.value;
    const selectedCsv = csvFiles.find((file) => file.name === selectedFileName);
    setSelectedFile(selectedCsv);
    const csvContent = selectedCsv.content
      .map((row) => Object.values(row).join(","))
      .join("\n");

    const blob = new Blob([csvContent], { type: "text/csv" });
    const file = new File([blob], selectedCsv.name, { type: "text/csv" });

    setUploadedRawFile(file);
    initializeColumnData(selectedCsv.content);
  };

  const handleColumnChange = useCallback((column, newValue) => {
    setColumnChanges((prevChanges) => ({ ...prevChanges, [column]: newValue }));
  }, []);

  const handleActionChange = useCallback((column, actionValue) => {
    setColumnActions((prevActions) => ({
      ...prevActions,
      [column]: actionValue,
    }));
  }, []);

  const handleSubmit = async () => {
    if (!uploadedRawFile) {
      return;
    }

    const baseUrl = `${window.location.origin}/upload-csv/`;
    try {
      const formData = new FormData();
      formData.append("file", uploadedRawFile);
      //  formData.append("columnChanges", JSON.stringify(columnChanges));
      //  formData.append("columnActions", JSON.stringify(columnActions));
      const response = await axios.post(baseUrl, formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      console.log("API response:", response.data);
    } catch (error) {
      console.error("Error uploading CSV file:", error);
    }
  };

  const tableHeaders = useMemo(
    () => (selectedFile ? Object.keys(selectedFile.content[0]) : []),
    [selectedFile]
  );

  return (
    <div>
      <div className="header">
        <ComboBox
          csvFiles={csvFiles}
          handleFileSelection={handleFileSelection}
          selectedFile={selectedFile}
        />

        <div className="inputWrapper">
          <h2>Process</h2>
          <label htmlFor="csvUpload">Upload CSV</label>
          <input
            type="file"
            id="csvUpload"
            accept=".csv"
            onChange={handleFileUpload}
            style={{ display: "none" }}
          />
        </div>
      </div>

      {selectedFile && (
        <>
          <Table
            headers={tableHeaders}
            data={selectedFile.content}
            columnChanges={columnChanges}
            columnActions={columnActions}
            handleColumnChange={handleColumnChange}
            handleActionChange={handleActionChange}
          />

          <div className="btnWrapper">
            <button onClick={handleSubmit}>Submit</button>
          </div>
        </>
      )}
    </div>
  );
};

export default CSVProcessor;
