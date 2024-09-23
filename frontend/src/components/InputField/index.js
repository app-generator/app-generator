import React from "react";

const InputField = ({ value, onChange, placeholder }) => {
  return (
    <input
      type="text"
      value={value}
      onChange={onChange}
      placeholder={placeholder}
      className="input-field"
      style={{ border: "none" }}
    />
  );
};

export default InputField;
