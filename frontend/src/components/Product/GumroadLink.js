import React, { useEffect } from 'react';

export default function GumroadLink({ payUrl, promoCode, children }) {
    useEffect(() => {
        if (!document.querySelector('script[src*="gumroad.js"]')) {
            const script = document.createElement('script');
            script.src = 'https://gumroad.com/js/gumroad.js';
            script.async = true;
            document.head.appendChild(script);
        }
    }, []);

    const fullUrl = payUrl + (promoCode || '');

    return (
        <a 
            href={fullUrl}
            className="inline-flex items-center gap-2 text-white bg-blue-700 hover:bg-blue-800 hover:text-white focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-3 py-2.5 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
        >
            {children}
        </a>
    );
}