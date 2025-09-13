import React from 'react';

const ProductCard = ({ product, onClickFunc, productId }) => {
    return (
        <div 
            className={`col-span-3 md:col-span-1 border rounded-lg p-3 shadow-md ${product.id === productId ? 'border-gray-600 dark:border-gray-200' : 'border-gray-200 dark:border-gray-700'}`}
        >
            <div className="relative rounded-2xl aspect-[4/3] overflow-hidden mb-3 group">
                <img
                    src={`/static/product/${product.design}/${product.tech1}/top.png`}
                    alt={product.seo_title}
                    className="w-full aspect-[4/3] object-cover hover:scale-105 transition-transform duration-150 ease-in-out"
                />
                <div className="absolute inset-0 bg-black bg-opacity-50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg"></div>
                <div className="absolute inset-0 flex flex-col items-center justify-center space-y-2 opacity-0 group-hover:opacity-100 transition-opacity duration-300 px-16">
                    <button
                        onClick={() => onClickFunc(product.id)}
                        className="w-full text-center px-4 py-2 bg-white text-gray-900 font-medium rounded"
                    >
                        Get Discount 
                    </button>
                </div>
            </div>

            <div className="flex justify-between items-center mb-2">
                <h4 className="font-bold">
                    <p className='cursor-pointer dark:text-gray-200' onClick={() => onClickFunc(product.id)}>{product.name}</p>
                </h4>
                <h4 className="text-gray-900 dark:text-white font-bold">
                    <span className="text-red-600">${product.price}</span>
                </h4>
            </div>
            <p className="text-gray-500 dark:text-gray-300 text-sm mb-5">{product.card_info}</p>
            <div className="flex items-center justify-between gap-3">
                <a
                    href={product.url_demo}
                    target='_blank'
                    className="inline-flex items-center gap-2 py-2.5 px-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700"
                >
                    Demo
                    <svg className="w-5 h-5 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                        <path stroke="currentColor" strokeWidth="2" d="M21 12c0 1.2-4.03 6-9 6s-9-4.8-9-6c0-1.2 4.03-6 9-6s9 4.8 9 6Z"/>
                        <path stroke="currentColor" strokeWidth="2" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"/>
                    </svg>     
                </a>
                <button
                    onClick={() => onClickFunc(product.id)}
                    className="inline-flex items-center gap-2 text-white bg-blue-700 hover:bg-blue-800 hover:text-white focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-3 py-2.5 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
                >
                    Get Discount
                </button>
            </div>
        </div >
    );
};

export default ProductCard;
