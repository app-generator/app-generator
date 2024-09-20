import React from "react";

const ComboBox = ({ csvFiles, handleFileSelection, selectedFile }) => {
  return (
    <div>
      <select
        id="csvSelect"
        onChange={handleFileSelection}
        value={selectedFile ? selectedFile.name : ""}
      >
        <option value="" disabled>
          Select Files
        </option>
        {csvFiles?.map((file, index) => (
          <option key={index} value={file.name}>
            {file.name}
          </option>
        ))}
      </select>
    </div>
  );
};

export default ComboBox;
