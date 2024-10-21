import React, { useState } from "react";
import './index.css';

const Table = ({ headers, data, limit, editable = false, setChanges = () => { }, setAction = () => { } }) => {
  const displayData = limit ? data.slice(0, limit) : data;
  const [editingIndex, setEditingIndex] = useState(null);
  const [headerValues, setHeaderValues] = useState(headers);

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
    <div className="tableWrapper">
      <table className="styled-table">
        <thead>
          {editable && (
            <tr>
              {headerValues.map((header, index) => (
                <th key={`action-header-${index}`}>
                  <select
                    className="w-full"
                    onChange={(e) => handleActionChange(header, e.target.value)}
                  >
                    <option value="">Select Action</option>
                    <option value="uppercase">Uppercase</option>
                    <option value="delete">Delete</option>
                  </select>
                </th>
              ))}
            </tr>
          )}
          <tr>
            {headerValues.map((header, index) => (<>
              {editable ? (
                <th
                  key={`header-${index}`}
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
                    />
                  ) : (
                    header
                  )}
                </th>
              ) : (
                <th>{header}</th>
              )}
            </>
            ))}
          </tr>
        </thead>
        <tbody>
          {displayData.map((row, rowIndex) => (
            <tr key={rowIndex}>
              {Object.values(row).map((value, colIndex) => (
                <td key={colIndex}>{value}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Table;
