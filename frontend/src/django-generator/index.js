import React, { useState } from 'react';
import Select from 'react-select';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css'
// Define options for react-select
const dbDriverOptions = [
    { value: 'postgresql', label: 'PostgreSQL' },
    { value: 'mysql', label: 'MySQL' },
    { value: 'sqlite', label: 'SQLite' },
    { value: 'mariadb', label: 'MariaDB' },
    // Add more as needed
];

const djangoFieldTypeOptions = [
    { value: 'CharField', label: 'CharField' },
    { value: 'TextField', label: 'TextField' },
    { value: 'ForeignKey', label: 'ForeignKey' },
    { value: 'BooleanField', label: 'BooleanField' },
    { value: 'IntegerField', label: 'IntegerField' },
    { value: 'DateField', label: 'DateField' },
    // Add more as needed
];

const DjangoGenerator = () => {
    const [formData, setFormData] = useState({
        project_name: '',
        backend: 'Django',
        frontend: 'NA',
        design: 'NA',
        db: {
            driver: 'sqlite',
            name: '',
            user: '',
            pass: '',
            host: 'localhost',
            port: ''
        },
        models: {},
        auth: {
            basic: true,
            github: false,
            google: false,
            opt: false
        },
        custom_user: {
            phone: '',
            zip: ''
        },
        deploy: {
            docker: false,
            ci_cd: false,
            go_live: false
        },
        tools: {
            celery: false,
            dynamicApiModule: false,
            dynamicDataTables: false,
            reactIntegration: false,
            api_generator: {}
        }
    });

    const [modelName, setModelName] = useState('');
    const [modelFields, setModelFields] = useState([{ fieldName: '', fieldType: '', relatedModel: '' }]);
    const [successMessage, setSuccessMessage] = useState('');
    const [expandedModels, setExpandedModels] = useState({}); // For collapsible model cards

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
        { id: Date.now(), name: 'phone', type: 'text', value: '' },
        { id: Date.now() + 1, name: 'zip', type: 'text', value: '' }
    ]);

    const [newField, setNewField] = useState({ name: '', type: 'text' });
    const [activeTab, setActiveTab] = useState('create');
    const [loading, setLoading] = useState(false);

    // Handle changes for main form inputs
    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({
            ...prev,
            [name]: value
        }));
        setDesignSelection(e.target.value);
    };

    // Handle changes for Database driver (react-select)
    const handleDBChange = (selectedOption) => {
        setFormData(prev => ({
            ...prev,
            db: {
                ...prev.db,
                driver: selectedOption ? selectedOption.value : ''
            }
        }));
    };

    // Handle changes for Database fields (Separate Handler)
    const handleDBFieldChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({
            ...prev,
            db: {
                ...prev.db,
                [name]: value
            }
        }));
    };

    // Handle changes for Authentication checkboxes
    const handleAuthChange = (e) => {
        const { name, checked } = e.target;
        setFormData(prev => ({
            ...prev,
            auth: {
                ...prev.auth,
                [name]: checked
            }
        }));
        setAuthChecked(prev => ({
            ...prev,
            auth: {
                ...prev.auth,
                [name]: checked
            }
        }));
    };

    // Handle changes for Deployment checkboxes
    const handleDeployChange = (e) => {
        const { name, checked } = e.target;
        setFormData(prev => ({
            ...prev,
            deploy: {
                ...prev.deploy,
                [name]: checked
            }
        }));
    };

    // Handle changes for Tools checkboxes and api_generator
    const handleToolsChange = (e, modelName = null) => {
        const { name, checked } = e.target;
        if (name.startsWith('api_generator_') && modelName) {
            setFormData(prev => ({
                ...prev,
                tools: {
                    ...prev.tools,
                    api_generator: {
                        ...prev.tools.api_generator,
                        [modelName]: checked ? `home.models.${modelName}` : undefined
                    }
                }
            }));
        } else {
            setFormData(prev => ({
                ...prev,
                tools: {
                    ...prev.tools,
                    [name]: checked
                }
            }));
        }
    };

    // Handle changes for Custom User Fields
    const handleCustomUserChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({
            ...prev,
            custom_user: {
                ...prev.custom_user,
                [name]: value
            }
        }));
    };

    // Add a new model to formData.models
    const addModel = () => {
        const trimmedModelName = modelName.trim();
        if (trimmedModelName === '') {
            alert('Model name cannot be empty.');
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
                if (fieldType === 'ForeignKey') {
                    if (relatedModel.trim() === '') {
                        alert(`ForeignKey field "${fieldName}" requires a related model name.`);
                        throw new Error('Related model name is missing.');
                    }
                    acc[fieldName.trim()] = { type: fieldType.trim(), related_model: relatedModel.trim() };
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
            alert('Please add at least one valid field.');
            return;
        }

        setFormData(prev => ({
            ...prev,
            models: {
                ...prev.models,
                [trimmedModelName]: newModel
            }
        }));

        // Reset the model input fields
        setModelName('');
        setModelFields([{ fieldName: '', fieldType: '', relatedModel: '' }]);

        // Show success message
        setSuccessMessage(`Model "${trimmedModelName}" added successfully!`);
        setTimeout(() => setSuccessMessage(''), 3000); // Clear message after 3 seconds
    };

    // Handle changes in model fields
    const handleModelFieldChange = (index, field, value) => {
        const updatedFields = [...modelFields];
        updatedFields[index][field] = value;
        setModelFields(updatedFields);
    };

    // Add a new field to the current model
    const addModelField = () => {
        setModelFields([...modelFields, { fieldName: '', fieldType: '', relatedModel: '' }]);
    };

    // Remove a field from the current model
    const removeModelField = (index) => {
        const updatedFields = modelFields.filter((_, i) => i !== index);
        setModelFields(updatedFields);
    };

    // Toggle model card expansion
    const toggleModelExpansion = (model) => {
        setExpandedModels(prev => ({
            ...prev,
            [model]: !prev[model]
        }));
    };
    const handleGenerate = async (e) => {
        e.preventDefault();
        console.log(JSON.stringify(formData, null, 2));
        setLoading(true);
        // setModalOpen(false);

        try {
            const response = await fetch('http://127.0.0.1:8000/tools/django-generator-statusd', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: formData,
            });

            if (!response.ok) {
                throw new Error('Failed to generate');
            }

            const data = await response.json();
            toast.success(
                <>
                Status: {data.status} <br />
                Info: {data.info}
              </>
            );

        } catch (error) {
            console.error('Error generating:', error);
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

    const ui = {
        "datta-able": {
            "img_thumb": "https://appsrv1-147a1.kxcdn.com/appseed-v2/media/products/datta-able/top.png",
            "demo_url": "https://django-datta-able.appseed-srv1.com/",
        },
        "soft-dashboard": {
            "img_thumb": "https://appsrv1-147a1.kxcdn.com/appseed-v2/media/products/soft-ui-dashboard/top.png",
            "demo_url": "https://django-soft-dash.onrender.com/",
        },
        "volt-dashboard": {
            "img_thumb": "https://appsrv1-147a1.kxcdn.com/appseed-v2/media/products/volt-dashboard/top.png",
            "demo_url": "https://django-volt.onrender.com/",
        },
    };

    const selectedDesign = designSelection === "soft"
        ? "soft-dashboard"
        : designSelection === "volt"
            ? "volt-dashboard"
            : "datta-able";

    const handleCustomUserChanges = (id, value) => {
        setCustomFields((prevFields) =>
            prevFields.map((field) =>
                field.id === id ? { ...field, value } : field
            )
        );
    };

    const addField = () => {
        if (newField.name) {
            setCustomFields((prevFields) => [
                ...prevFields,
                { id: Date.now(), name: newField.name, type: newField.type, value: '' }
            ]);
            setNewField({ name: '', type: 'text' });
        }
    };

    const deleteField = (id) => {
        setCustomFields((prevFields) =>
            prevFields.filter((field) => field.id !== id)
        );
    };

    return (
        <div className="min-h-screen bg-gray-100 p-6">
            {/* Main Content */}
            <form className="max-w-7xl mx-auto" onSubmit={handleGenerate}>
                <h1 className="text-3xl font-semibold mb-6 text-center">Django Generator</h1>
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                    {/* Project Details */}
                    <div className="bg-white p-6 rounded-lg shadow-md">
                        <h2 className="text-xl font-bold mb-4">Project Details</h2>
                        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-2 gap-4">
                            <div>
                                <label className="block text-gray-700">Project Name</label>
                                <input
                                    type="text"
                                    name="project_name"
                                    value={formData.project_name}
                                    onChange={handleChange}
                                    className="w-full mt-1 p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
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
                                    className="w-full mt-1 p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                                    placeholder="e.g., Django, Node.js"
                                />
                            </div>
                            <div>
                                <label className="block text-gray-700">Frontend</label>
                                <input
                                    type="text"
                                    name="frontend"
                                    value={formData.frontend}
                                    onChange={handleChange}
                                    className="w-full mt-1 p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                                    placeholder="e.g., React, Angular"
                                />
                            </div>
                            <div className="flex items-center space-x-4">
                                <div className='w-full'>
                                    <label className="block text-gray-700">Design</label>
                                    <select
                                        name="design"
                                        value={designSelection}
                                        onChange={handleChange}
                                        className="w-full mt-1 p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                                    >
                                        <option value="soft">Soft</option>
                                        <option value="volt">Volt</option>
                                        <option value="datta">Datta</option>
                                    </select>
                                </div>

                                <div>
                                    <a
                                        href={ui[selectedDesign].demo_url}
                                        target="_blank"
                                        rel="noopener noreferrer"
                                    >
                                        <img
                                            src={ui[selectedDesign].img_thumb}
                                            alt={selectedDesign}
                                            className="w-15 h-20 object-cover"
                                        />
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>

                    {/* Database Configuration */}
                    <div className="bg-white p-6 rounded-lg shadow-md">
                        <h2 className="text-xl font-bold mb-4">Database Settings</h2>
                        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                            <div>
                                <label className="block text-gray-700">Driver</label>
                                <Select
                                    options={dbDriverOptions}
                                    value={dbDriverOptions.find(option => option.value === formData.db.driver)}
                                    onChange={handleDBChange}
                                    placeholder="Select Database Driver"
                                    isClearable
                                />
                            </div>

                            {/* Show "Name" field for mysql, mariadb, postgresql, and sqlite */}
                            {(formData.db.driver === 'mysql' || formData.db.driver === 'mariadb' || formData.db.driver === 'postgresql' || formData.db.driver === 'sqlite') && (
                                <div>
                                    <label className="block text-gray-700">Name</label>
                                    <input
                                        type="text"
                                        name="name"
                                        value={formData.db.name}
                                        onChange={handleDBFieldChange}
                                        className="w-full mt-1 p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                                        placeholder="Database Name"
                                        required
                                    />
                                </div>
                            )}

                            <div>
                                <label className="block text-gray-700">User</label>
                                <input
                                    type="text"
                                    name="user"
                                    value={formData.db.user}
                                    onChange={handleDBFieldChange}
                                    className="w-full mt-1 p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                                    placeholder="Database User"
                                />
                            </div>
                            <div>
                                <label className="block text-gray-700">Password</label>
                                <input
                                    type="password"
                                    name="pass"
                                    value={formData.db.pass}
                                    onChange={handleDBFieldChange}
                                    className="w-full mt-1 p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                                    placeholder="Database Password"
                                />
                            </div>
                            <div>
                                <label className="block text-gray-700">Host</label>
                                <input
                                    type="text"
                                    name="host"
                                    value={formData.db.host || 'localhost'}
                                    onChange={handleDBFieldChange}
                                    className="w-full mt-1 p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                                    placeholder="Database Host"
                                />
                            </div>
                            <div>
                                <label className="block text-gray-700">Port</label>
                                <input
                                    type="number"
                                    name="port"
                                    value={
                                        formData.db.port ||
                                        (formData.db.driver === 'mysql' ? 3306 : formData.db.driver === 'postgresql' ? 5432 : '')
                                    }
                                    onChange={handleDBFieldChange}
                                    className="w-full mt-1 p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                                    placeholder="Database Port"
                                />
                            </div>
                        </div>
                    </div>

                    {/* Models Configuration */}
                    <div className="bg-white p-6 rounded-lg shadow-md lg:col-span-2">
                        <h2 className="text-xl font-bold mb-4">Database Tables</h2>
                        <div className="p-2 rounded-lg mb-4 ">
                            <ul style={{display:'flex',justifyContent:"space-around"}}>
                                <li>
                                    <a
                                        onClick={() => setActiveTab('create')}
                                        className={`px-4 py-2 rounded-md cursor-pointer duration-200 
                    ${activeTab === 'create' ? 'text-blue-500 font-bold border-b-2 border-blue-500 underline' : 'text-gray-700 hover:text-blue-500'}`}
                                    >
                                        Create Model
                                    </a>
                                </li>
                                <li>
                                    <a
                                        onClick={() => setActiveTab('added')}
                                        className={`px-4 py-2 rounded-md cursor-pointer duration-200 
                    ${activeTab === 'added' ? 'text-blue-500 font-bold border-b-2 border-blue-500 underline' : 'text-gray-700 hover:text-blue-500'}`}
                                    >
                                        Added Models
                                    </a>
                                </li>
                            </ul>
                        </div>


                        {activeTab === 'create' && (
                            <div>
                                {successMessage && (
                                    <div className="mb-4 p-2 bg-green-100 text-green-700 rounded">
                                        {successMessage}
                                    </div>
                                )}
                                <div className="mb-6">
                                    <label className="block text-gray-700 font-medium">Model Name</label>
                                    <input
                                        type="text"
                                        value={modelName}
                                        onChange={(e) => setModelName(e.target.value)}
                                        className="w-full mt-1 p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                                        placeholder="e.g., Product"
                                    />
                                </div>
                                <div className="mb-6">
                                    <h3 className="text-lg font-semibold mb-2">Fields</h3>
                                    {modelFields.map((field, index) => (
                                        <div key={index} className="flex flex-col md:flex-row items-start md:items-center mb-4">
                                            <div className="flex-1 mr-2 mb-2 md:mb-0">
                                                <label className="block text-gray-600">Field Name</label>
                                                <input
                                                    type="text"
                                                    value={field.fieldName}
                                                    onChange={(e) => handleModelFieldChange(index, 'fieldName', e.target.value)}
                                                    className="w-full mt-1 p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                                                    placeholder="e.g., title"
                                                />
                                            </div>
                                            <div className="flex-1 mr-2 mb-2 md:mb-0">
                                                <label className="block text-gray-600">Field Type</label>
                                                <Select
                                                    options={djangoFieldTypeOptions}
                                                    value={djangoFieldTypeOptions.find(option => option.value === field.fieldType)}
                                                    onChange={(selectedOption) => handleModelFieldChange(index, 'fieldType', selectedOption ? selectedOption.value : '')}
                                                    placeholder="Select Field Type"
                                                    isClearable
                                                />
                                            </div>
                                            {field.fieldType === 'ForeignKey' && (
                                                <div className="flex-1 mr-2 mb-2 md:mb-0">
                                                    <label className="block text-gray-600">Related Model</label>
                                                    <input
                                                        type="text"
                                                        value={field.relatedModel}
                                                        onChange={(e) => handleModelFieldChange(index, 'relatedModel', e.target.value)}
                                                        className="w-full mt-1 p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                                                        placeholder="e.g., Category"
                                                    />
                                                </div>
                                            )}
                                            <div className="flex items-end">
                                                {modelFields.length > 1 && (
                                                    <button
                                                        type="button"
                                                        onClick={() => removeModelField(index)}
                                                        className="mt-1 px-3 py-1 bg-red-500 text-white rounded hover:bg-red-600"
                                                        title="Remove Field"
                                                    >
                                                        Remove
                                                    </button>
                                                )}
                                            </div>
                                        </div>
                                    ))}
                                    <button
                                        type="button"
                                        onClick={addModelField}
                                        style={{ backgroundColor: '#172554' }}
                                        className="ml-3 px-6 py-2 text-white rounded hover:bg-blue-600"
                                    >
                                        Add Field
                                    </button>
                                </div>
                                <div className="flex space-x-4 mb-6">
                                    <button
                                        type="button"
                                        onClick={addModel}
                                        className="px-6 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
                                    >
                                        Add Model
                                    </button>
                                </div>
                            </div>
                        )}
                        {activeTab === 'added' && (
                            <div className="mt-4">
                                <h3 className="text-lg font-semibold mb-2">Added Models:</h3>
                                {Object.keys(formData.models).length === 0 ? (
                                    <p className="text-gray-600">No models added yet.</p>
                                ) : (
                                    <div className="space-y-4">
                                        {Object.entries(formData.models).map(([model, fields], index) => (
                                            <div key={index} className="border border-gray-300 rounded-lg p-4 bg-gray-50">
                                                <div className="flex justify-between items-center mb-2">
                                                    <h4 className="text-md font-medium">{model}</h4>
                                                    <button
                                                        type="button"
                                                        onClick={() => toggleModelExpansion(model)}
                                                        className="text-blue-500 hover:underline"
                                                    >
                                                        {expandedModels[model] ? 'Collapse' : 'Expand'}
                                                    </button>
                                                </div>
                                                {expandedModels[model] && (
                                                    <pre className="bg-white p-2 rounded mt-2 border border-gray-200 overflow-auto">
                                                        {JSON.stringify(fields, null, 2)}
                                                    </pre>
                                                )}
                                            </div>
                                        ))}
                                    </div>
                                )}
                            </div>
                        )}
                    </div>

                    {/* Authentication */}
                    <div className="bg-white p-6 rounded-lg shadow-md">
                        <h2 className="text-xl font-bold mb-4">Authentication</h2>
                        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                            <div className="flex items-center">
                                <input
                                    type="checkbox"
                                    name="basic"
                                    checked={authChecked.auth.basic}
                                    onChange={handleAuthChange}
                                    className="mr-2 h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                                />
                                <label className="text-gray-700">Basic</label>
                            </div>
                            <div className="flex items-center">
                                <input
                                    type="checkbox"
                                    name="github"
                                    checked={authChecked.auth.github}
                                    onChange={handleAuthChange}
                                    className="mr-2 h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                                />
                                <label className="text-gray-700">GitHub</label>
                            </div>

                            <div className="flex items-center">
                                <input
                                    type="checkbox"
                                    name="google"
                                    disabled
                                    className="mr-2 h-4 w-4 text-gray-300 border-gray-300 rounded focus:ring-blue-500"
                                />
                                <label className="text-gray-700">Google <span className="text-sm text-gray-500">(Soon)</span></label>
                            </div>

                            <div className="flex items-center">
                                <input
                                    type="checkbox"
                                    name="otp"
                                    disabled
                                    className="mr-2 h-4 w-4 text-gray-300 border-gray-300 rounded focus:ring-blue-500"
                                />
                                <label className="text-gray-700">OTP <span className="text-sm text-gray-500">(Soon)</span></label>
                            </div>
                        </div>
                    </div>


                    <div className="bg-white p-6 rounded-lg shadow-md">
                        <h2 className="text-lg font-bold mb-4">Extended User Model</h2>
                        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                            {customFields.map((field) => (
                                <div key={field.id}>
                                    <label className="block text-gray-700">{field.name.charAt(0).toUpperCase() + field.name.slice(1)}</label>
                                    <input
                                        type={field.type}
                                        name={field.name}
                                        value={field.value}
                                        onChange={(e) => handleCustomUserChanges(field.id, e.target.value)}
                                        className="w-full mt-1 p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                                        placeholder={`e.g., ${field.name}`}
                                    />
                                    <button
                                        type="button"
                                        onClick={() => deleteField(field.id)}
                                        className="mt-2 text-red-600 hover:underline"
                                    >
                                        Delete
                                    </button>
                                </div>
                            ))}
                        </div>

                        <h3 className="text-lg font-semibold mt-4 text-center mb-4">Add New Fields</h3>
                        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-2 gap-4">
                            <input
                                type="text"
                                value={newField.name}
                                onChange={(e) => setNewField({ ...newField, name: e.target.value })}
                                className="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                                placeholder="Field Name"
                            />
                            <select
                                value={newField.type}
                                onChange={(e) => setNewField({ ...newField, type: e.target.value })}
                                className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                            >
                                <option value="text">Text</option>
                                <option value="number">Number</option>
                                <option value="email">Email</option>
                            </select>
                            <button
                                type="button"
                                onClick={addField}
                                className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 w-32"
                            >
                                Add Field
                            </button>
                        </div>
                    </div>

                    {/* Deployment */}
                    <div className="bg-white p-6 rounded-lg shadow-md">
                        <h2 className="text-xl font-bold mb-4">Deployment</h2>
                        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                            <div className="flex items-center">
                                <input
                                    type="checkbox"
                                    name="docker"
                                    checked={formData.deploy.docker}
                                    onChange={handleDeployChange}
                                    className="mr-2 h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                                />
                                <label className="text-gray-700">Docker</label>
                            </div>
                            <div className="flex items-center">
                                <input
                                    type="checkbox"
                                    name="ci_cd"
                                    checked={formData.deploy.ci_cd}
                                    onChange={handleDeployChange}
                                    className="mr-2 h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                                />
                                <label className="text-gray-700">CI/CD</label>
                            </div>
                            <div className="flex items-center">
                                <input
                                    type="checkbox"
                                    name="go_live"
                                    checked={formData.deploy.go_live}
                                    onChange={handleDeployChange}
                                    disabled
                                    className="mr-2 h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                                />
                                <label className="text-gray-700">Go Live<span className="text-sm text-gray-500">(Soon)</span></label>
                            </div>
                        </div>
                    </div>

                    {/* Tools */}
                    <div className="bg-white p-6 rounded-lg shadow-md lg:col-span-2">
                        <h2 className="text-xl font-bold mb-4">Tools</h2>
                        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                            <div className="flex items-center">
                                <input
                                    type="checkbox"
                                    name="celery"
                                    checked={formData.tools.celery}
                                    onChange={handleToolsChange}
                                    className="mr-2 h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                                />
                                <label className="text-gray-700">Celery</label>
                            </div>

                            <div className="flex items-center">
                                <input
                                    type="checkbox"
                                    name="dynamicApiModule"
                                    checked={formData.tools.dynamicApiModule}
                                    onChange={handleToolsChange}
                                    className="mr-2 h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                                />
                                <label className="text-gray-700">Dynamic API Module</label>
                            </div>

                            <div className="flex items-center">
                                <input
                                    type="checkbox"
                                    name="dynamicDataTables"
                                    disabled
                                    className="mr-2 h-4 w-4 text-gray-300 border-gray-300 rounded focus:ring-blue-500"
                                />
                                <label className="text-gray-700">
                                    Dynamic DataTables <span className="text-sm text-gray-500">(Soon)</span>
                                </label>
                            </div>

                            <div className="flex items-center">
                                <input
                                    type="checkbox"
                                    name="reactIntegration"
                                    disabled
                                    className="mr-2 h-4 w-4 text-gray-300 border-gray-300 rounded focus:ring-blue-500"
                                />
                                <label className="text-gray-700">
                                    React Integration <span className="text-sm text-gray-500">(Soon)</span>
                                </label>
                            </div>
                        </div>

                        {Object.keys(formData.models).map((modelName, index) => (
                            <div key={index} className="flex items-center mt-4">
                                <input
                                    type="checkbox"
                                    name={`api_generator_${modelName}`}
                                    checked={!!formData.tools.api_generator[modelName]}
                                    onChange={(e) => handleToolsChange(e, modelName)}
                                    className="mr-2 h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                                />
                                <label className="text-gray-700">API Generator for {modelName} Model</label>
                            </div>
                        ))}
                    </div>
                </div>
                <div>
                    <button
                        type="submit"
                        className="mt-6 w-full px-6 py-3 bg-gray-800 text-white rounded-lg hover:bg-gray-700 transition-colors duration-300"
                        onClick={handleGenerate}
                        disabled={loading}
                    >
                        {loading ? 'Generating...' : 'Generate'}
                    </button>
                </div>
                <ToastContainer />

            </form>
        </div>
    );
};

export default DjangoGenerator;
