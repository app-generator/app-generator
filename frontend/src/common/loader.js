import React, { useEffect } from 'react';
import { FaSpinner } from 'react-icons/fa';

const LoadingOverlay = ({ isLoading }) => {
    useEffect(() => {
        const handleBeforeUnload = (event) => {
            if (isLoading) {
                event.preventDefault();
                event.returnValue = "The page is still loading. Are you sure you want to leave?";
            }
        };

        if (isLoading) {
            window.addEventListener('beforeunload', handleBeforeUnload);
        } else {
            window.removeEventListener('beforeunload', handleBeforeUnload);
        }

        return () => {
            window.removeEventListener('beforeunload', handleBeforeUnload);
        };
    }, [isLoading]);

    if (!isLoading) return null;

    return (
        <>
            <style>
                {`
          @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
          }
        `}
            </style>

            <div
                style={{
                    position: 'fixed',
                    top: 0,
                    left: 0,
                    width: '100%',
                    height: '100%',
                    backgroundColor: 'rgba(0, 0, 0, 0.5)',
                    zIndex: 1000,
                    display: 'flex',
                    justifyContent: 'center',
                    alignItems: 'center',
                }}
            >
                <div style={{ textAlign: 'center', color: '#fff' }}>
                    <FaSpinner
                        size={50}
                        className="spinner"
                        style={{
                            animation: 'spin 1.5s linear infinite',
                        }}
                    />
                </div>
            </div>
        </>
    );
};

export default LoadingOverlay;
