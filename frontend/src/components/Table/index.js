import React from "react";
import InputField from "../InputField";
import './index.css';

const Table = ({
  headers,
  data,
  columnChanges,
  columnActions,
  handleColumnChange,
  handleActionChange,
}) => {
  return (
    <div>
      {/* Table for displaying CSV data */}
      <h3 className="tableHeading">CSV File</h3>
      <div className="tableWrapper">
      <table className="table">
        <thead>
          <tr className="headerRow">
            {headers.map((header, index) => (
              <th
                key={index}
            
              >
                {header}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.map((row, rowIndex) => (
            <tr key={rowIndex}>
              {Object.values(row).map((value, colIndex) => (
                <td
                  key={colIndex}
                
                >
                  {value}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
      </div>

      {/* Table for column changes and actions */}
      <h3 className="tableHeading">Process File</h3>
      <table className="table">
        <thead>
          <tr className="headerRow">
            <th>Column</th>
            <th>Change</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {headers.map((column, index) => (
            <tr key={index}>
              <td>
                {column}
              </td>
              <td>
                <InputField
                  column={column}
                  value={columnChanges[column]}
                  onChange={handleColumnChange}
                  placeholder="Type new column name"
                />
              </td>
              <td>
                <InputField
                  column={column}
                  value={columnActions[column]}
                  onChange={handleActionChange}
                  placeholder="Type action"
                />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Table;
