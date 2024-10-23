import React, { useState, useEffect } from "react";
import './index.css';

const Table = ({ headers, data, limit, editable = false, setChanges = () => { }, setAction = () => { } }) => {
  const displayData = limit ? data.slice(0, limit) : data;
  const [editingIndex, setEditingIndex] = useState(null);
  const [headerValues, setHeaderValues] = useState(headers);

  useEffect(() => {
    if (headerValues.length === 0) {
      setHeaderValues(headers);  // Set the initial values when component first mounts
    }
  }, [headers]);

  const handleDoubleClick = (index) => {
    setEditingIndex(index);
  };

  const handleBlur = () => {
    setEditingIndex(null);
  };

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      setEditingIndex(null);
    }
  };

  const handleChangeInput = (index, value) => {
    setHeaderValues((prevHeaders) =>
      prevHeaders.map((header, i) => (i === index ? value : header))
    );

    setChanges((prevChanges) => ({
      ...prevChanges,
      [headers[index]]: value,
    }));
  };


  const handleActionChange = (column, value) => {
    setAction((prevAction) => ({
      ...prevAction,
      [column]: value,
    }));
  };

  return (
    <div className="relative overflow-x-auto">
      <table className="min-w-full text-sm text-left text-gray-500 dark:text-gray-400">
        <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
          {editable && (
            <tr>
              {headerValues.map((header, index) => (
                <th key={`action-header-${index}`} className="px-6 py-3">
                  <select
                    className="border-gray-300 rounded-md min-w-32"
                    onChange={(e) => handleActionChange(header, e.target.value)}
                  >
                    <option value="">Action</option>
                    <option value="delete">Delete</option>
                    <option value="uppercase">Uppercase</option>
                    <option value="lowercase">Lowercase</option>
                    <option value="uc_first">UC First</option>
                  </select>
                </th>
              ))}
            </tr>
          )}
          <tr>
            {headerValues.map((header, index) => (
              <React.Fragment key={`header-${index}`}>
                {editable ? (
                  <th
                    className="px-6 py-3 cursor-pointer"
                    onDoubleClick={() => handleDoubleClick(index)}
                  >
                    {editingIndex === index ? (
                      <input
                        type="text"
                        value={headerValues[index]}
                        onBlur={handleBlur}
                        onKeyDown={handleKeyDown}
                        onChange={(e) => handleChangeInput(index, e.target.value)}
                        autoFocus
                        className="border rounded-md px-2 py-1 w-full"
                      />
                    ) : (
                      header
                    )}
                  </th>
                ) : (
                  <th className="px-6 py-3">{header}</th>
                )}
              </React.Fragment>
            ))}
          </tr>
        </thead>
        <tbody>
          {displayData.map((row, rowIndex) => (
            <tr key={rowIndex} className="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
              {Object.values(row).map((value, colIndex) => (
                <td key={colIndex} className="px-6 py-4 whitespace-nowrap">
                  {value}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>

  );
};

export default Table;
