import React, { useState, useRef } from "react";
import { FaCheckCircle, FaTimesCircle, FaSpinner } from "react-icons/fa";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import CustomSelect from "../django-generator/custom_select";

const dbDriverOptions = [
  { value: "postgresql", label: "PostgreSQL" },
  { value: "mysql", label: "MySQL" },
  { value: "sqlite", label: "SQLite" },
];

const dbModeOptions = [
  { value: "existing_db", label: "Existing Database" },
  { value: "new_db", label: "New Database" }
]

const baseURL = window.location.origin;

const DBMigrator = () => {
  const fileInputRef = useRef(null);
  const targetFileInputRef = useRef(null);

  const customStyles = {
    control: (provided, state) => ({
      ...provided,
      minHeight: "30px",
      height: "42px",
      boxShadow: state.isFocused ? null : null,
    }),
  };
  const [isLoading, setIsLoading] = useState(false);
  const [sourceDB, setSourceDB] = useState({
    driver: "postgresql",
    file: "",
    name: "",
    user: "",
    pass: "",
    host: "localhost",
    port: 5432,
    connection: null,
  });

  const [targetDB, setTargetDB] = useState({
    driver: "postgresql",
    name: "",
    user: "",
    pass: "",
    host: "localhost",
    port: 5432,
    connection: null,
  });
  const [uploadedFileName, setUploadedFileName] = useState("");
  const [uploadedTargetFileName, setUploadedTargetFileName] = useState("");
  const [result, setResult] = useState({});
  const [dbMode, setDbMode] = useState("");

  const handleDBChange = (option, setDataBase) => {
    setDataBase((prev) => ({
      ...prev,
      driver: option ? option.value : "",
    }));
  };

  const handleModeChange = (option) => {
    setDbMode(option.value)
  }

  const handleDBFieldChange = (e, setDataBase) => {
    const { name, value } = e.target;
    setDataBase((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleFileButtonClick = () => {
    fileInputRef.current.click();
  };

  const handleTargetFileButtonClick = () => {
    targetFileInputRef.current.click();
  };


  const handleFileChange = (event, setStateCallback, setFileNameCallback) => {
    const file = event.target.files[0];
    if (!file) return;

    // Check if the file is a JSON file
    if (file.type !== "application/json") {
      toast.error("Please upload a valid JSON file.");
      return;
    }

    const reader = new FileReader();

    reader.onload = (e) => {
      try {
        const jsonData = JSON.parse(e.target.result);
        console.log(jsonData);

        // Optionally update state with JSON data
        setStateCallback((prev) => ({
          ...prev,
          file: jsonData,
        }));
      } catch (error) {
        console.error("Error parsing JSON:", error);
        toast.error("The file could not be parsed as JSON.");
      }
    };

    reader.onerror = () => {
      console.error("Error reading file.");
      toast.error("There was an error reading the file.");
    };

    reader.readAsText(file); // Read the file as text for JSON parsing
    setFileNameCallback(file.name);
  };

  // Usage for source file
  const handleSourceFileChange = (event) => {
    handleFileChange(event, setSourceDB, setUploadedFileName);
  };

  // Usage for target file
  const handleTargetFileChange = (event) => {
    handleFileChange(event, setSourceDB, setUploadedTargetFileName);
  };


  const handleDBCheck = async (db, setDatabase) => {
    try {
      setIsLoading(true);
      const response = await fetch(
        `${baseURL}/tools/db-migrator/checkconnect`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(db),
        }
      );

      if (!response.ok) {
        throw new Error("Failed to generate");
      }
      const data = await response.json();
      console.log(data);
      // setResult(data)
      if (data.status == 200) {
        setDatabase((prev) => ({
          ...prev,
          connection: true,
        }));
      } else {
        setDatabase((prev) => ({
          ...prev,
          connection: false,
        }));
      }
    } catch (error) {
      setDatabase((prev) => ({
        ...prev,
        connection: false,
      }));
      console.error("Error generating:", error);
      toast.error(
        <>
          Status: Error <br />
          Info: {error.message}
        </>
      );
    } finally {
      setIsLoading(false);
    }
  };

  const handleMigrate = async (e) => {
    e.preventDefault();
    try {
      const payload = {
        sourceDB,
        targetDB,
      };
      const response = await fetch(`${baseURL}/tools/db-migrator/db-migrate`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        throw new Error("Failed to generate");
      }
      const data = await response.json();
      console.log(data);
      setResult(data);
    } catch (error) {
      console.error("Error generating:", error);
      toast.error(
        <>
          Status: Error <br />
          Info: {error.message}
        </>
      );
    }
  };

  return (
    <div className="min-h-screen p-6 bg-gray-100">
      <ToastContainer />
      <h1 className="mb-6 text-3xl font-semibold text-center">
        DataBase Migrator
      </h1>
      <div className="grid grid-cols-1 gap-6 sm:grid-cols-2">
        <div className="flex flex-col h-full">
          <h3 className="mb-3 text-lg font-semibold text-center">Source DB</h3>
          <div className="h-full p-6 bg-white rounded-lg shadow-md">
            <div className="flex flex-col justify-between w-full h-full gap-4">
              {sourceDB.driver === "sqlite" ? (
                <div className="flex flex-col gap-4">
                  <div className="flex gap-4">
                    <div className="flex flex-col w-full gap-2">
                      <label className="block text-gray-700">DB Driver</label>
                      <CustomSelect
                        options={dbDriverOptions}
                        value={dbDriverOptions.find(
                          (option) => option.value === sourceDB.driver
                        )}
                        onChange={(e) => handleDBChange(e, setSourceDB)}
                        placeholder="Select Database Driver"
                        isClearable
                        styles={customStyles}
                      />
                    </div>

                    <div className="flex items-end justify-start w-full">
                      <button type="button" className="w-full p-2 border border-gray-300 rounded" onClick={handleFileButtonClick}>
                        Upload File
                      </button>
                      <input
                        type="file"
                        ref={fileInputRef}
                        onChange={handleSourceFileChange}
                        accept="application/json"
                        className="hidden"
                      />
                    </div>
                  </div>
                  {uploadedFileName && (
                    <div className="mt-2 text-gray-700">
                      Uploaded File: {uploadedFileName}
                    </div>
                  )}
                </div>
              ) : (
                <div className="flex flex-col w-full gap-4">
                  <div className="flex w-full gap-4">
                    <div className="flex flex-col w-full gap-2">
                      <label className="block text-gray-700">DB Driver</label>
                      <CustomSelect
                        options={dbDriverOptions}
                        value={dbDriverOptions.find(
                          (option) => option.value === sourceDB.driver
                        )}
                        onChange={(e) => handleDBChange(e, setSourceDB)}
                        placeholder="Select Database Driver"
                        isClearable
                        styles={customStyles}
                      />
                    </div>
                    <div className="flex flex-col w-full gap-2">
                      <label className="block text-gray-700">Name</label>
                      <input
                        type="text"
                        name="name"
                        value={sourceDB.name}
                        onChange={(e) => handleDBFieldChange(e, setSourceDB)}
                        className="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                        placeholder="Database Name"
                        required
                      />
                    </div>
                  </div>
                  <div className="grid grid-cols-2 gap-4">
                    <div className="flex flex-col w-full gap-2">
                      <label className="block text-gray-700">User</label>
                      <input
                        type="text"
                        name="user"
                        value={sourceDB.user}
                        onChange={(e) => handleDBFieldChange(e, setSourceDB)}
                        className="w-full p-2 mt-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                        placeholder="Database userName"
                      />
                    </div>
                    <div className="flex flex-col w-full gap-2">
                      <label className="block text-gray-700">Password</label>
                      <input
                        type="password"
                        name="pass"
                        value={sourceDB.pass}
                        onChange={(e) => handleDBFieldChange(e, setSourceDB)}
                        className="w-full p-2 mt-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                        placeholder="Database Password"
                      />
                    </div>
                    <div className="flex flex-col w-full gap-2">
                      <label className="block text-gray-700">Host</label>
                      <input
                        type="text"
                        name="host"
                        value={sourceDB.host || "localhost"}
                        onChange={(e) => handleDBFieldChange(e, setSourceDB)}
                        className="w-full p-2 mt-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                        placeholder="Database Host"
                      />
                    </div>
                    <div className="flex flex-col w-full gap-2">
                      <label className="block text-gray-700">Port</label>
                      <input
                        type="number"
                        name="port"
                        value={
                          sourceDB.port ||
                          (sourceDB.driver === "mysql"
                            ? 3306
                            : sourceDB.driver === "postgresql"
                              ? 5432
                              : "")
                        }
                        onChange={(e) => handleDBFieldChange(e, setSourceDB)}
                        className="w-full p-2 mt-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                        placeholder="Database Port"
                      />
                    </div>
                  </div>
                </div>
              )}
              <div className="flex items-center justify-center gap-4">
                <button
                  onClick={() => handleDBCheck(sourceDB, setSourceDB)}
                  disabled={isLoading}
                  className={`flex items-center px-6 py-2 text-black bg-white border border-black rounded transition-transform duration-150 ease-in-out transform
    hover:scale-105 active:scale-95 focus:outline-none
    ${isLoading ? "opacity-50 cursor-not-allowed" : ""}`}
                >
                  {isLoading ? "Checking..." : "Check Connection"}
                </button>
                {sourceDB.connection === true && (
                  <FaCheckCircle
                    className="w-6 h-6 text-green-500"
                    title="Connection Successful"
                  />
                )}
                {sourceDB.connection === false && (
                  <FaTimesCircle
                    className="w-6 h-6 text-red-500"
                    title="Connection Failed"
                  />
                )}
              </div>
            </div>
          </div>
        </div>
        <div className="flex flex-col h-full">
          <h3 className="mb-3 text-lg font-semibold text-center">
            Destination DB
          </h3>
          <div className="p-6 bg-white rounded-lg shadow-md">
            {/* <h2 className="mb-4 text-xl font-bold">Database Settings</h2> */}
            <div className="flex flex-col w-full gap-4">
              <div className="flex gap-4">
                <div className="flex flex-col w-full gap-2">
                  <label className="block text-gray-700">DB Driver</label>
                  <CustomSelect
                    options={dbDriverOptions}
                    value={dbDriverOptions.find(
                      (option) => option.value === targetDB.driver
                    )}
                    onChange={(e) => handleDBChange(e, setTargetDB)}
                    placeholder="Select Database Driver"
                    isClearable
                    styles={customStyles}
                  />
                </div>

                <div className="flex flex-col w-full gap-2">
                  <label className="block text-gray-700">Database Mode</label>
                  <CustomSelect
                    options={dbModeOptions}
                    value={dbModeOptions.find(
                      (option) => option.value === dbMode
                    )}
                    onChange={(e) => handleModeChange(e)}
                    placeholder="Select Database Mode"
                    isClearable
                    styles={customStyles}
                  />
                </div>
              </div>
              {(dbMode == 'new_db') &&
                <div className="grid grid-cols-2 gap-4">
                  <div className="flex flex-col w-full gap-2">
                    <label className="block text-gray-700">Name</label>
                    <input
                      type="text"
                      name="name"
                      value={targetDB.name}
                      onChange={(e) => handleDBFieldChange(e, setTargetDB)}
                      className="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                      placeholder="Database Name"
                      required
                    />
                  </div>
                </div>}
              {(dbMode == 'existing_db') && <>
                <div className="flex items-end justify-start w-full p-2">
                  <button type="button" className="w-full p-2 border border-gray-300 rounded" onClick={handleTargetFileButtonClick}>
                    Upload File
                  </button>
                  <input
                    type="file"
                    ref={targetFileInputRef}
                    onChange={handleTargetFileChange}
                    accept="application/json"
                    className="hidden"
                  />
                </div>
                {uploadedTargetFileName && (
                  <div className="mt-2 text-gray-700">
                    Uploaded File: {uploadedTargetFileName}
                  </div>
                )}
              </>}
              {(targetDB.driver !== "sqlite" && dbMode == "new_db") && (
                <div className="grid grid-cols-2 gap-4">
                  <div className="flex flex-col w-full gap-2">
                    <label className="block text-gray-700">User</label>
                    <input
                      type="text"
                      name="user"
                      value={targetDB.user}
                      onChange={(e) => handleDBFieldChange(e, setTargetDB)}
                      className="w-full p-2 mt-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                      placeholder="Database userName"
                    />
                  </div>
                  <div className="flex flex-col w-full gap-2">
                    <label className="block text-gray-700">Password</label>
                    <input
                      type="password"
                      name="pass"
                      value={targetDB.pass}
                      onChange={(e) => handleDBFieldChange(e, setTargetDB)}
                      className="w-full p-2 mt-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                      placeholder="Database Password"
                    />
                  </div>
                  <div className="flex flex-col w-full gap-2">
                    <label className="block text-gray-700">Host</label>
                    <input
                      type="text"
                      name="host"
                      value={targetDB.host || "localhost"}
                      onChange={(e) => handleDBFieldChange(e, setTargetDB)}
                      className="w-full p-2 mt-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                      placeholder="Database Host"
                    />
                  </div>
                  <div className="flex flex-col w-full gap-2">
                    <label className="block text-gray-700">Port</label>
                    <input
                      type="number"
                      name="port"
                      value={
                        targetDB.port ||
                        (targetDB.driver === "mysql"
                          ? 3306
                          : targetDB.driver === "postgresql"
                            ? 5432
                            : "")
                      }
                      onChange={(e) => handleDBFieldChange(e, setTargetDB)}
                      className="w-full p-2 mt-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                      placeholder="Database Port"
                    />
                  </div>
                </div>
              )}
              <div className="flex items-center justify-center gap-4">
                <button
                  onClick={() => handleDBCheck(targetDB, setTargetDB)}
                  disabled={isLoading}
                  className={`flex items-center px-6 py-2 text-black bg-white border border-black rounded transition-transform duration-150 ease-in-out transform
                  hover:scale-105 active:scale-95 focus:outline-none
                  ${isLoading ? "opacity-50 cursor-not-allowed" : ""}`}
                >
                  {isLoading ? "Checking..." : "Check Connection"}
                </button>
                {targetDB.connection === true && (
                  <FaCheckCircle
                    className="w-6 h-6 text-green-500"
                    title="Connection Successful"
                  />
                )}
                {targetDB.connection === false && (
                  <FaTimesCircle
                    className="w-6 h-6 text-red-500"
                    title="Connection Failed"
                  />
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
      <div>
        <div className="flex items-center justify-center">
          <button
            type="submit"
            className="px-6 py-3 mt-6 text-white transition-colors duration-300 bg-gray-800 rounded-lg hover:bg-gray-700"
            onClick={handleMigrate}
          >
            Migrate Data
          </button>
        </div>
      </div>
      <div className="p-4 mt-6 bg-white rounded-lg shadow-md">
        <h2 className="mb-4 text-lg font-semibold">Output from the tool</h2>
        <pre className="p-2 bg-gray-100 rounded">
          {result && Object.keys(result).length > 0
            ? JSON.stringify(result, null, 2)
            : "No data available"}
        </pre>
      </div>
    </div>
  );
};

export default DBMigrator;
