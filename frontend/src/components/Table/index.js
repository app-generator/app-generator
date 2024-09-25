import React from "react";
import './index.css'

const Table = ({ headers, data,limit }) => {
  const displayData = limit ? data.slice(0, limit) : data;
  
  return (
    <div className="tableWrapper">
      <table className="styled-table">
        <thead>
          <tr>
            {headers.map((header, index) => (
              <th key={index}>{header}</th>
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
