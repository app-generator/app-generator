import React from 'react';

const InputField = ({ column, value, onChange, placeholder }) => {
    return (
        <input
            type="text"
            value={value}
            onChange={(e) => onChange(column, e.target.value)}
            placeholder={placeholder}
            style={{ border: 'none' }}
        />
    );
};

export default InputField;
