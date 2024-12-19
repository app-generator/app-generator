import React, { useState, useEffect } from "react";
import Select from "react-select";
import { ToastContainer, toast } from "react-toastify";
import { Status } from "./StatusModal";
import CustomSelect from './custom_select';
import LoadingOverlay from "../common/loader";

import "react-toastify/dist/ReactToastify.css";
import { useParams } from "react-router-dom";

// Define options for react-select
const dbDriverOptions = [
  { value: "postgresql", label: "PostgreSQL" },
  { value: "mysql", label: "MySQL" },
  { value: "sqlite", label: "SQLite" },
  { value: "mariadb", label: "MariaDB" },
  // Add more as needed
];

const djangoFieldTypeOptions = [
  { value: "CharField", label: "CharField" },
  { value: "TextField", label: "TextField" },
  { value: "BooleanField", label: "BooleanField" },
  { value: "IntegerField", label: "IntegerField" },
  { value: "DateField", label: "DateField" },
  { value: "ForeignKey", label: "ForeignKey" },
  // Add more as needed
];

const baseURL = window.location.origin;

const DjangoGenerator = () => {
  const customStyles = {
    control: (provided, state) => ({
      ...provided,
      minHeight: "30px",
      height: "42px",
      boxShadow: state.isFocused ? null : null,
    }),
  };

  const [formData, setFormData] = useState({
    project_name: "",
    backend: "django",
    frontend: "NA",
    design: "soft",
    db: {
      driver: "sqlite",
      name: "",
      user: "",
      pass: "",
      host: "localhost",
      port: "",
    },
    models: {},
    auth: {
      basic: true,
      github: false,
      google: false,
      otp: false,
    },
    custom_user: {},
    deploy: {
      docker: true,
      ci_cd: true,
      go_live: false,
    },
    tools: {
      celery: false,
      dynamicApiModule: false,
      dynamicDataTables: false,
      reactIntegration: false,
      api_generator: {},
    },
  });

  const [modelName, setModelName] = useState("");
  const [modelFields, setModelFields] = useState([
    { fieldName: "", fieldType: "", relatedModel: "" },
    { fieldName: "", fieldType: "", relatedModel: "" },
  ]);
  const [updatedModelFields, setUpdatedModelFields] = useState([]);
  const [successMessage, setSuccessMessage] = useState("");
  const [successUserMessage, setSuccessUserMessage] = useState("");

  const [designSelection, setDesignSelection] = useState("soft");
  const [authChecked, setAuthChecked] = useState({
    auth: {
      basic: true,
      github: false,
      google: false,
      otp: false,
    },
  });

  const [customFields, setCustomFields] = useState([
    { fieldName: "", fieldType: "" },
    { fieldName: "", fieldType: "" },
  ]);

  const [activeTab, setActiveTab] = useState("create");
  const [loading, setLoading] = useState(false);

  const [openModal, setOpenModal] = useState(false);
  const [status, setStatus] = useState({});
  const [ui, setUI] = useState({});

  const { design } = useParams();

  const handleClose = () => {
    setOpenModal(false);
  };

  // Handle changes for main form inputs
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));

    if (name === 'design') {
      setDesignSelection(e.target.value);
    }
  };

  // Handle changes for Database driver (react-select)
  const handleDBChange = (selectedOption) => {
    setFormData((prev) => ({
      ...prev,
      db: {
        ...prev.db,
        driver: selectedOption ? selectedOption.value : "",
      },
    }));
  };

  // Handle changes for Database fields (Separate Handler)
  const handleDBFieldChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      db: {
        ...prev.db,
        [name]: value,
      },
    }));
  };

  // Handle changes for Authentication checkboxes
  const handleAuthChange = (e) => {
    const { name, checked } = e.target;
    setFormData((prev) => ({
      ...prev,
      auth: {
        ...prev.auth,
        [name]: checked,
      },
    }));
    setAuthChecked((prev) => ({
      ...prev,
      auth: {
        ...prev.auth,
        [name]: checked,
      },
    }));
  };

  // Handle changes for Deployment checkboxes
  const handleDeployChange = (e) => {
    const { name, checked } = e.target;
    setFormData((prev) => ({
      ...prev,
      deploy: {
        ...prev.deploy,
        [name]: checked,
      },
    }));
  };

  // Updated handleToolsChange function
  const handleToolsChange = (e, modelName = null) => {
    const { name, checked } = e.target;

    setFormData((prev) => {
      let updatedTools = { ...prev.tools };

      // Handle dynamicApiModule toggle
      if (name === "dynamicApiModule") {
        // When dynamicApiModule is toggled, update all api_generator_* checkboxes
        const updatedApiGenerators = Object.keys(prev.models).reduce(
          (acc, currentModel) => {
            acc[currentModel] = checked
              ? `home.models.${currentModel}`
              : undefined;
            return acc;
          },
          {}
        );

        updatedTools.dynamicApiModule = checked;
        updatedTools.api_generator = updatedApiGenerators;
      }
      // Handle individual api_generator_* toggle
      else if (name.startsWith("api_generator_") && modelName) {
        // Update the specific api_generator_* checkbox
        const updatedApiGeneratorValue = checked
          ? `home.models.${modelName}`
          : undefined;
        updatedTools.api_generator = {
          ...prev.tools.api_generator,
          [modelName]: updatedApiGeneratorValue,
        };

        // After updating, determine the state of dynamicApiModule
        const apiGeneratorValues = Object.values(updatedTools.api_generator);
        const allChecked = apiGeneratorValues.every(
          (value) => value !== undefined
        );
        const allUnchecked = apiGeneratorValues.every(
          (value) => value === undefined
        );

        if (allChecked) {
          updatedTools.dynamicApiModule = true;
        } else if (allUnchecked) {
          updatedTools.dynamicApiModule = false;
        } else {
          // Optionally handle the indeterminate state here
          // Note: React doesn't support setting the indeterminate property directly via state
          // It requires accessing the DOM element, which is outside the scope of this function
        }
      }
      // Handle other tool checkboxes
      else {
        updatedTools[name] = checked;
      }

      return {
        ...prev,
        tools: updatedTools,
      };
    });
  };

  // Handle Tab changed of tables
  const handleTabChange = (model) => {
    setActiveTab(model);
    const modelData = formData.models[model];
    console.log({ modelData }, Object.entries(modelData));

    // Transform the modelData into modelFields array
    const updatedModelFields = Object.entries(modelData).map(
      ([fieldName, fieldValue]) => {
        if (typeof fieldValue === "object" && fieldValue.type) {
          // Handle ForeignKey fields
          return {
            fieldName: fieldName,
            fieldType: fieldValue.type,
            relatedModel: fieldValue.related_model || "",
          };
        } else {
          // Handle regular fields
          return {
            fieldName: fieldName,
            fieldType: fieldValue,
            relatedModel: "",
          };
        }
      }
    );

    console.log({ updatedModelFields });

    // Update the state with the transformed modelFields
    setUpdatedModelFields(updatedModelFields);
  };

  // Add a new model to formData.models
  const addModel = () => {
    const trimmedModelName = modelName.trim();
    if (trimmedModelName === "") {
      alert("Model name cannot be empty.");
      return;
    }

    // Check for duplicate model names
    if (formData.models.hasOwnProperty(trimmedModelName)) {
      alert(`Model "${trimmedModelName}" already exists.`);
      return;
    }

    // Create new model object
    const newModel = modelFields.reduce((acc, field) => {
      const { fieldName, fieldType, relatedModel } = field;
      if (fieldName.trim() && fieldType.trim()) {
        if (fieldType === "ForeignKey") {
          if (relatedModel.trim() === "") {
            alert(
              `ForeignKey field "${fieldName}" requires a related model name.`
            );
            throw new Error("Related model name is missing.");
          }
          acc[fieldName.trim()] = {
            type: fieldType.trim(),
            related_model: relatedModel.trim(),
          };
        } else {
          acc[fieldName.trim()] = fieldType.trim();
        }
      }
      return acc;
    }, {});

    // If the loop above threw an error due to missing related model, stop execution
    if (!newModel) return;

    if (Object.keys(newModel).length === 0) {
      // No valid fields to add
      alert("Please add at least one valid field.");
      return;
    }

    setFormData((prev) => ({
      ...prev,
      models: {
        ...prev.models,
        [trimmedModelName]: newModel,
      },
    }));

    // Reset the model input fields
    setModelName("");
    setModelFields([
      { fieldName: "", fieldType: "", relatedModel: "" },
      { fieldName: "", fieldType: "", relatedModel: "" },
    ]);

    // Show success message
    setSuccessMessage(`Model "${trimmedModelName}" added successfully!`);
    setTimeout(() => setSuccessMessage(""), 3000); // Clear message after 3 seconds
  };

  // Save a custom User Model to formData.custom_user
  const saveUserModel = () => {
    setFormData((prev) => ({
      ...prev,
      custom_user: customFields,
    }));
    setSuccessUserMessage;
    setSuccessUserMessage(`User Model saved successfully!`);
    setTimeout(() => setSuccessUserMessage(""), 3000); // Clear message after 3 seconds
  };

  //Remove model to formData.models
  const removeModelTab = (modelName) => {
    setFormData((prevFormData) => {
      const { [modelName]: _, ...remainingModels } = prevFormData.models;
      return {
        ...prevFormData,
        models: remainingModels,
      };
    });

    // Update the active tab if necessary
    if (activeTab === modelName) {
      // Set the active tab to "create" or another default value
      setActiveTab("create");
    }

    // Provide user feedback
    setSuccessMessage(`Model "${modelName}" removed successfully!`);
    setTimeout(() => setSuccessMessage(""), 3000); // Clear message after 3 seconds
  };

  // Handle changes in model fields
  const handleModelFieldChange = (
    index,
    field,
    value,
    modelData,
    setModelData
  ) => {
    const updatedFields = [...modelData];
    updatedFields[index][field] = value;
    setModelData(updatedFields);
  };

  // Add a new field to the current model
  const addModelField = () => {
    setModelFields([
      ...modelFields,
      { fieldName: "", fieldType: "", relatedModel: "" },
    ]);
  };

  // Remove a field from the User model
  const removeField = (index, modelData, setModelData) => {
    const updatedFields = modelData.filter((_, i) => i !== index);
    setModelData(updatedFields);
  };

  // Add a new field to the User model
  const addUserModelField = () => {
    setCustomFields([...customFields, { fieldName: "", fieldType: "" }]);
  };

  // Add a new field to the updated model
  const addUpdatedModelField = () => {
    setUpdatedModelFields([
      ...updatedModelFields,
      { fieldName: "", fieldType: "", relatedModel: "" },
    ]);
  };

  // Save changes to the model
  const saveModelChanges = (modelName) => {
    const updatedModel = updatedModelFields.reduce((acc, field) => {
      const { fieldName, fieldType, relatedModel } = field;
      if (fieldName.trim() && fieldType.trim()) {
        if (fieldType === "ForeignKey" && relatedModel.trim() === "") {
          alert(
            `ForeignKey field "${fieldName}" requires a related model name.`
          );
          return acc;
        }
        acc[fieldName.trim()] =
          fieldType === "ForeignKey"
            ? { type: fieldType.trim(), related_model: relatedModel.trim() }
            : fieldType.trim();
      }
      return acc;
    }, {});

    setFormData((prev) => ({
      ...prev,
      models: {
        ...prev.models,
        [modelName]: updatedModel,
      },
    }));

    setSuccessMessage(`Changes to "${modelName}" saved successfully!`);
    setTimeout(() => setSuccessMessage(""), 3000);
  };

  const handleGenerate = async (e) => {
    e.preventDefault();
    console.log(JSON.stringify(formData, null, 2));
    setLoading(true);

    try {
      const response = await fetch(`${baseURL}/tools/django-generator-status`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.info || "Failed to generate");
      }

      const data = await response.json();
      setOpenModal(true);
      setStatus(data);
    } catch (error) {
      console.error("Error generating:", error);
      setOpenModal(true);
      setStatus({
        status: "error",
        info: error.message || "Something went wrong!",
      });
    } finally {
      setLoading(false);
    }
  };

  const handleUI = async () => {
    setLoading(true);
    try {
      const response = await fetch(`${baseURL}/tools/django-generator/design`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (!response.ok) {
        throw new Error("Failed to generate");
      }

      const data = await response.json();
      if (data.ui) {
        setUI(data.ui);
      } else {
        toast.error(
          <>
            Status: Error <br />
            Info: Failed to fetch design
          </>
        );
      }
    } catch (error) {
      console.error("Error generating:", error);
      toast.error(
        <>
          Status: Error <br />
          Info: Something went wrong!
        </>
      );
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    handleUI();
  }, []);

  useEffect(() => {
    if (design) {
      setDesignSelection(design)
    }
  }, [design])

  const selectedDesign =
    designSelection === "soft"
      ? "soft"
      : designSelection === "material"
        ? "material"
        : designSelection === "argon"
          ? "argon"
          : designSelection === "corporate"
            ? "corporate"
            : designSelection === "black"
              ? "black"
              : designSelection === "berry"
                ? "berry"
                : designSelection === "datta"
                  ? "datta"
                  : designSelection === "gradient"
                    ? "gradient"
                    : designSelection === "volt"
                      ? "volt"
                      : designSelection === "adminlte"
                        ? "adminlte"
                        : designSelection === "tabler"
                          ? "tabler"
                          : designSelection === "soft-kit"
                            ? "soft-kit"
                            : designSelection === "material-kit"
                              ? "material-kit"
                              : "pixel";

  return (
    <>
      <div
        className={`min-h-screen bg-gray-100 p-6 ${openModal
          ? "fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center"
          : ""
          }`}
      >
        {/* Main Content */}
        <form className="w-full" onSubmit={handleGenerate}>
          <h1 className="mb-6 text-3xl font-semibold text-center">
            Django Generator
          </h1>
          <div className="grid grid-cols-1 gap-6 lg:grid-cols-2">
            {/* Project Details */}
            <div className="p-6 bg-white rounded-lg shadow-md">
              {/* <h2 className="mb-4 text-xl font-bold">Project Details</h2> */}
              <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-2">
                <div>
                  <label className="block text-gray-700">Project Name</label>
                  <input
                    type="text"
                    name="project_name"
                    value={formData.project_name}
                    onChange={handleChange}
                    placeholder="Project Name here"
                    className="w-full p-2 mt-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                    required
                  />
                </div>
                <div>
                  <label className="block text-gray-700">Backend</label>
                  <input
                    type="text"
                    name="backend"
                    value={formData.backend}
                    readOnly
                    onChange={handleChange}
                    className="w-full p-2 mt-1 text-gray-400 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                    placeholder="e.g., Django, Node.js"
                  />
                </div>
                <div>
                  <select
                    name="design"
                    value={designSelection}
                    onChange={handleChange}
                    className="w-full p-2 mt-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                  >
                    <option value="soft">Soft Dashboard</option>
                    <option value="material">Material Dashboard</option>
                    <option value="argon">Argon Dashboard</option>
                    <option value="corporate">Corporate Dashboard</option>
                    <option value="black">Black Dashboard</option>
                    <option value="berry">Berry Dashboard</option>
                    <option value="datta">Datta Dashboard</option>
                    <option value="gradient">Gradient Dashboard</option>
                    <option value="volt">Volt Dashboard</option>
                    <option value="adminlte">AdminLTE</option>
                    <option value="tabler">Tabler</option>
                    <option value="soft-kit">Soft UI</option>
                    <option value="material-kit">Material Kit</option>
                    <option value="pixel">Pixel UI</option>
                  </select>
                </div>
                <div className="flex items-start">
                  <a
                    href={ui[selectedDesign]?.demo_url}
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    <img
                      src={ui[selectedDesign]?.img_thumb}
                      alt={selectedDesign}
                      className="object-cover h-20 w-15"
                    />
                  </a>
                  <label className="pt-2">(click for preview)</label>
                </div>
              </div>
            </div>

            {/* Database Configuration */}
            <div className="p-6 bg-white rounded-lg shadow-md">
              {/* <h2 className="mb-4 text-xl font-bold">Database Settings</h2> */}
              <div className="flex flex-col w-full gap-4">
                <div className="flex gap-4">
                  <div className="flex flex-col w-full gap-2">
                    <label className="block text-gray-700">DB Driver</label>
                    <CustomSelect

                      options={dbDriverOptions}
                      value={dbDriverOptions.find(
                        (option) => option.value === formData.db.driver
                      )}
                      onChange={handleDBChange}
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
                      value={formData.db.name}
                      onChange={handleDBFieldChange}
                      className="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                      placeholder="Database Name"
                      required
                    />
                  </div>
                </div>
                {formData.db.driver !== "sqlite" && (
                  <div className="grid grid-cols-2 gap-4">
                    <div className="flex flex-col w-full gap-2">
                      <label className="block text-gray-700">User</label>
                      <input
                        type="text"
                        name="user"
                        value={formData.db.user}
                        onChange={handleDBFieldChange}
                        className="w-full p-2 mt-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                        placeholder="Database userName"
                      />
                    </div>
                    <div className="flex flex-col w-full gap-2">
                      <label className="block text-gray-700">Password</label>
                      <input
                        type="password"
                        name="pass"
                        value={formData.db.pass}
                        onChange={handleDBFieldChange}
                        className="w-full p-2 mt-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                        placeholder="Database Password"
                      />
                    </div>
                    <div className="flex flex-col w-full gap-2">
                      <label className="block text-gray-700">Host</label>
                      <input
                        type="text"
                        name="host"
                        value={formData.db.host || "localhost"}
                        onChange={handleDBFieldChange}
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
                          formData.db.port ||
                          (formData.db.driver === "mysql"
                            ? 3306
                            : formData.db.driver === "postgresql"
                              ? 5432
                              : "")
                        }
                        onChange={handleDBFieldChange}
                        className="w-full p-2 mt-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                        placeholder="Database Port"
                      />
                    </div>
                  </div>
                )}
              </div>
            </div>

            {/* Models Configuration */}
            <div className="p-6 bg-white rounded-lg shadow-md lg:col-span-2">
              <h2 className="mb-4 text-xl font-bold">Database Tables</h2>
              <div className="py-2 mb-4 rounded-lg ">
                <ul className="flex flex-wrap text-sm font-medium text-center text-gray-500 border-b border-gray-200 dark:border-gray-700 dark:text-gray-400">
                  {/* Static Tabs */}
                  <li className="me-2">
                    <div
                      onClick={() => setActiveTab("create")}
                      aria-current="page"
                      className={`inline-block p-4 rounded-t-lg cursor-pointer
                        ${activeTab === "create"
                          ? "text-blue-600 bg-gray-100 active dark:bg-gray-800 dark:text-blue-500"
                          : "hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300"
                        }`}
                    >
                      Create Model
                    </div>
                  </li>
                  {Object.keys(formData.models).map((model, index) => (
                    <li className="me-2" key={index}>
                      <div
                        onClick={() => handleTabChange(model)}
                        aria-current={activeTab === model ? "page" : undefined}
                        className={`inline-block p-4 rounded-t-lg cursor-pointer items-center
                        ${activeTab === model
                            ? "text-blue-600 bg-gray-100 active dark:bg-gray-800 dark:text-blue-500"
                            : "hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300"
                          }`}
                      >
                        {model}
                      </div>
                    </li>
                  ))}
                </ul>
              </div>

              {activeTab === "create" && (
                <div>
                  {successMessage && (
                    <div className="p-2 mb-4 text-green-700 bg-green-100 rounded">
                      {successMessage}
                    </div>
                  )}
                  <div className="mb-6">
                    <label className="block font-medium text-gray-700">
                      Model Name
                    </label>
                    <input
                      type="text"
                      value={modelName}
                      onChange={(e) => setModelName(e.target.value)}
                      className="w-full p-2 mt-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                      placeholder="e.g., Product"
                    />
                  </div>
                  <div className="flex flex-col gap-4 mb-6">
                    {modelFields.map((field, index) => (
                      <div
                        key={index}
                        className="flex flex-col gap-4 bg-white md:flex-row md:items-end md:space-x-4"
                      >
                        {/* Field Name */}
                        <div className="flex-1">
                          <label className="block mb-1 text-sm font-medium text-gray-700">
                            Field Name
                          </label>
                          <input
                            type="text"
                            value={field.fieldName}
                            onChange={(e) =>
                              handleModelFieldChange(
                                index,
                                "fieldName",
                                e.target.value,
                                modelFields,
                                setModelFields
                              )
                            }
                            className="w-full px-3 py-2 placeholder-gray-400 transition duration-150 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
                            placeholder="e.g., title"
                          />
                        </div>
                        {/* Field Type */}
                        <div className="flex-1">
                          <label className="block mb-1 text-sm font-medium text-gray-700">
                            Field Type
                          </label>
                          <CustomSelect
                            options={djangoFieldTypeOptions}
                            value={
                              djangoFieldTypeOptions.find(
                                (option) => option.value === field.fieldType
                              ) || null
                            }
                            onChange={(selectedOption) =>
                              handleModelFieldChange(
                                index,
                                "fieldType",
                                selectedOption ? selectedOption.value : "",
                                modelFields,
                                setModelFields
                              )
                            }
                            placeholder="Select Field Type"
                            styles={customStyles}
                            isClearable
                          />
                        </div>
                        {/* Related Model (Conditional) */}
                        {field.fieldType === "ForeignKey" && (
                          <div className="flex-1">
                            <label className="block mb-1 text-sm font-medium text-gray-700">
                              Related Model
                            </label>
                            <CustomSelect
                              options={Object.keys(formData.models).map(
                                (model) => ({ value: model, label: model })
                              )}
                              value={
                                Object.keys(formData.models)
                                  .map((model) => ({
                                    value: model,
                                    label: model,
                                  }))
                                  .find(
                                    (option) =>
                                      option.value === field.relatedModel
                                  ) || null
                              }
                              onChange={(selectedOption) =>
                                handleModelFieldChange(
                                  index,
                                  "relatedModel",
                                  selectedOption ? selectedOption.value : "",
                                  modelFields,
                                  setModelFields
                                )
                              }
                              placeholder="Select Field Type"
                              styles={customStyles}
                              isClearable
                            />
                          </div>
                        )}
                        {/* Remove Button */}
                        <div className="flex items-end mb-1">
                          <button
                            type="button"
                            onClick={() =>
                              removeField(index, modelFields, setModelFields)
                            }
                            className="inline-flex items-center px-3 py-2 text-sm font-medium text-white transition duration-150 bg-red-600 border border-transparent rounded-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
                            title="Remove Field"
                          >
                            X
                          </button>
                        </div>
                      </div>
                    ))}
                  </div>
                  <div className="flex items-center justify-center gap-4">
                    <button
                      type="button"
                      onClick={addModelField}
                      style={{ backgroundColor: "#172554" }}
                      className="px-6 py-2 text-white rounded hover:bg-blue-600"
                    >
                      Add Field
                    </button>
                    <button
                      type="button"
                      onClick={addModel}
                      className="px-6 py-2 text-white bg-blue-500 rounded hover:bg-blue-600"
                    >
                      Save Model
                    </button>
                  </div>
                </div>
              )}
              {activeTab !== "create" && activeTab in formData.models && (
                <div className="mt-4">
                  {successMessage && (
                    <div className="p-2 mb-4 text-green-700 bg-green-100 rounded">
                      {successMessage}
                    </div>
                  )}
                  <div className="flex flex-col gap-4 mb-6">
                    {updatedModelFields.map((field, index) => (
                      <div
                        key={index}
                        className="flex flex-col gap-4 bg-white md:flex-row md:items-end md:space-x-4"
                      >
                        {/* Field Name */}
                        <div className="flex-1">
                          <label className="block mb-1 text-sm font-medium text-gray-700">
                            Field Name
                          </label>
                          <input
                            type="text"
                            value={field.fieldName}
                            onChange={(e) =>
                              handleModelFieldChange(
                                index,
                                "fieldName",
                                e.target.value,
                                updatedModelFields,
                                setUpdatedModelFields
                              )
                            }
                            className="w-full px-3 py-2 placeholder-gray-400 transition duration-150 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
                            placeholder="e.g., title"
                          />
                        </div>
                        {/* Field Type */}
                        <div className="flex-1">
                          <label className="block mb-1 text-sm font-medium text-gray-700">
                            Field Type
                          </label>
                          <CustomSelect
                            options={djangoFieldTypeOptions}
                            value={
                              djangoFieldTypeOptions.find(
                                (option) => option.value === field.fieldType
                              ) || null
                            }
                            onChange={(selectedOption) =>
                              handleModelFieldChange(
                                index,
                                "fieldType",
                                selectedOption ? selectedOption.value : "",
                                updatedModelFields,
                                setUpdatedModelFields
                              )
                            }
                            placeholder="Select Field Type"
                            styles={customStyles}
                            isClearable
                          />
                        </div>
                        {/* Related Model (Conditional) */}
                        {field.fieldType === "ForeignKey" && (
                          <div className="flex-1">
                            <label className="block mb-1 text-sm font-medium text-gray-700">
                              Related Model
                            </label>
                            <CustomSelect
                              options={Object.keys(formData.models)
                                .filter((model) => model !== activeTab)
                                .map((model) => ({ value: model, label: model }))}
                              value={
                                Object.keys(formData.models)
                                  .map((model) => ({
                                    value: model,
                                    label: model,
                                  }))
                                  .find(
                                    (option) =>
                                      option.value === field.relatedModel
                                  ) || null
                              }
                              onChange={(selectedOption) =>
                                handleModelFieldChange(
                                  index,
                                  "relatedModel",
                                  selectedOption ? selectedOption.value : "",
                                  updatedModelFields,
                                  setUpdatedModelFields
                                )
                              }
                              placeholder="Select Field Type"
                              styles={customStyles}
                              isClearable
                            />
                          </div>
                        )}
                        {/* Remove Button */}
                        <div className="flex items-end mb-1">
                          <button
                            type="button"
                            onClick={() =>
                              removeField(
                                index,
                                updatedModelFields,
                                setUpdatedModelFields
                              )
                            }
                            className="inline-flex items-center px-3 py-2 text-sm font-medium text-white transition duration-150 bg-red-600 border border-transparent rounded-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
                            title="Remove Field"
                          >
                            X
                          </button>
                        </div>
                      </div>
                    ))}
                  </div>
                  <div className="flex items-center justify-center gap-4">
                    <button
                      type="button"
                      onClick={() => addUpdatedModelField(activeTab)}
                      style={{ backgroundColor: "#172554" }}
                      className="px-6 py-2 text-white rounded"
                    >
                      Add Field
                    </button>
                    <button
                      type="button"
                      onClick={() => saveModelChanges(activeTab)}
                      style={{ backgroundColor: "#3B82F6" }}
                      className="px-6 py-2 text-white rounded "
                    >
                      Save Changes
                    </button>
                    <button
                      type="button"
                      onClick={() => removeModelTab(activeTab)}
                      style={{ backgroundColor: "#FF0000" }}
                      className="px-6 py-2 text-white rounded"
                    >
                      Delete
                    </button>
                  </div>
                </div>
              )}
            </div>

            <div className="p-6 bg-white rounded-lg shadow-md">
              <h2 className="mb-4 text-lg font-bold">Extended User Model</h2>
              {successUserMessage && (
                <div className="p-2 mb-4 text-green-700 bg-green-100 rounded">
                  {successUserMessage}
                </div>
              )}
              <div className="flex flex-col gap-4 mb-6">
                {customFields.map((field, index) => (
                  <div
                    key={index}
                    className="flex flex-col gap-4 bg-white md:flex-row md:items-end md:space-x-4"
                  >
                    {/* Field Name */}
                    <div className="flex-1">
                      <label className="block mb-1 text-sm font-medium text-gray-700">
                        Field Name
                      </label>
                      <input
                        type="text"
                        value={field.fieldName}
                        onChange={(e) =>
                          handleModelFieldChange(
                            index,
                            "fieldName",
                            e.target.value,
                            customFields,
                            setCustomFields
                          )
                        }
                        className="w-full px-3 py-2 placeholder-gray-400 transition duration-150 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
                        placeholder="e.g., title"
                      />
                    </div>
                    {/* Field Type */}
                    <div className="flex-1">
                      <label className="block mb-1 text-sm font-medium text-gray-700">
                        Field Type
                      </label>
                      <CustomSelect
                        options={djangoFieldTypeOptions.filter(
                          (item) => item.label !== "ForeignKey"
                        )}
                        value={
                          djangoFieldTypeOptions.find(
                            (option) => option.value === field.fieldType
                          ) || null
                        }
                        onChange={(selectedOption) =>
                          handleModelFieldChange(
                            index,
                            "fieldType",
                            selectedOption ? selectedOption.value : "",
                            customFields,
                            setCustomFields
                          )
                        }
                        placeholder="Select Field Type"
                        styles={customStyles}
                        isClearable
                      />
                    </div>
                    {/* Remove Button */}
                    <div className="flex items-end mb-1">
                      <button
                        type="button"
                        onClick={() =>
                          removeField(index, customFields, setCustomFields)
                        }
                        className="inline-flex items-center px-3 py-2 text-sm font-medium text-white transition duration-150 bg-red-600 border border-transparent rounded-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
                        title="Remove Field"
                      >
                        X
                      </button>
                    </div>
                  </div>
                ))}
              </div>
              <div className="flex items-center justify-center gap-4">
                <button
                  type="button"
                  onClick={addUserModelField}
                  style={{ backgroundColor: "#172554" }}
                  className="px-6 py-2 text-white rounded hover:bg-blue-600"
                >
                  Add Field
                </button>
                <button
                  type="button"
                  onClick={saveUserModel}
                  className="px-6 py-2 text-white bg-blue-500 rounded hover:bg-blue-600"
                >
                  Save Model
                </button>
              </div>
            </div>

            <div className="grid grid-cols-2 gap-5">
              {/* Authentication */}
              <div className="p-6 bg-white rounded-lg shadow-md md:col-span-1 col-span-2">
                <h2 className="mb-4 text-xl font-bold">Authentication</h2>
                <div className="flex flex-col gap-4">
                  <div className="flex items-center">
                    <input
                      type="checkbox"
                      name="basic"
                      checked={authChecked.auth.basic}
                      onChange={handleAuthChange}
                      className="w-4 h-4 mr-2 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                    />
                    <label className="text-gray-700">Basic</label>
                  </div>
                  <div className="flex items-center">
                    <input
                      type="checkbox"
                      name="github"
                      checked={authChecked.auth.github}
                      onChange={handleAuthChange}
                      className="w-4 h-4 mr-2 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                    />
                    <label className="text-gray-700">GitHub</label>
                  </div>
                  <div className="flex items-center">
                    <input
                      type="checkbox"
                      name="google"
                      disabled
                      className="w-4 h-4 mr-2 text-gray-300 border-gray-300 rounded focus:ring-blue-500"
                    />
                    <label className="text-gray-400">
                      Google <span className="text-sm text-gray-500">(Soon)</span>
                    </label>
                  </div>
                  <div className="flex items-center">
                    <input
                      type="checkbox"
                      name="otp"
                      disabled
                      className="w-4 h-4 mr-2 text-gray-300 border-gray-300 rounded focus:ring-blue-500"
                    />
                    <label className="text-gray-400">
                      OTP (one-time password){" "}
                      <span className="text-sm text-gray-500">(Soon)</span>
                    </label>
                  </div>
                </div>
              </div>
              {/* Tools */}
              <div className="p-6 bg-white rounded-lg shadow-md md:col-span-1 col-span-2">
                <h2 className="mb-4 text-xl font-bold">Tools</h2>
                <div className="flex flex-col gap-4">
                  <div className="flex items-center">
                    <input
                      type="checkbox"
                      name="celery"
                      checked={formData.tools.celery}
                      onChange={handleToolsChange}
                      className="w-4 h-4 mr-2 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                    />
                    <label className="text-gray-700">Celery</label>
                  </div>
                  <div className="flex items-center">
                    <input
                      type="checkbox"
                      name="dynamicApiModule"
                      checked={formData.tools.dynamicApiModule}
                      onChange={handleToolsChange}
                      className="w-4 h-4 mr-2 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                    />
                    <label className="text-gray-700">Dynamic API Module</label>
                  </div>
                  {Object.keys(formData.models).length !== 0 && (
                    <div className="flex flex-col gap-4 ml-4">
                      {Object.keys(formData.models).map((modelName, index) => (
                        <div key={index} className="flex items-center">
                          <input
                            type="checkbox"
                            name={`api_generator_${modelName}`}
                            checked={!!formData.tools.api_generator[modelName]}
                            onChange={(e) => handleToolsChange(e, modelName)}
                            className="w-4 h-4 mr-2 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                          />
                          <label className="text-gray-700">
                            API Generator for {modelName} Model
                          </label>
                        </div>
                      ))}
                    </div>
                  )}
                  <div className="flex items-center">
                    <input
                      type="checkbox"
                      name="dynamicDataTables"
                      disabled
                      className="w-4 h-4 mr-2 text-gray-300 border-gray-300 rounded focus:ring-blue-500"
                    />
                    <label className="text-gray-400">
                      Dynamic DataTables{" "}
                      <span className="text-sm text-gray-500">(Soon)</span>
                    </label>
                  </div>

                  <div className="flex items-center">
                    <input
                      type="checkbox"
                      name="reactIntegration"
                      disabled
                      className="w-4 h-4 mr-2 text-gray-300 border-gray-300 rounded focus:ring-blue-500"
                    />
                    <label className="text-gray-400">
                      React Integration{" "}
                      <span className="text-sm text-gray-500">(Soon)</span>
                    </label>
                  </div>
                </div>
              </div>
            </div>

            {/* Deployment */}
            <div className="p-6 bg-white rounded-lg shadow-md">
              <h2 className="mb-4 text-xl font-bold">Deployment</h2>
              <div className="flex flex-col gap-4">
                <div className="flex items-center">
                  <input
                    type="checkbox"
                    name="docker"
                    checked={formData.deploy.docker}
                    onChange={handleDeployChange}
                    className="w-4 h-4 mr-2 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                  />
                  <label className="text-gray-700">Docker</label>
                </div>
                <div className="flex items-center">
                  <input
                    type="checkbox"
                    name="ci_cd"
                    checked={formData.deploy.ci_cd}
                    onChange={handleDeployChange}
                    className="w-4 h-4 mr-2 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                  />
                  <label className="text-gray-700">Render CI/Cd Scripts</label>
                </div>
                <div className="flex items-center">
                  <input
                    type="checkbox"
                    name="go_live"
                    checked={formData.deploy.go_live}
                    onChange={handleDeployChange}
                    disabled
                    className="w-4 h-4 mr-2 text-gray-300 border-gray-300 rounded focus:ring-blue-500"
                  />
                  <label className="text-gray-400">
                    Render Go LIVE
                    <span className="text-sm text-gray-500">(Soon)</span>
                  </label>
                </div>
              </div>
            </div>

          </div>
          <div>
            <button
              type="submit"
              className="w-full px-6 py-3 mt-6 text-white transition-colors duration-300 bg-gray-800 rounded-lg hover:bg-gray-700"
              onClick={handleGenerate}
              disabled={loading}
            >
              {loading ? "Generating..." : "Generate"}
            </button>
          </div>
          <ToastContainer />
        </form>
        <Status open={openModal} handleClose={handleClose} status={status} />
      </div>
      <LoadingOverlay isLoading={loading} />
    </>
  );
};

export default DjangoGenerator;
