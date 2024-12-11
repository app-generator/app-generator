import React, { useState } from 'react';

const CustomSelect = ({
  options,
  value,
  onChange,
  placeholder,
  isClearable,
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedValue, setSelectedValue] = useState(value || null);

  const filteredOptions = options.filter((option) =>
    option.label.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const handleSelect = (selectedOption) => {
    setSelectedValue(selectedOption);
    onChange(selectedOption);
    setIsOpen(false);
  };

  const handleClear = (e) => {
    e.stopPropagation();
    setSelectedValue(null);
    onChange(null);
  };

  return (
    <div style={{ position: 'relative',  fontFamily: 'Arial, sans-serif' }}>
      {/* Select Box */}
      <div
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          padding: '8px 12px',
          border: '1px solid #ced4da',
          borderRadius: '4px',
          backgroundColor: 'white',
          cursor: 'pointer',
          fontSize: '14px',
          color: '#495057',
          boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)',
        }}
        onClick={() => setIsOpen(!isOpen)}
      >
        <div style={{ flexGrow: 1 }}>
          {selectedValue ? selectedValue.label : placeholder}
        </div>
        <div style={{ display: 'flex', alignItems: 'center' }}>
          {isClearable && selectedValue && (
            <span
              style={{
                color: '#6c757d',
                fontSize: '18px',
                cursor: 'pointer',
                marginRight: '10px',
                lineHeight: '1',
              }}
              onClick={handleClear}
            >
              ×
            </span>
          )}
          <span style={{ fontSize: '12px', color: '#6c757d' }}>
            {isOpen ? '▲' : '▼'}
          </span>
        </div>
      </div>

      {/* Dropdown */}
      {isOpen && (
        <div
          style={{
            position: 'absolute',
            width: '100%',
            border: '1px solid #ced4da',
            borderRadius: '4px',
            backgroundColor: 'white',
            boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
            marginTop: '4px',
            zIndex: 999,
          }}
        >
          {/* Search Box */}
          <input
            type="text"
            style={{
              width: '100%',
              padding: '8px 12px',
              border: 'none',
              borderBottom: '1px solid #ced4da',
              fontSize: '14px',
              boxSizing: 'border-box',
            }}
            placeholder="Search..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />

          {/* Options */}
          <div
            style={{
              maxHeight: '200px',
              overflowY: 'auto',
              padding: '0',
              margin: '0',
              listStyle: 'none',
            }}
          >
            {filteredOptions.length > 0 ? (
              filteredOptions.map((option) => (
                <div
                  key={option.value}
                  style={{
                    padding: '10px 12px',
                    cursor: 'pointer',
                    fontSize: '14px',
                    color: selectedValue?.value === option.value ? 'white' : '#495057',
                    backgroundColor: selectedValue?.value === option.value ? '#007bff' : 'transparent',
                    transition: 'background-color 0.2s ease, color 0.2s ease',
                  }}
                  onClick={() => handleSelect(option)}
                  onMouseEnter={(e) =>
                    (e.target.style.backgroundColor = selectedValue?.value === option.value
                      ? '#0056b3'
                      : '#f8f9fa')
                  }
                  onMouseLeave={(e) =>
                    (e.target.style.backgroundColor = selectedValue?.value === option.value
                      ? '#007bff'
                      : 'transparent')
                  }
                >
                  {option.label}
                </div>
              ))
            ) : (
              <div
                style={{
                  padding: '10px',
                  textAlign: 'center',
                  color: '#6c757d',
                  fontSize: '14px',
                }}
              >
                No options found
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default CustomSelect;
